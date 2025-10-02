from database import TaskDatabase
from typing import List, Tuple

class TaskManager:
    """Класс для управления меню и взаимодействия с пользователем"""
    def __init__(self):
        """Инициализация менеджра задач"""
        self.db = TaskDatabase()

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

    def display_tasks(self, tasks: List[Tuple]):
        """Функция для отображения списка задач"""
        if not tasks:
            print("Задачи не найдены")
            return
        #Выводим заголовок таблицы с форматированием столбцов
        print(f"\n{'ID':<4} {'Статус':<15} {'Заголовок':<20} {'Описание':<30}")
        print("-"*70)
        for task in tasks:
            #Распаковываем кортеж с данными задач
            #Ожидаемая структура
            task_id, title, description, status, created_at = task
            #Форматируем заголовок
            title_display = title[:18]+".." if len(title)>20 else title
            #Форматируем описание
            desc_display = description[:28]+".." if len(description)>30 else description
            print(f"{task_id:<4} {status:<15} {title_display:<20} {desc_display:<30}")

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
        """Запуск основного цикла приложения"""
        print("Добро пожаловать в менеджер задач!")

        while True:
            self.display_menu()
            choice = input("Выберите действие(1-6): ").strip()
            if choice == '1':
                tasks = self.db.get_all_tasks()
                self.display_tasks(tasks)

            elif choice == '2':
                self.add_task_interactive()

            elif choice == '3':
                self.update_status_interactive()

            elif choice == '4':
                self.delete_task_interactive()

            elif choice == '5':
                self.search_tasks_interactive()

            elif choice == '6':
                print("До свидания!")
                break
            else:
                print("Неверный выбор! Пожалуйста, выберите действие от 1 до 6.")
            input('\nНажмите Enter для продолжения...')
                
            
        


        

    
            
        


            



    



        
