import pygame
import sys
import random

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()
FPS=60

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Квадрат в Pygame")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


# Параметры квадрата
square_size = 30
x=100
y=100
dx=10
dy=10
# Главный цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование квадрата
    pygame.draw.rect(screen, WHITE, (x, y, square_size, square_size))
        # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)
    #pygame.draw.rect(screen, BLACK, (x, y, square_size, square_size))
    if (x+dx>=WIDTH):
        #dx=random.randint(5,15)
        dx=-dx
    if (y+dy>=HEIGHT):
        #dy=random.randint(5,15)
        dy=-dy
    if (x+dx<=0):
        #dx=random.randint(5,15)
        dx=-dx
    if (y+dy<=0):
        #dx=random.randint(5,15)
        dy=-dy
    x=x+dx
    y=y+dy
    pygame.draw.rect(screen, WHITE, (x, y, square_size, square_size))






# Завершение работы
pygame.quit()
sys.exit()
