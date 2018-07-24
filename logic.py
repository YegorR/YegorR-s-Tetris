from constant import STARTING_POINT, BLOCK_SIZE
import fallen
import random
import figure

figures = {'I', 'S', 'Z', 'O', 'L', 'J', 'T'}
colors = {'red', 'green', 'blue', 'black', 'white'}


class Logic:

    def __init__(self):
        self._field = [[False for _ in range(15)] for _ in range(30)]
        self._figure = None
        self._prompt = None
        self._fallen = fallen.Fallen()

    def start(self):
        self._prompt = self._create_figute()
        self._figure = self._create_figute()
        pos = self._start_position(self._figure.get_figure(), self._figure.get_turn())
        self._figure.move(self._figure.get_turn(), *self._game_to_real(pos[0], pos[1]))

    def render(self, display_surf):
        if self._figure is not None:
            self._figure.draw(display_surf)
        if self._prompt is not None:
            self._prompt.draw(display_surf)
        if self._fallen is not None:
            self._fallen.draw(display_surf)


    def _game_to_real(self, a, b):
        return STARTING_POINT[0]+BLOCK_SIZE*a, STARTING_POINT[1]+BLOCK_SIZE*b

    def _create_figute(self):
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
