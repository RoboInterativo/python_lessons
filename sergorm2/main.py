#Импорт класса TaskManager из модуля menu
from taskmanager import TaskManager

def main():
    """Главная функция приложения"""
    try:
        #Создание экземпляра класса
        app = TaskManager('newdb')
        #Запускаем основной цикл приложения
        app.run()
    #Обработка прерывания от клавиатуры(Ctrl+C)
    except KeyboardInterrupt:
        print("\n\nПриложение завершено пользователем.")
    #Обработка всех остальных исключений
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
