import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Расстояние между шариками")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        # Рисуем центр
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), 3)

def draw_distance_line(surface, ball1, ball2):
    """Рисует линию между центрами шариков и показывает расстояние"""
    # Линия между центрами
    pygame.draw.line(surface, BLACK, (ball1.x, ball1.y), (ball2.x, ball2.y), 2)

    # Вычисляем расстояние
    distance = math.sqrt((ball2.x - ball1.x)**2 + (ball2.y - ball1.y)**2)

    # Текст с расстоянием
    font = pygame.font.Font(None, 24)
    mid_x = (ball1.x + ball2.x) / 2
    mid_y = (ball1.y + ball2.y) / 2
    text = font.render(f"{distance:.1f}", True, BLACK)
    text_rect = text.get_rect(center=(mid_x, mid_y - 15))
    screen.blit(text, text_rect)

    return distance

# Создаем шарики
ball1 = Ball(150, 200, 30, RED)
ball2 = Ball(450, 200, 25, BLUE)

clock = pygame.time.Clock()
dragging = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем, кликнули ли на шарик
            mouse_x, mouse_y = event.pos
            dist_to_ball1 = math.sqrt((mouse_x - ball1.x)**2 + (mouse_y - ball1.y)**2)
            dist_to_ball2 = math.sqrt((mouse_x - ball2.x)**2 + (mouse_y - ball2.y)**2)

            if dist_to_ball1 <= ball1.radius:
                dragging = ball1
            elif dist_to_ball2 <= ball2.radius:
                dragging = ball2

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

        elif event.type == pygame.MOUSEMOTION and dragging:
            # Перемещаем шарик
            dragging.x, dragging.y = event.pos

    # Отрисовка
    screen.fill(WHITE)

    # Рисуем расстояние
    distance = draw_distance_line(screen, ball1, ball2)

    # Проверяем столкновение и меняем цвет
    if distance < ball1.radius + ball2.radius:
        collision_color = GREEN
    else:
        collision_color = RED

    # Рисуем сумму радиусов для сравнения
    sum_radius_text = f"Сумма радиусов: {ball1.radius + ball2.radius}"
    font = pygame.font.Font(None, 36)
    text = font.render(sum_radius_text, True, BLACK)
    screen.blit(text, (10, 10))

    # Информация о столкновении
    collision_text = f"Столкновение: {'ДА' if distance < ball1.radius + ball2.radius else 'НЕТ'}"
    text2 = font.render(collision_text, True, collision_color)
    screen.blit(text2, (10, 50))

    # Рисуем шарики
    ball1.draw(screen)
    ball2.draw(screen)

    pygame.display.flip()
    clock.tick(60)
