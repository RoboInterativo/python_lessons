from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage
from langchain_core.output_parsers import PydanticOutputParser

from tools import search_tool, wiki_tool, save_to_txt  # Исправлено: save_to_txt вместо save_tool

import os
from collections.abc import Callable
from langchain.tools.tool_node import ToolCallRequest

load_dotenv()

# Определение класса должно быть ДО его использования
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

YANDEX_CLOUD_API_KEY = os.getenv("YANDEX_CLOUD_API_KEY")
YANDEX_CLOUD_FOLDER = os.getenv("YANDEX_CLOUD_FOLDER")
YANDEX_GPT_MODEL = os.getenv("YANDEX_GPT_MODEL")

# llm = ChatOpenAI(
#     base_url="https://ai.api.cloud.yandex.net/v1",
#     api_key=YANDEX_CLOUD_API_KEY,
#     model=f"gpt://{YANDEX_CLOUD_FOLDER}/{YANDEX_GPT_MODEL}/latest",
#     default_headers={"x-folder-id": YANDEX_CLOUD_FOLDER},
#     temperature=0.3,
#     max_tokens=500,
# )
llm = ChatOpenAI(
    base_url="https://llm.api.cloud.yandex.net/v1",  # Исправленный URL
    api_key=YANDEX_CLOUD_API_KEY,
    model=YANDEX_GPT_MODEL,  # Просто имя модели, без gpt:// префикса
    default_headers={
        "x-folder-id": YANDEX_CLOUD_FOLDER,
        "Authorization": f"Api-Key {YANDEX_CLOUD_API_KEY}"  # Добавляем Authorization header
    },
    temperature=0.3,
    max_tokens=500,
)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Создаем middleware для обработки ошибок
@wrap_tool_call
def handle_tool_errors(
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], ToolMessage],
) -> ToolMessage:
    """Обработка ошибок инструментов."""
    try:
        return handler(request)
    except Exception as e:
        return ToolMessage(
            content=f"Ошибка инструмента: {str(e)}",
            tool_call_id=request.tool_call["id"],
        )

tools = [search_tool, wiki_tool, save_to_txt]  # Исправлено: save_to_txt вместо save_tool
format=parser.get_format_instructions()

# Создаем агента с новым API
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=promt,
    middleware=[handle_tool_errors]
)

# Запускаем агента
query = input("Что я могу помочь тебе изучить? ")

try:
    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )
    
    # Извлекаем финальный ответ агента
    final_message = response["messages"][-1].content
    
    # Парсим ответ
    structured_response = parser.parse(final_message)
    print(structured_response)
    
except Exception as e:
    print(f"Error: {e}")
    if 'response' in locals():
        print(f"Raw Response: {response}")