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



player_y = 10




# Главный игровой цикл
running = True
x=10
y=10
dx=5
dy=5
player_speed=5
score=0
font = pygame.font.Font(None, 36)
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

    pygame.draw.rect(screen, WHITE,(x,y,10,10))

    pygame.draw.rect(screen, WHITE,(750,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))

    # Рисуем счет
    score_text = font.render(f"Счет: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))


    # Обновление экрана
    pygame.display.flip()
    x=x+dx
    y=y+dy

    if x>=WIDTH:
        x=30
        y=random.randint(10,500)
        dx=5
        dy=5
        score=score+1
    if x>=750:
        if (x <= 750 + PADDLE_WIDTH and
            y + 10 >= player_y and
            y <= player_y + PADDLE_HEIGHT):
            dx = -dx
        #score += 1
        # Немного меняем угол отскока для разнообразия
        #dy = random.choice([-5, 5])
    if (  x<=0):
            dx=-dx
    elif (y>=HEIGHT or  y<=0) :
            dy=-dy
    clock.tick(FPS)

    clock.tick(FPS)

pygame.quit()
sys.exit()
