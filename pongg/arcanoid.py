import pygame
import sys
import random
from mycolor import *

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
BALL_SIZE = 20
WHITE = (255, 255, 255)
RED=(255,0,0)
BLACK = (0, 0, 0)
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Один игрок")
clock = pygame.time.Clock()


player_x=10
player_y=550
x=10
y=player_y-10
dx=1
dy=-1
player_speed=3




# Главный игровой цикл
running = True


rect_x=10
rect_y=10
rect_width=50
rect_height=25
border_width=1


fields=[]

def ball_to_field_coords(ball_x, ball_y, rect_x, rect_y, rect_width, rect_height):
    """
    Преобразует координаты мяча в координаты ячейки поля.

    Параметры:
    ball_x, ball_y - координаты центра мяча
    rect_x, rect_y - координаты верхнего левого угла поля (нулевой ячейки)
    rect_width, rect_height - размер одной ячейки поля

    Возвращает:
    field_i, field_j - индексы ячейки в поле (столбец, строка)
    """
    # Вычисляем смещение от начала поля
    offset_x = ball_x - rect_x
    offset_y = ball_y - rect_y

    # Определяем номер ячейки (целочисленное деление)
    field_i = offset_x // rect_width
    field_j = offset_y // rect_height

    # Проверяем, попадает ли мяч в границы поля
    if 0 <= field_i < 11 and 0 <= field_j < 22:


# Создаем два слоя (Surface)
layer1 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Слой с альфа-каналом
layer2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Второй слой

# Прозрачность слоев (опционально)
layer1.set_alpha(255)  # Полностью непрозрачный
layer2.set_alpha(255)  # Немного прозрачный

def draw_filed():
    for j in range (22):
        for i in range(11):

            color=fields[j][i]
            # if color !=0:
            pygame.draw.rect(layer2, BLACK, (rect_x+rect_width*i, rect_y+rect_height*j, rect_width, rect_height), border_width)
            pygame.draw.rect(layer2, color_list[color], (rect_x-1+rect_width*i, rect_y-1+rect_height*j, rect_width-1, rect_height-1))
    #Обновление экрана

for j in range (22):
    field_rows=[]

    for i in range(11):

        if j>=15:
            color=0
        else:
            color=random.randint(0,len(color_list)-1)
        field_rows.append(color)
    fields.append(field_rows)

draw_filed()


font = pygame.font.Font(None, 36)
while running:

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        pygame.draw.rect(layer1, BLACK,(player_x,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))
        screen.blit(layer1, (0, 0))
        player_x -= player_speed
        pygame.draw.rect(layer1, WHITE,(player_x,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))
        screen.blit(layer1, (0, 0))
    if keys[pygame.K_RIGHT] and player_x < WIDTH-PADDLE_WIDTH:
        pygame.draw.rect(layer1, BLACK,(player_x,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))
        screen.blit(layer1, (0, 0))
        player_x += player_speed
        pygame.draw.rect(layer1, WHITE,(player_x,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))
        screen.blit(layer1, (0, 0))

    # Отрисовка
    screen.fill(BLACK)
        # Рисуем слои в правильном порядке (сначала нижний, потом верхний)
    #layer1.fill(BLACK)
    xx,yy=ball_to_field_coords(x, y, rect_x, rect_y, rect_width, rect_height)



    xx,yy=ball_to_field_coords(x, y, rect_x, rect_y, rect_width, rect_height)
    if xx is not None and yy is not None:  # Проверяем, что оба значения не None
        if fields[yy][xx]>0:
            fields[yy][xx]=0
            dy=-dy
            draw_filed()

    pygame.draw.rect(layer1, BLACK,(x,y,10,10))
    screen.blit(layer1, (0, 0))
    x=x+dx
    y=y+dy
    pygame.draw.rect(layer1, WHITE,(x,y,10,10))
    screen.blit(layer1, (0, 0))

    pygame.draw.rect(layer1, BLACK,(player_x,player_y,PADDLE_WIDTH,PADDLE_HEIGHT))
    pygame.draw.rect(layer1, WHITE,(player_x+1,player_y+1,PADDLE_WIDTH-1,PADDLE_HEIGHT-1))




    #pygame.draw.rect(layer1, WHITE,(x+1,y-1,9,9))
    if y>=player_y:
        if (x>=player_x and x<=player_x+PADDLE_WIDTH):
            dy=-dy
        else:
            x=random.randint(10,650)
            y=player_y-10
            dx=1
            dy=-1

    if x>=rect_width*11+10:
        dx=-dx
    if x<=0:
        dx=-dx
    if xx:
        if yy:
            score_text = font.render(f"Счет: {xx}:{yy}:[{fields[yy][xx]}]", True, WHITE)
            screen.blit(score_text, (650, 20))
    screen.blit(layer2, (0, 0))
    screen.blit(layer1, (0, 0))



    pygame.display.flip()


    clock.tick(FPS)

pygame.quit()
sys.exit()
