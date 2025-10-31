import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Упрощенная симуляция шариков")

BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

class Ball:
    def __init__(self):
        self.radius = random.randint(20, 40)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)

        speed = random.uniform(3, 6)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.color = random.choice(COLORS)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Отражение от стен
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.vx = -self.vx
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.vy = -self.vy

        # Ограничение в пределах экрана
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def check_collision(ball1, ball2):
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx * dx + dy * dy)

    if distance < ball1.radius + ball2.radius:
        # Просто меняем направления при столкновении
        ball1.vx, ball2.vx = ball2.vx, ball1.vx
        ball1.vy, ball2.vy = ball2.vy, ball1.vy

        # Разделяем шарики
        overlap = (ball1.radius + ball2.radius - distance) / 2
        angle = math.atan2(dy, dx)
        ball1.x -= overlap * math.cos(angle)
        ball1.y -= overlap * math.sin(angle)
        ball2.x += overlap * math.cos(angle)
        ball2.y += overlap * math.sin(angle)

balls = [Ball() for _ in range(8)]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for ball in balls:
        ball.move()
        ball.draw()

    # Проверка столкновений
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            check_collision(balls[i], balls[j])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
