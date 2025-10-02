from typing import List, Tuple
import curses
import sqlite3
#Аннотация типов для лучшей читаемости кода
from typing import List, Tuple

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.is_completed})>"





class TaskManager:
    """Класс для управления меню и взаимодействия с пользователем"""
    def __init__(self,db_name):
        """Инициализация менеджра задач"""

        db_name = f"sqlite:///{db_name}"
        self.engine = create_engine(db_name, echo=True)  # echo=True для отладки
        self.Session = sessionmaker(bind=self.engine)

        # Создаем таблицы
        self._create_tables()

    def _create_tables(self):
        """Создание таблиц"""
        Base.metadata.create_all(self.engine)

    def display_menu(self):
        """Отображение главного меню"""
        print("\n"+"="*50)
        print("МЕНЕДЖЕР ЗАДАЧ")
        print("\n"+"="*50)
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Обновить статус задачи")
        print("4. Удалить задачу")
        print("5. Поик задач")
        print("6. Выход")
        print("\n"+"="*50)

    def display_tasks2(self ):
        """Функция для отображения списка задач"""

        """Получение всех задач"""
        session = self.Session()
        try:
            tasks= session.query(Task).order_by(Task.created_at.desc()).all()
        finally:
            session.close()

        if not tasks:
            print("Задачи не найдены")
            return
        #Выводим заголовок таблицы с форматированием столбцов
        print(f"\n{'ID':<4} {'Статус':<15} {'Заголовок':<20} {'Описание':<30}")
        print("-"*70)
        for task in tasks:
            #print(task)
            #Распаковываем кортеж с данными задач
            #Ожидаемая структура
            task_id, title, description, status, created_at = task
            #Форматируем заголовок
            title_display = title[:18]+".." if len(title)>20 else title
            #Форматируем описание
            desc_display = description[:28]+".." if len(description)>30 else description
            print(f"{task_id:<4} {status:<15} {title_display:<20} {desc_display:<30}")
    def display_tasks(self):
            """Функция для отображения списка задач"""

            """Получение всех задач"""
            session = self.Session()
            try:
                tasks= session.query(Task).order_by(Task.created_at.desc()).all()
            finally:
                session.close()

            if not tasks:
                print("Задачи не найдены")
                return
    def add_task_interactive(self):
        """Интерактивное добавление задачи"""
        print("\n --- ДОБАВЛЕНИЕ НОВОЙ ЗАДАЧИ ---")
        title = input("Введите заголовок задачи: ").strip()

        if not title:
            print("Ошибка: заголовок не может быть пустым")
            return

        description = input("Введите описание задачи(необязательно): ").strip()
        task_id = self.db.add_task(title, description)
        print(f"Задача успешно добавлена! ID: {task_id}")

    def update_status_interactive(self):
        """Интерактивное обновление статуса задачт"""
        print("\n --- ОБНОВЛЕНИЕ СТАТУСА ЗАДАЧИ ---")

        try:
            task_id = int(input("Введите ID задачи: "))
        except:
            print("Ошибка: введите корректный числовой ID")
            return
        task = self.db.get_task_by_id(task_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена")
            return

        print(f"Текущая задача: {task[1]}- {task[3]}")
        print('Доступные статусы: ')
        print("1. не выполнено ")
        print("2. в процессе ")
        print("3. выполнено")

        choice = input("Выберите новый статус(1-3)").strip()
        status_map = {
            '1': 'не выолнено',
            '2': 'в процессе',
            '3': 'выполнено'
        }
        if choice in status_map:
            new_status = status_map[choice]
            if self.db.update_task_status(task_id, new_status):
                print(f"Статус успешно обновлен на: {new_status}")
            else:
                print("Ошибка при обновлении статуса")
        else:
            print("Неверный выбор статуса!")

    def delete_task_interactive(self):
        """Интерактивное удаление задачи"""
        print("\n--- УДАЛЕНИЕ ЗАДАЧИ ---")

        try:
            task_id = int(input("Введите ID задачи для удаления: "))
        except ValueError:
            print("Ошибка: введите корректный числовой ID")
            return
        task = self.db.get_task_by_id(task_id)
        if not task:
            print(f"Задачап с ID {task_id} не найдена!")
            return
        print(f"Вы уверены, что хотите удалить задачу: '{task[1]}'?")
        confirmation = input("Введите 'да', для подтверждения: ").strip().lower()

        if confirmation == 'да':
            if self.db.delete_task(task_id):
                print("Задача успешно удалена")
            else:
                print("Ошибка при удалении задачи")
        else:
            print('Удаление отменено')
    def search_tasks_interactive(self):
        """Интерактивный поиск задач"""
        print("\n--- ПОИСК ЗАДАЧ ---")
        keyword = input("Введите ключевое слово для поиска: ").strip()

        if not keyword:
            print("Ошибка: ключевое слово не может быть пустым!")
            return

        tasks = self.db.search_task(keyword)
        if tasks:
            print(f"\nНайдено задач: {len(tasks)}")
            self.display_tasks(tasks)
        else:
            print("Задачи по Ващему запросу могут быть не найдены.")

    def run(self):
        def use_curses(stdscr):
            """Запуск основного цикла приложения"""
            #print("Добро пожаловать в менеджер задач!")
            curses.start_color()
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

            # Clear screen and set up initial display
            stdscr.clear()
            menuitems=[
            "Показать все задачи",
            "Добавить задачу",
            "Обновить статус задачи",
            "Удалить задачу",
            "Поиcк задач",
            "Выход"


            ]
            stdscr.addstr(0, 0, "МЕНЕДЖЕР ЗАДАЧ", curses.A_BOLD)
            for i, item in enumerate(menuitems):

                stdscr.addstr(i+2, 0, f"{i}. {item}" )

            stdscr.refresh()

            current_row = 2 # Start at the first option
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
            stdscr.attroff(curses.color_pair(1))
            stdscr.refresh()

            while True:
                key = stdscr.getch()

                if key == curses.KEY_UP and current_row > 2:
                    # Deselect current
                    stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
                    current_row -= 1
                    # Select new
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
                    stdscr.attroff(curses.color_pair(1))
                elif key == curses.KEY_DOWN and current_row < len(menuitems)+1:
                    # Deselect current
                    stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
                    current_row += 1
                    # Select new
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
                    stdscr.attroff(curses.color_pair(1))
                elif key == ord('\n'): # Enter key
                    if current_row == 2:
                        stdscr.addstr(6, 0, "You selected Option One!")
                    elif current_row == 3:
                        stdscr.addstr(6, 0, "You selected Option Two!")
                    elif current_row == 7:
                        break # Exit the loop
                    stdscr.refresh()
                    stdscr.getch() # Wait for another key press

                stdscr.refresh()
        curses.wrapper(use_curses)
        #while True:
            # self.display_menu()
            # choice = input("Выберите действие(1-6): ").strip()
            # if choice == '1':
            #     tasks = self.db.get_all_tasks()
            #     #print(tasks)
            #     self.display_tasks(tasks)
            #
            # elif choice == '2':
            #     self.add_task_interactive()
            #
            # elif choice == '3':
            #     self.update_status_interactive()
            #
            # elif choice == '4':
            #     self.delete_task_interactive()
            #
            # elif choice == '5':
            #     self.search_tasks_interactive()
            #
            # elif choice == '6':
            #     print("До свидания!")
            #     break
            # else:
            #     print("Неверный выбор! Пожалуйста, выберите действие от 1 до 6.")
            # input('\nНажмите Enter для продолжения...')
