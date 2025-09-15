#Импортируем необходимые компоненты
#Модуль для создания GUI
import tkinter as tk
#Модуль для тематических виджетов(вкладки и т.д.)
from tkinter import ttk
#Модуль для получения системной информации
import psutil
#Модуль для работы со временем
import time
#Математический модуль
import math
#Модуль для многопоточности
import threading
#Структура данных "двухсторонняя очередь"
from collections import deque

class PerformanceMonitor:
    def __init__(self,root):
    #Инициилизация главного окна приложения
        #Сохранение ссылки на главное меню
        self.root = root
        #Установка заголовка окна
        self.root.title("Монитор производительности")
        #Установка размеров окна(ширина х высота)
        self.root.geometry("800x600")
        #Настровка данных графиков
        #Cоздание очередей для хранения последних
        #100 значений каждого параметра
        #Данные использования CPU
        self.cpu_data = deque([0]*100, maxlen=100)
        #Данные использования памяти
        self.memory_data = deque([0]*100, maxlen=100)
        #Данные использования диска
        self.disk_data = deque([0]*100, maxlen=100)
        #Данные сетевой активности
        self.network_data = deque([0]*100, maxlen=100)

        #Вызов метода для настройки пользовательского интефейса
        self.setup_ui()
        #Флаг для управления циктом мониторинга
        self.running = True
        #Запуск мониторинга производительности
        self.start_monitoring()

    def setup_ui(self):
        #Создаем вкладки для отображения различных метрик
        #Cоздание виджета вкладок
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill = 'both',expand = True, padx = 10, pady = 10)

        #Вкладка CPU
        #Создание фрейма для вкладки CPU
        cpu_frame = ttk.Frame(notebook)
        #Добавляе вкладки с названием
        notebook.add(cpu_frame, text = "Процессор")
        #Холст для рисования графика CPU
        self.cpu_canvas = tk.Canvas (cpu_frame,bg='white', height = 200)
        #Размещение холста
        self.cpu_canvas.pack (fill = 'both',expand = True, padx = 10, pady = 10)

        #Вкладка память
        #Создание фрейма для вкладки памяти
        memory_frame = ttk.Frame(notebook)
        #Добавляе вкладки с названием
        notebook.add(memory_frame, text = "Память")
        #Холст для рисования графика памяти
        self.memory_canvas = tk.Canvas (memory_frame,bg='white', height = 200)
        #Размещение холста
        self.memory_canvas.pack (fill = 'both',expand = True, padx = 10, pady = 10)

        #Вкладка диск
        #Создание фрейма для вкладки диск
        disk_frame = ttk.Frame(notebook)
        #Добавляе вкладки с названием
        notebook.add(disk_frame, text = "Диск")
        #Холст для рисования графика памяти
        self.disk_canvas = tk.Canvas (disk_frame,bg='white', height = 200)
        #Размещение холста
        self.disk_canvas.pack (fill = 'both',expand = True, padx = 10, pady = 10)

        #Вкладка сеть
        #Создание фрейма для вкладки сеть
        network_frame = ttk.Frame(notebook)
        #Добавляе вкладки с названием
        notebook.add(network_frame, text = "Сеть")
        #Холст для рисования графика памяти
        self.network_canvas = tk.Canvas (network_frame,bg='white', height = 200)
        #Размещение холста
        self.network_canvas.pack (fill = 'both',expand = True, padx = 10, pady = 10)

        #Статистика внизу окна
        #Фрейм статистики
        stats_frame = ttk.Frame(self.root)
        # Размещение с заполнением по ширине
        stats_frame.pack(fill = 'x', padx = 10, pady = 5)

        #Метки для отображения текущих значений
        #метка использования CPU
        self.cpu_label = ttk.Label(stats_frame, text = 'CPU: 0%')
        self.cpu_label.pack(side='left', padx = 5)
        #метка использования памяти
        self.memory_label = ttk.Label(stats_frame, text = 'Память: 0%')
        self.memory_label.pack(side='left', padx = 5)
        #метка использования диска
        self.disk_label = ttk.Label(stats_frame, text = 'Диск: 0%')
        self.disk_label.pack(side='left', padx = 5)
        #метка использования сети
        self.network_label = ttk.Label(stats_frame, text = 'Сеть: 0%')
        self.network_label.pack(side='left', padx = 5)

        #Кнопка для выхода из приложения
        exit_button = ttk.Button(self.root, text = "Выход",command = self.exit_app)
        exit_button.pack(pady = 5)

    #Метод для рисования графика на холсте
    def draw_graph(self, canvas, data, color, title, max_value = 100):
        #Очистка холста перед рисование
        canvas.delete("all")
        #Получение текущего размера холста
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        #Проверка на минимальные размеры(избегаем ошибок)
        if width <=1 or height <=1:
            return
        #Рисуем сетку на фоне графика
        for i in range(0,101,20):# Линии каждые 20%
            #Расчет позиции Y для линии сетки
            y= height - (i/100*height)
            canvas.create_line(0,y,widht, y ,fill = 'lightgrey',dash = (2,2))
            #Подпись значения на сетке
            canvas.create_text(5,y, text = f'{i}%', anchor = 'sw', fill = 'gray')
        #Рисуем сам график
        points = []
        #Перебор всех данных
        for i, value in enumerate(data):
            #Расчет позиции Х
            x =(i / len(data))* wight
            #Расчет позиции Y
            y = height - (value/ max_value * height)
            points.append((x,y))
        #Соединяем точки линиями
        if len(points)>1:#Проверка, что есть хотябы 2 точки
            for i in range(len(points)-1):
                #От текущей точки
                canvas.create_line(points[i][0],points[i][1],
                points[i+1][0],points[i+1][1],
                fill = color, wight = 2)
                
                #Добавляем заголовок графика
                canvas.create_text(width//2,15,text = title, font = ('Arial',
                           12,'bold'))
    #Метод получения данных
    def get_performance_data(self):
        #Процессор
        pu_percent = psutil.cpu_percent(interval = 0.1)

        #
    def update_data(self):
        cpu = self.get_performance_data()
        #Обновляем текущще значение
        self.cpu_data.append(cpu)

        #Обновляет текстовые метки
        self.cpu_label.config(text = f'CPU: {cpu: .1f}%')
        #Перерисовываем график
        self.draw_graph(self.cpu_canvas, self.cpu_data,'red',
                            'Использование процессора')
        #Бесконечный цикл
    def monitoring_loop(self):
        while self.running:
            #Обновляем данные
            self.update_data()
            time.sleep(1)
        #Создаем фоновый поток для мониторинга
    def start_monitoring(self):
        self_monitor_thread = threading.Thread(target = self.monitoring_loop, daemon = True)

        self.update_ui()

    #периодическое обновление UI(каждую секунду)
    def update_ui(self):
        if self.running:
            self.root.after(1000, self.update_ui)
    #Остановка мониторинга
    def exit_app(self):
        #Останавливаем мониторинг
        self.running = False
        #Завершаем главный цикл Tkinter
        self.root.quit()
        #Уничтожаем окно
        self.root.destroy()
        

        

        

def main():
    #Проверяем наличие psutil(входит в стандартную
    #поставку дистрибутивов Python)
    try:
        import psutil
    except ImportError:
        print('Ошибка. Модуль psutil не установлен.')
        print('Установите его с помощью pip install')
        return
    #Создаем главное окно Tkinter
    root = tk.Tk()
    #Создаем экземпляр приложения
    app = PerformanceMonitor(root)
#Стандартная проверка для запуска основной программы
if __name__ == "__main__":
    main()

  
    







