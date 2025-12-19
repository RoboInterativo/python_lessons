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
RED=(255,0,0)
BLACK = (0, 0, 0)
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Один игрок")
clock = pygame.time.Clock()







# Главный игровой цикл
running = True
x=10
y=10
dx=5
dy=5
rect_x=10
rect_y=10
rect_width=50
rect_height=25
border_width=1

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

    # pygame.draw.rect(screen, WHITE,(x,y,10,10))
    for i in range(11):
        pygame.draw.rect(screen, RED,(rect_x+i*rect_width,rect_y,
        rect_width,rect_height) )
    #rect_x=10 начальная
    #Левый верхний угол прямоугольник (x,y)
    #Ширина и высота




    # Обновление экрана
    pygame.display.flip()
    x=x+dx
    y=y+dy

    clock.tick(FPS)

pygame.quit()
sys.exit()
