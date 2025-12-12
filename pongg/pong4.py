import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Один игрок")
clock = pygame.time.Clock()


dx=5
dy=5
x=10
y=10




# Главный игровой цикл
running = True
while running:

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - PADDLE_HEIGHT:
        player_y += player_speed

    # Отрисовка
    screen.fill(BLACK)

    # pygame.draw.rect(screen, WHITE,(10,10,30,110))
    pygame.draw.rect(screen, WHITE,(x,y,20,20))

    # Обновление экрана
    pygame.display.flip()
    x=x+dx
    y=y+dy
    if (x>=WIDTH or  x<=0):
        dx=-dx
    elif (y>=HEIGHT or  y<=0) :
        dy=-dy
    clock.tick(FPS)

pygame.quit()
sys.exit()
