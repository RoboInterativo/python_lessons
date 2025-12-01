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

# Параметры игрока
player_x = 50
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
player_speed = 7

# Параметры мяча
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Счет
score = 0
font = pygame.font.Font(None, 36)

def reset_ball():
    """Сброс мяча в центр"""
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 5 * random.choice((1, -1))
    ball_speed_y = 5 * random.choice((1, -1))

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

    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отскок от верхней и нижней стенки
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Отскок от левой стенки (игрок проиграл)
    if ball_x <= 0:
        reset_ball()
        score = max(0, score - 1)  # Не даем счету уйти в минус

    # Отскок от правой стенки
    if ball_x >= WIDTH - BALL_SIZE:
        ball_speed_x = -ball_speed_x

    # Столкновение с ракеткой игрока
    if (ball_x <= player_x + PADDLE_WIDTH and
        ball_y + BALL_SIZE >= player_y and
        ball_y <= player_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x
        score += 1
        # Немного меняем угол отскока для разнообразия
        ball_speed_y += random.uniform(-1, 1)

    # Отрисовка
    screen.fill(BLACK)

    # Рисуем игрока
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Рисуем мяч (квадрат)
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Рисуем счет
    score_text = font.render(f"Счет: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
