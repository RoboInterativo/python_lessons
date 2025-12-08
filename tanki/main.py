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
FPS = 25

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Один игрок")
clock = pygame.time.Clock()



assets_image = pygame.image.load('assets.png')
frame1 = pygame.Surface((16, 16))
frame2 = pygame.Surface((16, 16))
card_rect=(0,0,15,15)
frame1.blit(assets_image, (0, 0), card_rect)
card_rect=(0+16,0,15+16,15)
frame2.blit(assets_image, (0, 0), card_rect)
frames=[frame1,frame2]
index=0
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

    # pygame.draw.rect(screen, WHITE, (0, 0, 100, 200))

    # Обновление экрана
    scaled_image = pygame.transform.scale(frames[index], (64,64))
    screen.blit(scaled_image,(0,0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
    if index==0:
        index=1
    else:
        index=0

pygame.quit()
sys.exit()
