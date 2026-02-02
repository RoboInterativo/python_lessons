import pygame
import random

# Цвета шариков
RED = (255, 0, 0)
ORANGE = (0xFF, 0x7F, 0)
YELLOW = (0xFF, 0xFF, 0)  # Исправлен желтый цвет (было 0x7F)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
D_BLUE = (75, 0, 130)
PURPLE = (148, 0, 210)

mycolors = [RED, ORANGE, YELLOW, GREEN, BLUE, D_BLUE, PURPLE]

# Цвета фона
GRAY = (0xb3, 0xb3, 0xb3)
WHITE = (0xFF, 0xFF, 0xFF)
TEXTCOLOR = (0, 0, 0)
(width, height) = (800, 600)

running = True

# Направления для проверки линий: (dx, dy)
DIRECTIONS = [
    (1, 0),   # горизонталь вправо
    (0, 1),   # вертикаль вниз
    (1, 1),   # диагональ вправо-вниз
    (1, -1)   # диагональ вправо-вверх
]

def draw_circle(x, y, color, hide):
    """Рисует шарик или пустую клетку"""
    if hide:
        pygame.draw.circle(screen, GRAY, (125 + 50 * x, 125 + 50 * y), 21)
    else:
        pygame.draw.circle(screen, TEXTCOLOR, (125 + 50 * x, 125 + 50 * y), 21)
        pygame.draw.circle(screen, color, (125 + 50 * x, 125 + 50 * y), 20)

def check_and_remove_lines():
    """
    Проверяет все линии на поле и удаляет те, где 5+ шариков одного цвета.
    Возвращает количество удаленных шариков.
    """
    to_remove = []  # Список координат шариков для удаления

    # Проходим по всем клеткам поля
    for y in range(9):
        for x in range(9):
            color = pole[y][x]
            if color < 0:  # Пустая клетка
                continue

            # Проверяем все направления из текущей клетки
            for dx, dy in DIRECTIONS:
                line_length = 1  # Текущий шарик уже первый
                line_cells = [(x, y)]  # Координаты шариков в линии

                # Проверяем в одну сторону
                nx, ny = x + dx, y + dy
                while 0 <= nx < 9 and 0 <= ny < 9 and pole[ny][nx] == color:
                    line_length += 1
                    line_cells.append((nx, ny))
                    nx += dx
                    ny += dy

                # Проверяем в противоположную сторону
                nx, ny = x - dx, y - dy
                while 0 <= nx < 9 and 0 <= ny < 9 and pole[ny][nx] == color:
                    line_length += 1
                    line_cells.append((nx, ny))
                    nx -= dx
                    ny -= dy

                # Если линия длиной 5 или больше
                if line_length >= 5:
                    to_remove.extend(line_cells)

    # Удаляем дубликаты (шарик может быть в нескольких линиях одновременно)
    to_remove = list(set(to_remove))

    # Удаляем найденные шарики с поля
    for x, y in to_remove:
        pole[y][x] = -1
        draw_circle(x, y, GRAY, True)

    return len(to_remove)

def add_new_balls(count=3):
    """Добавляет новые шарики в случайные пустые клетки"""
    balls_added = 0
    attempts = 0
    max_attempts = 100  # Чтобы избежать бесконечного цикла

    while balls_added < count and attempts < max_attempts:
        x = random.randint(0, 8)
        y = random.randint(0, 8)

        if pole[y][x] < 0:  # Клетка пустая
            color = random.randint(0, 6)
            pole[y][x] = color
            draw_circle(x, y, mycolors[color], False)
            balls_added += 1

        attempts += 1

    return balls_added

# Игровое поле: -1 = пусто, 0-6 = цвет шарика
pole = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
]

def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lines 98")
    screen.fill(TEXTCOLOR)

    # Рисуем игровое поле
    pygame.draw.rect(screen, GRAY, (100, 100, 450, 450))
    for i in range(9):
        # Горизонтальные линии
        pygame.draw.line(screen, TEXTCOLOR, [100, 100 + 50 * i], [550, 100 + 50 * i], 1)
        pygame.draw.line(screen, WHITE, [101, 100 + 50 * i + 1], [550, 100 + 50 * i + 1], 1)
        # Вертикальные линии
        pygame.draw.line(screen, TEXTCOLOR, [100 + 50 * i, 100], [100 + 50 * i, 550], 1)
        pygame.draw.line(screen, WHITE, [100 + 50 * i + 1, 101], [100 + 50 * i + 1, 550], 1)

    # Добавляем начальные шарики (5 штук, как в оригинале)
    initial_balls = 5
    balls_added = 0
    while balls_added < initial_balls:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if pole[y][x] < 0:  # Клетка пустая
            color = random.randint(0, 6)
            pole[y][x] = color
            draw_circle(x, y, mycolors[color], False)
            balls_added += 1

    pygame.display.update()

    # Переменные для выбора шарика
    selected = False
    selected_coord = (0, 0)
    selected_color = -1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = get_coord(pos)

                if selected:
                    # Если шарик уже выбран, пытаемся переместить
                    if 0 <= x < 9 and 0 <= y < 9:
                        if pole[y][x] < 0:  # Клетка пустая
                            # Убираем старый шарик
                            xs, ys = selected_coord
                            pole[ys][xs] = -1
                            draw_circle(xs, ys, GRAY, True)

                            # Ставим на новое место
                            pole[y][x] = selected_color
                            draw_circle(x, y, mycolors[selected_color], False)

                            # Снимаем выделение
                            selected = False

                            # Проверяем линии после перемещения
                            removed = check_and_remove_lines()

                            # Добавляем новые шарики только если ничего не удалили
                            if removed == 0:
                                add_new_balls(3)

                            # После добавления новых шариков снова проверяем линии
                            check_and_remove_lines()

                            pygame.display.update()

                else:
                    # Выбираем шарик для перемещения
                    if 0 <= x < 9 and 0 <= y < 9:
                        selected_color = pole[y][x]
                        if selected_color >= 0:  # Клетка не пустая
                            selected = True
                            selected_coord = (x, y)

        pygame.display.update()

def get_coord(pos):
    """Преобразует координаты мыши в координаты клетки"""
    x = (pos[0] - 100) // 50
    y = (pos[1] - 100) // 50
    return x, y

if __name__ == '__main__':
    main()
