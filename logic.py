import fallen
import random
import figure
import pygame
from constant import GAME_PERIOD, SHIFT_PERIOD, BEFORE_SHIFT_PERIOD
from constant import GAME_PERIOD_EVENT, SHIFT_EVENT, BEFORE_SHIFT_EVENT

figures = {'I', 'S', 'Z', 'O', 'L', 'J', 'T'}
colors = {'red', 'green', 'blue', 'black', 'white'}


class Logic:

    def __init__(self):
        self._field = [[False for _ in range(20)] for _ in range(10)]
        self._figure = None
        self._prompt = None
        self._fallen = fallen.Fallen()

        self._period = GAME_PERIOD[0]
        pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)

        self._left_pressed = False
        self._right_pressed = False
        self._down_pressed = False
        self._up_pressed = False

    def start(self):
        self._prompt = self._create_figure()
        self._figure = self._create_figure()
        pos = self._start_position(self._figure.get_figure(), self._figure.get_turn())
        self._figure.move(self._figure.get_turn(), pos[0], pos[1])

    def render(self, display_surf):
        if self._figure is not None:
            self._figure.draw(display_surf)
        if self._prompt is not None:
            self._prompt.draw(display_surf)
        if self._fallen is not None:
            self._fallen.draw(display_surf)

    def period(self):
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
                block.add(self._fallen)
            self._figure = self._prompt
            pos = self._start_position(self._figure.get_figure(), self._figure.get_turn())
            self._figure.move(self._figure.get_turn(), pos[0], pos[1])
            self._prompt = self._create_figure()

    def key_down(self, key):
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, BEFORE_SHIFT_PERIOD)
        if key == pygame.K_LEFT:
            self._left_pressed = True
            for coord in self._figure.get_coord():
                if coord[0] == 0 or self._field[coord[0]-1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]-1, pos[1])
        elif key == pygame.K_RIGHT:
            self._right_pressed = True
            for coord in self._figure.get_coord():
                if coord[0] == 9 or self._field[coord[0]+1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]+1, pos[1])
        elif key == pygame.K_DOWN:
            self._down_pressed = True
            self.period()
            pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)
        elif key == pygame.K_UP:
            self._up_pressed = True
            self.turning()

    def key_up(self, key):
        pygame.time.set_timer(BEFORE_SHIFT_EVENT, 0)
        pygame.time.set_timer(SHIFT_EVENT, 0)
        if key == pygame.K_LEFT:
            self._left_pressed = False
        elif key == pygame.K_RIGHT:
            self._right_pressed = False
        elif key == pygame.K_DOWN:
            self._down_pressed = False
        elif key == pygame.K_UP:
            self._up_pressed = False

    def begin_shift(self):
        if not self._is_only_one_key_pressed():
            return

        pygame.time.set_timer(BEFORE_SHIFT_EVENT, 0)
        pygame.time.set_timer(SHIFT_EVENT, SHIFT_PERIOD)

    def shift(self):
        if not self._is_only_one_key_pressed():
            return

        if self._left_pressed:
            for coord in self._figure.get_coord():
                if coord[0] == 0 or self._field[coord[0]-1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]-1, pos[1])

        elif self._right_pressed:
            for coord in self._figure.get_coord():
                if coord[0] == 9 or self._field[coord[0]+1][coord[1]]:
                    return
            pos = self._figure.get_main_coord()
            self._figure.move(self._figure.get_turn(), pos[0]+1, pos[1])

        elif self._down_pressed:
            self.period()
            pygame.time.set_timer(GAME_PERIOD_EVENT, self._period)

    def turning(self):
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


    def _create_figure(self):
        _figure = random.choice(list(figures))
        turn = random.randint(1, 4)
        color = random.choice(list(colors))
        return figure.Figure(color, _figure, turn)

    def _start_position(self, _figure, turn):
        if _figure == "I" and turn % 2 == 1:
            return random.randint(0, 6), 0
            return 6, 0
        elif ((_figure == "L" or _figure == "J") and (turn % 4 == 1 or turn % 4 == 3) or
            (_figure == "S" or _figure == "Z") and turn % 2 == 0 or
            _figure == "T" and (turn % 4 == 0 or turn % 4 == 2)):
            return random.randint(0, 7), 0
            return 7, 0
        elif _figure == "I" and turn % 2 == 0:
            return random.randint(0, 9), 0
            return 9, 0
        else:
            return random.randint(0, 8), 0

    def _is_only_one_key_pressed(self):
        if self._up_pressed and not (self._down_pressed or self._left_pressed or self._right_pressed):
            return True
        if self._down_pressed and not (self._up_pressed or self._left_pressed or self._right_pressed):
            return True
        if self._left_pressed and not (self._down_pressed or self._up_pressed or self._right_pressed):
            return True
        if self._right_pressed and not (self._down_pressed or self._left_pressed or self._up_pressed):
            return True
        return False
