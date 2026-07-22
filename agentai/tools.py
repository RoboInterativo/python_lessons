from langchain.tools import tool
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from datetime import datetime
import json

# Настройка инструментов
search = DuckDuckGoSearchRun()
wiki_api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki = WikipediaQueryRun(api_wrapper=wiki_api)

@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Сохраняет структурированные исследовательские данные в текстовый файл.
    
    Args:
        data: Данные для сохранения
        filename: Имя файла для сохранения (по умолчанию: research_output.txt)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Данные успешно сохранены в {filename}"

@tool
def search_tool(query: str) -> str:
    """
    Поиск информации в интернете.
    
    Args:
        query: Поисковый запрос
    """
    try:
        return search.run(query)
    except Exception as e:
        return f"Ошибка поиска: {str(e)}. Попробуйте изменить запрос."

@tool
def wiki_tool(query: str) -> str:
    """
    Поиск информации в Wikipedia.
    
    Args:
        query: Поисковый запрос
    """
    try:
        result = wiki.run(query)
        if not result or len(result.strip()) < 10:
            return f"Не найдено информации в Wikipedia по запросу: {query}"
        return result
    except Exception as e:
        return f"Ошибка Wikipedia: {str(e)}. Попробуйте другой запрос."