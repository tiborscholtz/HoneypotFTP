import curses
from math import floor
from constants import CURSES_OPTIONS


class Screen:
    def __init__(self):
        self._current_page = "c"
        self._options = CURSES_OPTIONS
        pass


    def get_current_page(self):
        return self._current_page
    
    def is_current_page(self,_check_page):
        return self._current_page == _check_page

    def change_current_page(self,_new_page):
        for option in self._options:
            if option["key"] == _new_page:
                self._current_page = option["key"]
                break
        pass

    def print_curses_options(self,stdscr,current_page):
        maxy, maxx = stdscr.getmaxyx()
        text_length = 0
        for c_o in self._options:
            text_length += len("("+c_o["key"]+"):")
            text_length += len(c_o["text"])

        starting_x = floor((maxx / 2) - (text_length / 2))
        for c_o in self._options:
            current_option = "("+c_o["key"]+"):"
            current_option_length = len(current_option)
            color = curses.color_pair(12) if (current_page == c_o["key"]) else curses.color_pair(6)
            stdscr.addstr((maxy-1), starting_x, current_option, color)
            starting_x += (current_option_length + 1)
            current_text = c_o["text"]
            current_text_length = len(current_text)
            stdscr.addstr((maxy-1), starting_x, current_text, curses.color_pair(16))
            starting_x += (current_text_length + 1)
        pass

    def print_table(self,stdscr,col_widths,columns,data,starting_x,starting_y):
        start_x, start_y = starting_x, starting_y  # Starting position
        def draw_cell(y, x, text, width):
            stdscr.addch(y, x, '|')
            stdscr.addstr(y, x + 1, text.ljust(width - 1))  # Text with padding
        y = start_y
        x = start_x
        for i, header in enumerate(columns):
            draw_cell(y, x, header, col_widths[i])
            x += col_widths[i]
        stdscr.addch(y, x, '|')
        y += 1
        x = start_x
        stdscr.addch(y, x, '+')
        for width in col_widths:
            stdscr.addstr(y, x + 1, '-' * (width - 1))
            x += width
            stdscr.addch(y, x, '+')
        for row in data:
            y += 1
            x = start_x
            for i, cell in enumerate(row):
                draw_cell(y, x, str(cell), col_widths[i])
                x += col_widths[i]
            stdscr.addch(y, x, '|')