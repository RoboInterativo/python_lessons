import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Снеговик")

# Цвета
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BROWN = (101, 67, 33)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Функция для рисования снеговика
def draw_snowman(x, y, size=1.0):
    # Координаты центра снеговика
    center_x = x
    center_y = y

    # Размеры шаров (нижний, средний, верхний)
    bottom_radius = int(80 * size)
    middle_radius = int(60 * size)
    top_radius = int(40 * size)

    # Рисуем снежные шары (снизу вверх)
    # Нижний шар
    pygame.draw.circle(screen, WHITE, (center_x, center_y), bottom_radius)
    pygame.draw.circle(screen, BLACK, (center_x, center_y), bottom_radius, 2)  # контур

    # Средний шар
    middle_y = center_y - bottom_radius - middle_radius + 10
    pygame.draw.circle(screen, WHITE, (center_x, middle_y), middle_radius)
    pygame.draw.circle(screen, BLACK, (center_x, middle_y), middle_radius, 2)  # контур

    # Верхний шар (голова)
    top_y = middle_y - middle_radius - top_radius + 10
    pygame.draw.circle(screen, WHITE, (center_x, top_y), top_radius)
    pygame.draw.circle(screen, BLACK, (center_x, top_y), top_radius, 2)  # контур

    # Глаза
    eye_radius = int(6 * size)
    pygame.draw.circle(screen, BLACK, (center_x - 12 * size, top_y - 5 * size), eye_radius)
    pygame.draw.circle(screen, BLACK, (center_x + 12 * size, top_y - 5 * size), eye_radius)

    # Нос (морковка)
    nose_points = [
        (center_x, top_y + 5 * size),
        (center_x + 25 * size, top_y),
        (center_x, top_y + 10 * size)
    ]
    pygame.draw.polygon(screen, ORANGE, nose_points)

    # Рот (пуговки)
    for i in range(5):
        mouth_x = center_x - 10 * size + i * 5 * size
        mouth_y = top_y + 15 * size
        pygame.draw.circle(screen, BLACK, (int(mouth_x), int(mouth_y)), int(3 * size))

    # Пуговицы на среднем шаре
    for i in range(3):
        button_y = middle_y - 10 * size + i * 20 * size
        pygame.draw.circle(screen, BLACK, (center_x, int(button_y)), int(8 * size))

    # Шляпа
    hat_y = top_y - top_radius
    # Поля шляпы
    pygame.draw.rect(screen, BLACK,
                    (center_x - 40 * size, hat_y, 80 * size, 10 * size))
    # Верх шляпы
    pygame.draw.rect(screen, BLACK,
                    (center_x - 20 * size, hat_y - 30 * size, 40 * size, 35 * size))

    # Руки (ветки)
    arm_length = 70 * size
    # Левая рука
    pygame.draw.line(screen, BROWN,
                    (center_x - middle_radius, middle_y),
                    (center_x - middle_radius - arm_length, middle_y - 30 * size),
                    int(5 * size))
    # Правая рука
    pygame.draw.line(screen, BROWN,
                    (center_x + middle_radius, middle_y),
                    (center_x + middle_radius + arm_length, middle_y - 30 * size),
                    int(5 * size))

    # Шарф
    scarf_width = 30 * size
    # Вертикальная часть шарфа
    pygame.draw.rect(screen, RED,
                    (center_x - scarf_width//2, middle_y - 15 * size,
                     scarf_width, middle_radius + 15 * size))

    # Концы шарфа
    scarf_end_length = 50 * size
    # Левый конец
    pygame.draw.rect(screen, RED,
                    (center_x - scarf_width//2 - scarf_end_length,
                     middle_y + middle_radius,
                     scarf_end_length, 10 * size))
    # Правый конец
    pygame.draw.rect(screen, RED,
                    (center_x + scarf_width//2,
                     middle_y + middle_radius,
                     scarf_end_length, 10 * size))

# Функция для рисования снежинок
def draw_snowflakes(snowflakes):
    for flake in snowflakes:
        x, y, size, speed = flake
        # Рисуем снежинку (простой крестик)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), int(size))
        pygame.draw.line(screen, WHITE, (x - size, y), (x + size, y), 1)
        pygame.draw.line(screen, WHITE, (x, y - size), (x, y + size), 1)

        # Обновляем позицию снежинки
        flake[1] += speed  # двигаем вниз
        flake[0] += math.sin(flake[1] * 0.01) * 0.5  # немного влево-вправо

        # Если снежинка упала за экран, возвращаем ее наверх
        if flake[1] > HEIGHT:
            flake[1] = 0
            flake[0] = flake[0] % WIDTH

# Основной цикл
running = True
clock = pygame.time.Clock()

# Создаем список снежинок
snowflakes = []
for _ in range(100):
    x = pygame.time.get_ticks() % WIDTH  # разное начальное положение
    y = pygame.time.get_ticks() % HEIGHT
    size = pygame.time.get_ticks() % 3 + 1  # размер 1-3
    speed = pygame.time.get_ticks() % 2 + 0.5  # скорость 0.5-2.5
    snowflakes.append([x, y, size, speed])

# Снег на земле
snow_height = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Заполнение фона (небо)
    screen.fill(SKY_BLUE)

    # Снег на земле
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - snow_height, WIDTH, snow_height))

    # Рисуем снежинки
    draw_snowflakes(snowflakes)

    # Рисуем снеговика
    draw_snowman(WIDTH // 2, HEIGHT - snow_height - 50, 1.2)

    # Рисуем маленького снеговика справа
    draw_snowman(WIDTH - 150, HEIGHT - snow_height - 30, 0.7)

    # Рисуем солнце
    sun_radius = 50
    pygame.draw.circle(screen, YELLOW, (100, 100), sun_radius)

    # Лучи солнца
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        start_x = 100 + (sun_radius + 5) * math.cos(rad)
        start_y = 100 + (sun_radius + 5) * math.sin(rad)
        end_x = 100 + (sun_radius + 20) * math.cos(rad)
        end_y = 100 + (sun_radius + 20) * math.sin(rad)
        pygame.draw.line(screen, YELLOW, (start_x, start_y), (end_x, end_y), 3)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
