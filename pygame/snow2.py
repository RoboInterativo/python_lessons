import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая симуляция снега")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (30, 30, 70)

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.wind = random.uniform(-0.5, 0.5)
        self.stopped = False

    def fall(self):
        if self.stopped:
            return

        self.y += self.speed
        self.x += self.wind

        # Останавливаемся при достижении низа экрана
        if self.y >= HEIGHT - 5:
            self.stopped = True
            self.y = HEIGHT - 5

        # Если вышли за боковые границы, создаем новую
        if self.x < 0 or self.x > WIDTH:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(-50, 0)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

snowflakes = [Snowflake() for _ in range(200)]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    # Добавляем новые снежинки взамен остановившихся
    stopped_count = sum(1 for s in snowflakes if s.stopped)
    if stopped_count < 150:  # Поддерживаем определенное количество падающих снежинок
        snowflakes.append(Snowflake())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
