

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки анимации
FRAME_WIDTH = 128
FRAME_HEIGHT = 128
COLUMNS = 6
ROWS = 4
TOTAL_FRAMES = COLUMNS * ROWS  # 24 кадра
ANIMATION_SPEED = 0.1  # Скорость смены кадров

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spritesheet_path, position):
        super().__init__()

        # Загружаем spritesheet
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

        # Создаем список для хранения всех кадров
        self.frames = []

        # Разрезаем spritesheet на отдельные кадры
        self.load_frames()

        # Настройки анимации
        self.current_frame = 0
        self.animation_speed = ANIMATION_SPEED
        self.animation_timer = 0

        # Устанавливаем начальное изображение и rect
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=position)

    def load_frames(self):
        """Разрезает spritesheet на отдельные кадры"""
        for row in range(ROWS):
            for col in range(COLUMNS):
                # Вычисляем координаты текущего кадра
                x = col * FRAME_WIDTH
                y = row * FRAME_HEIGHT

                # Создаем поверхность для кадра и копируем туда часть spritesheet
                frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)
                frame.blit(self.spritesheet, (0, 0), (x, y, FRAME_WIDTH, FRAME_HEIGHT))

                # Масштабируем если нужно (опционально)
                # frame = pygame.transform.scale(frame, (FRAME_WIDTH * 2, FRAME_HEIGHT * 2))

                self.frames.append(frame)

    def update(self, dt):
        """Обновляет анимацию"""
        # Увеличиваем таймер
        self.animation_timer += dt

        # Если прошло достаточно времени, меняем кадр
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0

            # Переходим к следующему кадру
            self.current_frame += 1

            # Если дошли до конца, возвращаемся к началу
            if self.current_frame >= TOTAL_FRAMES:
                self.current_frame = 0

            # Обновляем изображение
            self.image = self.frames[self.current_frame]

    def draw(self, surface):
        """Отрисовывает спрайт на поверхности"""
        surface.blit(self.image, self.rect)

def main():
    # Создаем окно
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Continuous Sprite Sheet Animation - 24 Frames")
    clock = pygame.time.Clock()

    # Создаем анимированный спрайт
    # ЗАМЕНИТЕ "spritesheet.png" на путь к вашему файлу
    #player = AnimatedSprite("./Turrets/Gun/Basic/basic_gun_shooting_animation.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    player = AnimatedSprite("./Turrets/Gun/Basic/basic_gun_shooting_animation.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Основной игровой цикл
    running = True
    while running:
        # Время, прошедшее с последнего кадра (в секундах)
        dt = clock.tick(FPS) / 250.0

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        player.update(dt)

        # Отрисовка
        screen.fill(BLACK)
        player.draw(screen)

        # Отладочная информация
        font = pygame.font.Font(None, 36)
        text = font.render(f"Frame: {player.current_frame + 1}/24", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
