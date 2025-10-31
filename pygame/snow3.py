import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция падающих снежинок с накоплением")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (30, 30, 70)
DARK_BLUE = (20, 20, 50)

# Класс снежинки
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)
        self.accumulated = False  # Флаг, указывающий, что снежинка накопилась
        self.accumulated_y = HEIGHT  # Y-координата, где снежинка остановилась

    def fall(self, accumulated_snow):
        # Если снежинка уже накопилась, не двигаем ее
        if self.accumulated:
            return

        self.y += self.speed
        self.x += self.wind

        # Проверяем, достигла ли снежинка накопленного снега или низа экрана
        target_y = HEIGHT
        if accumulated_snow:
            # Находим самую высокую точку накопленного снега в колонке x
            column_x = int(self.x)
            if 0 <= column_x < WIDTH:
                target_y = accumulated_snow[column_x]

        # Если снежинка достигла накопленного снега или низа экрана
        if self.y >= target_y:
            self.accumulated = True
            self.y = target_y - 1
            self.accumulated_y = self.y
            return True  # Возвращаем True, чтобы обновить накопленный снег

        # Если снежинка вышла за боковые границы, создаем новую
        if self.x < 0 or self.x > WIDTH:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(-50, 0)

        return False

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Функция для обновления уровня накопленного снега
def update_accumulated_snow(accumulated_snow, x, y):
    column = int(x)
    if 0 <= column < WIDTH:
        accumulated_snow[column] = min(accumulated_snow[column], y)
    return accumulated_snow

# Создание снежинок
snowflakes = [Snowflake() for _ in range(300)]

# Массив для хранения уровня накопленного снега (изначально дно экрана)
accumulated_snow = [HEIGHT] * WIDTH

# Основной цикл
clock = pygame.time.Clock()
running = True
snow_level = HEIGHT  # Уровень снега (начинается с низа экрана)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана
    screen.fill(DARK_BLUE)

    # Рисуем накопленный снег
    for x in range(WIDTH):
        snow_height = HEIGHT - accumulated_snow[x]
        if snow_height > 0:
            pygame.draw.line(screen, WHITE, (x, accumulated_snow[x]), (x, HEIGHT), 1)

    # Обновление и отрисовка снежинок
    for snowflake in snowflakes:
        if snowflake.fall(accumulated_snow):
            # Если снежинка накопилась, обновляем уровень снега
            accumulated_snow = update_accumulated_snow(accumulated_snow, snowflake.x, snowflake.y)
        snowflake.draw()

    # Добавляем новые снежинки, если нужно
    if len([s for s in snowflakes if not s.accumulated]) < 150:
        snowflakes.append(Snowflake())

    # Удаляем старые снежинки, если их слишком много (для оптимизации)
    if len(snowflakes) > 400:
        # Удаляем некоторые накопленные снежинки
        accumulated_flakes = [s for s in snowflakes if s.accumulated]
        if len(accumulated_flakes) > 200:
            # Оставляем только последние 200 накопленных снежинок
            snowflakes = [s for s in snowflakes if not s.accumulated] + accumulated_flakes[-200:]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
