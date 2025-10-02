import curses

def main(stdscr):
    # Initialize colors (optional)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Clear screen and set up initial display
    stdscr.clear()
    menuitems=[
    "Показать все задачи",
    "Добавить задачу",
    "Обновить статус задачи",
    "Удалить задачу",
    "Поиcк задач",
    "Выход"


    ]
    stdscr.addstr(0, 0, "Main Menu", curses.A_BOLD)
    for i, item in enumerate(menuitems):

        stdscr.addstr(i+2, 0, f"{i}. {item}" )

    stdscr.refresh()

    current_row = 2 # Start at the first option
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 2:
            # Deselect current
            stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
            current_row -= 1
            # Select new
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
            stdscr.attroff(curses.color_pair(1))
        elif key == curses.KEY_DOWN and current_row < len(menuitems)+1:
            # Deselect current
            stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
            current_row += 1
            # Select new
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(current_row, 0, f"{current_row-1}. {menuitems[current_row-2]}")
            stdscr.attroff(curses.color_pair(1))
        elif key == ord('\n'): # Enter key
            if current_row == 2:
                stdscr.addstr(6, 0, "You selected Option One!")
            elif current_row == 3:
                stdscr.addstr(6, 0, "You selected Option Two!")
            elif current_row == 7:
                break # Exit the loop
            stdscr.refresh()
            stdscr.getch() # Wait for another key press

        stdscr.refresh()

curses.wrapper(main)
