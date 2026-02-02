import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Домик с трубой, окном и дверью")

# Цвета
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
BROWN = (101, 67, 33)
RED = (220, 20, 60)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_BROWN = (51, 25, 0)

def полигон(*args)
  pygame.draw.line(*args)
# Функция для рисования домика
def draw_house():
    # Основание дома (фон)
    pygame.draw.rect(screen, BROWN, (250, 250, 300, 250))

    # Крыша (треугольник)
    pygame.draw.polygon(screen, RED, [(200, 250), (400, 150), (600, 250)])

    # Дверь
    pygame.draw.rect(screen, DARK_BROWN, (350, 350, 100, 150))
    pygame.draw.circle(screen, YELLOW, (430, 425), 8)  # ручка двери

    # Окно
    pygame.draw.rect(screen, WHITE, (280, 280, 100, 80))
    pygame.draw.rect(screen, BLACK, (280, 280, 100, 80), 2)  # рамка
    # Переплет окна
    pygame.draw.line(screen, BLACK, (330, 280), (330, 360), 2)
    pygame.draw.line(screen, BLACK, (280, 320), (380, 320), 2)

    # Труба
    pygame.draw.rect(screen, GRAY, (500, 150, 40, 80))
    pygame.draw.rect(screen, BLACK, (500, 150, 40, 80), 2)  # контур трубы

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Заполнение фона
    screen.fill(SKY_BLUE)

    # Трава
    pygame.draw.rect(screen, GREEN, (0, 500, WIDTH, 100))

    # Рисуем домик
    draw_house()

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
