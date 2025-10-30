import pygame
import sys
import math

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
TOTAL_FRAMES = COLUMNS * ROWS
ANIMATION_SPEED = 0.1
ROTATION_SPEED = 1  # градусов в кадр

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spritesheet_path, position):
        super().__init__()

        # Загружаем spritesheet
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

        # Создаем список для хранения всех кадров
        self.frames = []
        self.load_frames()

        # Настройки анимации
        self.current_frame = 0
        self.animation_speed = ANIMATION_SPEED
        self.animation_timer = 0

        # Настройки вращения
        self.angle = 0
        self.rotation_speed = ROTATION_SPEED

        # Устанавливаем начальное изображение и rect
        self.original_image = self.frames[0]
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)

    def load_frames(self):
        """Разрезает spritesheet на отдельные кадры"""
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = col * FRAME_WIDTH
                y = row * FRAME_HEIGHT
                frame = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)
                frame.blit(self.spritesheet, (0, 0), (x, y, FRAME_WIDTH, FRAME_HEIGHT))
                self.frames.append(frame)

    def update(self, dt):
        """Обновляет анимацию и вращение"""
        # Обновляем анимацию
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % TOTAL_FRAMES
            self.original_image = self.frames[self.current_frame]

        # Обновляем вращение
        self.angle = (self.angle + self.rotation_speed) % 360

        # Применяем вращение к текущему кадру
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=old_center)

    def draw(self, surface):
        """Отрисовывает спрайт на поверхности"""
        surface.blit(self.image, self.rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Animated Sprite with Rotation")
    clock = pygame.time.Clock()

    player = AnimatedSprite("./Turrets/Gun/Basic/basic_gun_shooting_animation.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    running = True
    while running:
        dt = clock.tick(FPS) / 250.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Переключение вращения по нажатию R
                    player.rotation_speed = 0 if player.rotation_speed != 0 else ROTATION_SPEED
                elif event.key == pygame.K_LEFT:
                    player.rotation_speed = abs(player.rotation_speed)  # По часовой
                elif event.key == pygame.K_RIGHT:
                    player.rotation_speed = -abs(player.rotation_speed)  # Против часовой

        player.update(dt)
        screen.fill(BLACK)
        player.draw(screen)

        # Отладочная информация
        font = pygame.font.Font(None, 36)
        frame_text = font.render(f"Frame: {player.current_frame + 1}/24", True, WHITE)
        rotation_text = font.render(f"Rotation: {int(player.angle)}°", True, WHITE)
        help_text = font.render("R: toggle rotation, ←→: change direction", True, WHITE)

        screen.blit(frame_text, (10, 10))
        screen.blit(rotation_text, (10, 50))
        screen.blit(help_text, (10, 90))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
