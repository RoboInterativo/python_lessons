import pygame
import random
import math
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция упругих шариков")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 128, 0), (128, 0, 255), (0, 255, 128)
]

# Класс шарика
class Ball:
    def __init__(self, x=None, y=None, radius=None):
        self.radius = radius if radius else random.randint(15, 35)
        self.x = x if x else random.randint(self.radius, WIDTH - self.radius)
        self.y = y if y else random.randint(self.radius, HEIGHT - self.radius)

        # Случайная начальная скорость и направление
        speed = random.uniform(2, 5)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.color = random.choice(COLORS)
        self.mass = self.radius  # Масса пропорциональна радиусу

    def move(self):
        # Движение шарика
        self.x += self.vx
        self.y += self.vy

        # Отражение от стен
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx = -self.vx
        elif self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.vx = -self.vx

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy = -self.vy
        elif self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Рисуем обводку для лучшей видимости
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius, 2)

# Функция для проверки столкновений между шариками
def check_collision(ball1, ball2):
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx * dx + dy * dy)

    # Если шарики пересекаются
    if distance < ball1.radius + ball2.radius:
        # Вычисляем угол столкновения
        angle = math.atan2(dy, dx)

        # Вычисляем компоненты скорости в системе координат столкновения
        v1 = math.sqrt(ball1.vx * ball1.vx + ball1.vy * ball1.vy)
        v2 = math.sqrt(ball2.vx * ball2.vx + ball2.vy * ball2.vy)

        dir1 = math.atan2(ball1.vy, ball1.vx)
        dir2 = math.atan2(ball2.vy, ball2.vx)

        # Новые скорости после упругого столкновения
        new_vx1 = v2 * math.cos(dir2 - angle) * math.cos(angle) + v1 * math.sin(dir1 - angle) * math.cos(angle + math.pi/2)
        new_vy1 = v2 * math.cos(dir2 - angle) * math.sin(angle) + v1 * math.sin(dir1 - angle) * math.sin(angle + math.pi/2)

        new_vx2 = v1 * math.cos(dir1 - angle) * math.cos(angle) + v2 * math.sin(dir2 - angle) * math.cos(angle + math.pi/2)
        new_vy2 = v1 * math.cos(dir1 - angle) * math.sin(angle) + v2 * math.sin(dir2 - angle) * math.sin(angle + math.pi/2)

        # Устанавливаем новые скорости
        ball1.vx = new_vx1
        ball1.vy = new_vy1
        ball2.vx = new_vx2
        ball2.vy = new_vy2

        # Разделяем шарики, чтобы они не застревали друг в друге
        overlap = (ball1.radius + ball2.radius - distance) / 2
        ball1.x -= overlap * math.cos(angle)
        ball1.y -= overlap * math.sin(angle)
        ball2.x += overlap * math.cos(angle)
        ball2.y += overlap * math.sin(angle)

        return True
    return False

# Функция для проверки всех столкновений
def handle_all_collisions(balls):
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            check_collision(balls[i], balls[j])

# Создание шариков
balls = [Ball() for _ in range(10)]

# Основной цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Добавляем новый шарик при клике мыши
            if event.button == 1:  # Левая кнопка мыши
                balls.append(Ball(event.pos[0], event.pos[1]))
            elif event.button == 3:  # Правая кнопка мыши
                if balls:
                    balls.pop()

    # Обработка клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # Добавляем случайный шарик при нажатии пробела
        balls.append(Ball())
    if keys[pygame.K_c]:
        # Очищаем экран при нажатии C
        balls.clear()

    # Заполнение экрана
    screen.fill(BLACK)

    # Обновление и отрисовка шариков
    for ball in balls:
        ball.move()
        ball.draw()

    # Проверка столкновений
    handle_all_collisions(balls)

    # Отображение информации
    font = pygame.font.Font(None, 36)
    text = font.render(f"Шариков: {len(balls)}", True, WHITE)
    screen.blit(text, (10, 10))

    help_text = font.render("ЛКМ: добавить шарик | ПКМ: удалить | Пробел: случайный | C: очистить", True, WHITE)
    screen.blit(help_text, (10, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
