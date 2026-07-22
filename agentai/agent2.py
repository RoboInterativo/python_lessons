from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain_core.utils.uuid import uuid7
from langchain_openai import ChatOpenAI
from tools import search_tool, wiki_tool, save_to_txt
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from datetime import datetime
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

import os


load_dotenv()
YANDEX_CLOUD_API_KEY = os.getenv("YANDEX_CLOUD_API_KEY")
YANDEX_CLOUD_FOLDER = os.getenv("YANDEX_CLOUD_FOLDER")
# YANDEX_GPT_MODEL = os.getenv("YANDEX_GPT_MODEL")
YANDEX_GPT_MODEL="gpt://b1g7m5u10ln6tbv85e75/deepseek-v4-flash/latest"

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

tools = [search_tool, wiki_tool, save_to_txt]  # Исправлено: save_to_txt вместо save_tool

#llm= ChatOllama(model="qwen2.5:7b")

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



prompt = ChatPromptTemplate.from_messages([
    ("system", """
      Ты — научный ассистент, который поможет сгенерировать научную статью.  
    Ответь на запрос пользователя и используй необходимые инструменты.  
    Оформи вывод в этом формате и не предоставляй никакого другого текста:
    Wrap the output in this format and provide no other text {format}
    """),
    ("human", """
    
    
    Вопрос: {content}
    """)
])



agent = create_agent(
    llm,
    tools=tools,    
    system_prompt=prompt  ,
)

# Запускаем агента
#query = input("Что я могу помочь тебе изучить? ")
import json
from datetime import datetime

# Запускаем агента
query = input("Что я могу помочь тебе изучить? ")

try:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )
    
    print("\n" + "="*60)
    print("📊 АНАЛИЗ ВЫПОЛНЕНИЯ ЗАПРОСА")
    print("="*60)
    
    # 1. Анализ использованных инструментов
    print("\n🔧 ИСПОЛЬЗОВАННЫЕ ИНСТРУМЕНТЫ:")
    tools_used = []
    tools_errors = []
    
    for msg in result["messages"]:
        # Проверяем вызовы инструментов
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            for tool_call in msg.tool_calls:
                tool_name = tool_call.get('name', 'unknown')
                tool_args = tool_call.get('args', {})
                tools_used.append({
                    'name': tool_name,
                    'args': tool_args,
                    'id': tool_call.get('id', '')
                })
                print(f"  ✅ {tool_name}({', '.join([f'{k}={v}' for k, v in tool_args.items()])})")
        
        # Проверяем результаты инструментов (ToolMessage)
        if hasattr(msg, 'type') and msg.type == 'tool':
            if 'Ошибка' in str(msg.content) or 'error' in str(msg.content).lower():
                tools_errors.append({
                    'tool': msg.name,
                    'error': msg.content
                })
                print(f"  ❌ {msg.name}: ОШИБКА - {msg.content[:100]}...")
    
    # 2. Статистика
    print("\n📈 СТАТИСТИКА:")
    print(f"  Всего вызовов инструментов: {len(tools_used)}")
    print(f"  Успешных: {len(tools_used) - len(tools_errors)}")
    print(f"  С ошибками: {len(tools_errors)}")
    
    # 3. Финальный ответ
    final_message = result["messages"][-1].content
    print("\n📝 ФИНАЛЬНЫЙ ОТВЕТ АГЕНТА:")
    
    # Пробуем распарсить как JSON
    try:
        # Ищем JSON в ответе
        import re
        json_match = re.search(r'\{.*\}', final_message, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            data = json.loads(json_str)
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(final_message[:500] + "..." if len(final_message) > 500 else final_message)
    except:
        print(final_message[:500] + "..." if len(final_message) > 500 else final_message)
    
    # 4. Сохраняем полный отчет
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report = {
        'query': query,
        'timestamp': timestamp,
        'tools_used': tools_used,
        'tools_errors': tools_errors,
        'final_response': final_message,
        'full_result': str(result)
    }
    
    with open(f'research_report_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Полный отчет сохранен в: research_report_{timestamp}.json")
    print("="*60)
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    if 'result' in locals():
        print("\nСырой результат:")
        print(result)


# result = agent.invoke(
#         {"messages": [{"role": "user", "content": query}]}
# )

# print (result)

# structured_response = parser.parse(result["messages"][-1].content)

# # Конвертируем в словарь
# response_dict = structured_response.dict()

# # Добавляем метаданные
# response_dict['timestamp'] = datetime.now().isoformat()
# response_dict['query'] = query

# # Выводим в консоль
# print("\n=== Результат исследования ===")
# print(json.dumps(response_dict, ensure_ascii=False, indent=2))