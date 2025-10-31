import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция падающих снежинок")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (30, 30, 70)

# Класс снежинки
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)

    def fall(self):
        self.y += self.speed
        self.x += self.wind

        # Если снежинка вышла за пределы экрана, создаем новую
        if self.y > HEIGHT or self.x < 0 or self.x > WIDTH:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(-50, 0)
            self.speed = random.uniform(1, 3)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Создание снежинок
snowflakes = [Snowflake() for _ in range(200)]

# Основной цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана
    screen.fill(BLUE)

    # Обновление и отрисовка снежинок
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
