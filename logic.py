import fallen
import random
import figure
import pygame
from constant import GAME_PERIOD, PERIOD_EVENT

figures = {'I', 'S', 'Z', 'O', 'L', 'J', 'T'}
colors = {'red', 'green', 'blue', 'black', 'white'}


class Logic:

    def __init__(self):
        self._field = [[False for _ in range(30)] for _ in range(15)]
        self._figure = None
        self._prompt = None
        self._fallen = fallen.Fallen()

        self._period = GAME_PERIOD[0]
        pygame.time.set_timer(PERIOD_EVENT, self._period)

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
            pos = self._start_position(self._figure, self._figure.get_turn())
            self._figure.move(self._figure.get_turn(), pos[0], pos[1])
            self._prompt = self._create_figure()


    def _create_figure(self):
        _figure = random.choice(list(figures))
        turn = random.randint(1, 4)
        color = random.choice(list(colors))
        return figure.Figure(color, _figure, turn)

    def _start_position(self, _figure, turn):
        if _figure == "I" and turn % 2 == 1:
            return random.randint(0, 6), 0
        elif ((_figure == "L" or _figure == "J") and (turn % 4 == 1 or turn % 4 == 3) or
            (_figure == "S" or _figure == "Z") and turn % 2 == 1 or
            _figure == "T" and (turn % 4 == 0 or turn % 4 == 2)):
            return random.randint(0, 7), 0
        elif _figure == "I" and turn % 2 == 0:
            return random.randint(0, 9), 0
        else:
            return random.randint(0, 8), 0
