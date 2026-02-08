import pygame
import sys
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
BROWN = (101, 67, 33)
RED = (220, 20, 60)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_BROWN = (51, 25, 0)

ГОЛУБОЙ = (135, 206, 235)
ЗЕЛЕНЫЙ = (34, 139, 34)
КОРИЧНЕВЫЙ = (101, 67, 33)
КРАСНЫЙ = (220, 20, 60)
ЖЕЛТЫЙ = (255, 255, 0)
ЧЕРНЫЙ = (0, 0, 0)
БЕЛЫЙ = (255, 255, 255)
СЕРЫЙ = (128, 128, 128)
ТЕМНО_КОРИЧНЕВЫЙ = (51, 25, 0)
# Дополнительные цвета для полноты палитры
ФИОЛЕТОВЫЙ = (138, 43, 226)      # Дополнительный к желтому
ОРАНЖЕВЫЙ = (255, 165, 0)         # Между желтым и красным
РОЗОВЫЙ = (255, 192, 203)         # Светлый оттенок
ТЕМНО_СИНИЙ = (0, 0, 139)         # Контрастный к светлым цветам
СВЕТЛО_ЗЕЛЕНЫЙ = (144, 238, 144)  # Светлый зеленый
СИНИЙ = (0, 0, 255)               # Основной синий
ТЕМНО_ЗЕЛЕНЫЙ = (0, 100, 0)       # Темный зеленый
БИРЮЗОВЫЙ = (64, 224, 208)        # Между синим и зеленым


def полигон(*args):
  pygame.draw.polygon(*args)

def круг(*args):
    pygame.draw.circle(*args)  # ручка двери

def прямоугольник(*args):
    pygame.draw.rect(*args)
def линия(*args):
    pygame.draw.line(*args)

def дуга(*args):
    pygame.draw.arc(*args)

def элипс(*args):
    pygame.draw.elipse(*args)



class Игра:
    def __init__(self):
        self.ШИРИНА, self.ВЫСОТА = 800, 600
        self.экран = pygame.display.set_mode((self.ШИРИНА, self.ВЫСОТА))
    def игровой_цикл(self):
        pass

    def клавиши(self):
        pass
    def столкновения(self):
        pass
    def заливка(self,цвет):
        self.экран.fill(цвет)
    def перед_игрой(self):
        pass
    def запуск(self):
        pygame.init()
        running=True
        clock = pygame.time.Clock()
        self.перед_игрой()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    self.клавиши()

            self.игровой_цикл()
            pygame.display.flip()
            self.столкновения()
            clock.tick(60)

        pygame.quit()
        sys.exit()
