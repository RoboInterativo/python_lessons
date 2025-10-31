import os
import subprocess
import sys

def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Вывод меню"""
    print("=" * 40)
    print("         МЕНЮ ЗАПУСКА PYTHON СКРИПТОВ")
    print("=" * 40)
    print("1 - Запустить симуляцию снежинок")
    print("2 - Запустить симуляцию снежинок с накоплением")
    print("3 - Запустить симуляцию снежинок с накоплением 2")
    print("4 - Запустить симуляцию шариков")
    print("5 - Запустить симуляцию шариков 2")
    print("6 - Запустить симуляцию шариков расчет растояния")
    print("0 - Выход")
    print("-" * 40)

def run_script(script_name):
    """Запуск Python скрипта"""
    try:
        if os.path.exists(script_name):
            print(f"Запуск {script_name}...")
            print("-" * 40)
            result = subprocess.run([sys.executable, script_name], check=True)
            if result.returncode == 0:
                print(f"\n{script_name} завершен успешно!")
            else:
                print(f"\n{script_name} завершен с ошибкой!")
        else:
            print(f"Файл {script_name} не найден!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске {script_name}: {e}")
    except KeyboardInterrupt:
        print(f"\nЗапуск {script_name} прерван пользователем")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    input("\nНажмите Enter для продолжения...")

def main():
    """Основная функция меню"""
    scripts = {
        '1': 'snow.py',
        '2': 'snow2.py',
        '3': 'snow3.py',
        '4': 'balls.py',
        '5': 'ball_s.py',
        '6': 'ball_n.py'
    }

    while True:
        clear_screen()
        print_menu()

        choice = input("Выберите пункт меню: ").strip()

        if choice == '0':
            print("Выход из программы...")
            break
        elif choice in scripts:
            run_script(scripts[choice])
        else:
            print("Неверный выбор! Попробуйте снова.")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
