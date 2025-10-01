#Импортируем необходимые компоненты
#Модуль для работы с базой данный SQLite
import sqlite3
#Аннотация типов для лучшей читаемости кода
from typing import List, Tuple



class TaskDatabase(object):
    """Класс для работы с БД SQLite"""

    def __init__(self, db_name):
        """Инициализация базы данных"""
        # Сохраняем имя базы данных
        self.db_name = db_name
        # Создаем таблицу для инициализации
        self._create_table()


    def _create_table(self):
        """Создание таблицы задач, если она не существует"""
        #Используем контекстный менеджер для автоматического
        #управления соединением
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'не выполнено',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            #Подтверждение изменений в БД
            conn.commit()
    def add_task(self,title: str, description: str = "")-> int:
        """Добавление новой записи"""
        #управления соединением
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks(title,description)VALUES(?,?)",
                #Передаем параметры в кортеж
                (title,description)
            )
            #Сохраняем изменения
            conn.commit()
            #Возвращаем ID созданной записи
            return cursor.lastrowid

    def get_all_tasks(self) -> List[Tuple]:
        """Получение всех задач"""
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            # cursor.execute("SELECT * FROM tasks ORDER_BY created_at DESC")
            cursor.execute("SELECT * FROM tasks ")
            #Возвращаем все найденный записи
            return cursor.fetchall()

    def get_task_by_id(self, task_id: int) -> Tuple:
        """Получение задачи по ID"""
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor
            cursor.execute("SELECT * FROM tasks WHERE id=?",(task_id))
            #Возвращаем одку запись или None
            return cursor.fetchone()

    def update_task_status(self, task_id: int, status: str)-> bool:
        """Обновление статуса задачи"""
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE tasks SET status = ? WHERE id = ?",
                # Параметры: новый статус и ID задачи
                (status, rask_id)
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_task(self,task_id: int) -> bool:
        """Удаление записи"""
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            #Удаляем запись по ID
            cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id))
            conn.commit()
            #Возвращаем True, если была удалена хотя бы одна запись
            return cursor.rowcount > 0

    def search_task(self, keyword: str)->List[Tuple]:
        """Поиск задач по ключевому слову"""
        with sqlite3.connect(self.db_name) as conn:
            #Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()
            #Удаляем запись по ID
            cursor.execute(
                "SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ? ORDER BY created_at DESK",

                (f"%{keyword}%", f"%{keyword}%")#Любой текст до и после keyword
            )
            return cursor.fetchall()
