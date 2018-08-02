import fallen
import random
import figure
import pygame
from constant import GAME_PERIOD, SHIFT_PERIOD, BEFORE_SHIFT_PERIOD
from constant import GAME_PERIOD_EVENT, SHIFT_EVENT, BEFORE_SHIFT_EVENT, GAME_OVER_EVENT

figures = {'I', 'S', 'Z', 'O', 'L', 'J', 'T'}
colors = {'red', 'green', 'blue', 'black', 'white'}


def f(p):
    for i in range(10):
        for j in range(20):
            if p[i][j]:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()


class Logic:

    def __init__(self):
        self._field = [[False for _ in range(20)] for _ in range(10)]
        self._figure = None
        self._prompt = None
        self._fallen = fallen.Fallen()

        self._period = GAME_PERIOD[0]
        pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)

        self._active_pressed = None  # "L", "R", "U", "D"

        self._score = 0

    def start(self):
        self._prompt = self._create_figure()
        self._figure = self._create_figure()
        pos = self._start_position(self._figure)
        self._figure.move(self._figure.get_turn(), pos[0], pos[1])

    def render(self, display_surf):
        if self._figure is not None:
            self._figure.draw(display_surf)
        if self._prompt is not None:
            self._prompt.draw(display_surf)
        if self._fallen is not None:
            self._fallen.draw(display_surf)

    def period(self):
        if self._figure is None:
            return
        is_space = True
        for coord in self._figure.get_coord():
            if coord[1] == 19 or self._field[coord[0]][coord[1]+1]:
                is_space = False
                break
        if is_space:
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0], pos[1]+1)
        else:
            for coord in self._figure.get_coord():
                self._field[coord[0]][coord[1]] = True
            for block in self._figure.sprites():
                block.remove(self._figure)
                self._fallen.add(block)
            self.destroy_lines()
            self._figure = self._prompt
            pos = self._start_position(self._figure)
            if pos is None:
                self.game_over()
                return
            self._figure.move(self._figure.get_turn(), pos[0], pos[1])
            self._prompt = self._create_figure()

    def key_down(self, key):
        if self._figure is None:
            return
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, BEFORE_SHIFT_PERIOD)
        pygame.time.set_timer(SHIFT_EVENT, 0)
        if key == pygame.K_LEFT:
            self._active_pressed = "L"
            for coord in self._figure.get_coord():
                if coord[0] == 0 or self._field[coord[0]-1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]-1, pos[1])
        elif key == pygame.K_RIGHT:
            self._active_pressed = "R"
            for coord in self._figure.get_coord():
                if coord[0] == 9 or self._field[coord[0]+1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]+1, pos[1])
        elif key == pygame.K_DOWN:
            self._active_pressed = "D"
            self.period()
            pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)
        elif key == pygame.K_UP:
            self._active_pressed = "U"
            self.turning()

    def key_up(self, key):
        if self._figure is None:
            return
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, 0)
        pygame.time.set_timer(SHIFT_EVENT, 0)
        if key == pygame.K_LEFT:
            if self._active_pressed == "L":
                self._active_pressed = None
        elif key == pygame.K_RIGHT:
            if self._active_pressed == "R":
                self._active_pressed = None
        elif key == pygame.K_DOWN:
            if self._active_pressed == "D":
                self._active_pressed = None
        elif key == pygame.K_UP:
            if self._active_pressed == "U":
                self._active_pressed = None

    def begin_shift(self):
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, 0)
        pygame.time.set_timer(SHIFT_EVENT, SHIFT_PERIOD)

    def shift(self):
        if self._figure is None:
            return

        if self._active_pressed == "L":
            for coord in self._figure.get_coord():
                if coord[0] == 0 or self._field[coord[0]-1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]-1, pos[1])

        elif self._active_pressed == "R":
            for coord in self._figure.get_coord():
                if coord[0] == 9 or self._field[coord[0]+1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]+1, pos[1])

        elif self._active_pressed == "D":
            self.period()
            pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)

    def turning(self):
        if self._figure is None:
            return

        _figure = self._figure.get_figure()
        _turn = self._figure.get_turn()
        _pos = self._figure.get_main_coord()
        a = _pos[0]
        b = _pos[1]

        if _figure == "O":
            return
        if _figure == "I":
            if _turn % 2 == 0:
                if a == 9 or a < 2 or self._field[a-2][b+1] or self._field[a-1][b+1] or self._field[a+1][b+1]:
                    return
                self._figure.move(1, a-2, b+1)
            else:
                if b == 0 or b > 17 or self._field[a+2][b-1] or self._field[a+2][b+1] or self._field[a+2][b+2]:
                    return
                self._figure.move(0, a+2, b-1)

        if _figure == "T":
            if _turn % 4 == 0:
                if b > 17 or self._field[a+2][b+1] or self._field[a+2][b+2]:
                    return
                self._figure.move(1, a+1, b)
            elif _turn % 4 == 1:
                if a == 0 or self._field[a-1][b+2] or self._field[a][b+2]:
                    return
                self._figure.move(2, a-1, b+1)
            elif _turn % 4 == 2:
                if b == 0 or self._field[a][b] or self._field[a][b-1]:
                    return
                self._figure.move(3, a, b-1)
            else:
                if a > 7 or self._field[a+1][b] or self._field[a+2][b]:
                    return
                self._figure.move(0, a, b)

        if _figure == "S":
            if _turn % 2 == 0:
                if b == 0 or self._field[a+1][b-1] or self._field[a+2][b+1]:
                    return
                self._figure.move(1, a+1, b-1)
            else:
                if a == 0 or self._field[a-1][b+2] or self._field[a][b+2]:
                    return
                self._figure.move(0, a-1, b+1)
        if _figure == "Z":
            if _turn % 2 == 0:
                if b == 0 or self._field[a][b+1] or self._field[a+1][b-1]:
                    return
                self._figure.move(1, a, b-1)
            else:
                if a == 8 or self._field[a+1][b+2] or self._field[a+2][b+2]:
                    return
                self._figure.move(0, a, b+1)
        if _figure == "J":
            if _turn % 4 == 0:
                if a == 8 or self._field[a][b+1] or self._field[a+2][b+2]:
                    return
                self._figure.move(1, a, b+1)
            elif _turn % 4 == 1:
                if b == 0 or self._field[a][b-1] or self._field[a+1][b-1]:
                    return
                self._figure.move(2, a, b-1)
            elif _turn % 4 == 2:
                if a == 8 or self._field[a+1][b+1] or self._field[a+2][b+1] or self._field[a+2][b+2]:
                    return
                self._figure.move(3, a, b+1)
            else:
                if b == 0 or self._field[a][b+1] or self._field[a+1][b+1] or self._field[a+1][b-1]:
                    return
                self._figure.move(0, a, b - 1)
        if _figure == "L":
            if _turn % 4 == 0:
                if a == 8 or self._field[a+1][b+1] or self._field[a+2][b+1]:
                    return
                self._figure.move(1, a, b+1)
            elif _turn % 4 == 1:
                if b == 0 or self._field[a][b-1] or self._field[a+1][b-1] or self._field[a+1][b+1]:
                    return
                self._figure.move(2, a, b - 1)
            elif _turn % 4 == 2:
                if a == 8 or self._field[a][b+2] or self._field[a+2][b+1] or self._field[a+2][b+2]:
                    return
                self._figure.move(3, a, b+1)
            else:
                if b == 0 or self._field[a][b] or self._field[a][b-1]:
                    return
                self._figure.move(0, a, b-1)

    def game_over(self):
        pygame.time.set_timer(GAME_PERIOD_EVENT, 0)
        pygame.time.set_timer(SHIFT_EVENT, 0)
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, 0)
        self._figure = None
        pygame.event.post(pygame.event.Event(GAME_OVER_EVENT, dict()))

    def destroy_lines(self):
        i = 19
        while i >= 0:
            is_line = True
            for j in range(10):
                if not self._field[j][i]:
                    is_line = False
                    break
            if not is_line:
                i -= 1
                continue
            else:
                self._score += 1
                if self._score % 10 == 0 and self._period != GAME_PERIOD[len(GAME_PERIOD)-1]:
                    self._period = GAME_PERIOD[self._score // 10]
                for j in range(i, 0, -1):
                    for k in range(10):
                        self._field[k][j] = self._field[k][j-1]
                self._fallen.destroy_line(i)

    def get_score(self):
        return self._score

    def _create_figure(self):
        _figure = random.choice(list(figures))
        turn = random.randint(1, 4)
        color = random.choice(list(colors))
        return figure.Figure(color, _figure, turn)

    def _start_position(self, _figure):
        _type = _figure.get_figure()
        turn = _figure.get_turn()
        if _type == "I" and turn % 2 == 1:
            pos_list = [i for i in range(0, 6+1)]
        elif ((_type == "L" or _type == "J") and (turn % 4 == 1 or turn % 4 == 3) or
              (_type == "S" or _type == "Z") and turn % 2 == 0 or
              _type == "T" and (turn % 4 == 0 or turn % 4 == 2)):
            pos_list = [i for i in range(0, 7+1)]
        elif _type == "I" and turn % 2 == 0:
            pos_list = [i for i in range(0, 9+1)]
        else:
            pos_list = [i for i in range(0, 8+1)]
        figure_pos = _figure.get_coord()
        while True:
            start_pos = random.choice(pos_list)
            is_empty = True
            for i in figure_pos:
                if self._field[i[0]+start_pos][i[1]]:
                    pos_list.remove(start_pos)
                    if not pos_list:
                        return None
                    is_empty = False
                    break
            if is_empty:
                return start_pos, 0
