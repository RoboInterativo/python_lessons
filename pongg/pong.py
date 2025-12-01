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

    pygame.draw.rect(screen, WHITE, (0, 0, 100, 200))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
