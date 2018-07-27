from constant import PROMPT_POINT, STARTING_POINT
import block
from blockContainer import BlockContainer

figure_dict = {'I': 0, 'J': 1, 'L': 2, 'O': 3, 'S': 4, 'T': 5, 'Z': 6}


class Figure(BlockContainer):

    def _rerectering(self, turn, a, b, start_x=STARTING_POINT[0], start_y=STARTING_POINT[1]):
        if figure_dict[self._figure] == figure_dict['I']:
            if turn % 2 == 0:
                for i in range(4):
                    self._blocks[i].update(a, b + i, start_x, start_y)
            else:
                for i in range(4):
                    self._blocks[i].update(a + i, b, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['J']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(a+1, b + i, start_x, start_y)
                self._blocks[3].update(a, b + 2, start_x, start_y)
            elif turn % 4 == 1:
                self._blocks[0].update(a, b, start_x, start_y)
                for i in range(1, 4):
                    self._blocks[i].update(a + i - 1, b + 1, start_x, start_y)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(a, b + i, start_x, start_y)
                self._blocks[3].update(a + 1, b, start_x, start_y)
            else:
                for i in range(3):
                    self._blocks[i].update(a + i, b, start_x, start_y)
                self._blocks[3].update(a + 2, b + 1, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['L']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(a, b + i, start_x, start_y)
                self._blocks[3].update(a + 1, b + 2, start_x, start_y)
            elif turn % 4 == 1:
                for i in range(3):
                    self._blocks[i].update(a + i, b, start_x, start_y)
                self._blocks[3].update(a, b + 1, start_x, start_y)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(a + 1, b + i, start_x, start_y)
                self._blocks[3].update(a, b, start_x, start_y)
            else:
                for i in range(3):
                    self._blocks[i].update(a + i, b + 1, start_x, start_y)
                self._blocks[3].update(a + 2, b, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['O']:
            self._blocks[0].update(a, b, start_x, start_y)
            self._blocks[1].update(a + 1, b, start_x, start_y)
            self._blocks[2].update(a + 1, b + 1, start_x, start_y)
            self._blocks[3].update(a, b + 1, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['S']:
            if turn % 2 == 0:
                self._blocks[0].update(a, b + 1, start_x, start_y)
                self._blocks[1].update(a + 1, b + 1, start_x, start_y)
                self._blocks[2].update(a + 1, b, start_x, start_y)
                self._blocks[3].update(a + 2, b, start_x, start_y)
            else:
                self._blocks[0].update(a, b, start_x, start_y)
                self._blocks[1].update(a, b + 1, start_x, start_y)
                self._blocks[2].update(a + 1, b + 1, start_x, start_y)
                self._blocks[3].update(a + 1, b + 2, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['T']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(a + i, b, start_x, start_y)
                self._blocks[3].update(a + 1, b + 1, start_x, start_y)
            elif turn % 4 == 1:
                for i in range(3):
                    self._blocks[i].update(a + 1, b + i, start_x, start_y)
                self._blocks[3].update(a, b + 1, start_x, start_y)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(a + i, b + 1, start_x, start_y)
                self._blocks[3].update(a + 1, b, start_x, start_y)
            else:
                for i in range(3):
                    self._blocks[i].update(a, b + i, start_x, start_y)
                self._blocks[3].update(a + 1, b + 1, start_x, start_y)

        elif figure_dict[self._figure] == figure_dict['Z']:
            if turn % 2 == 0:
                self._blocks[0].update(a, b, start_x, start_y)
                self._blocks[1].update(a + 1, b, start_x, start_y)
                self._blocks[2].update(a + 1, b + 1, start_x, start_y)
                self._blocks[3].update(a + 2, b + 1, start_x, start_y)
            else:
                self._blocks[0].update(a + 1, b, start_x, start_y)
                self._blocks[1].update(a + 1, b + 1, start_x, start_y)
                self._blocks[2].update(a, b + 1, start_x, start_y)
                self._blocks[3].update(a, b + 2, start_x, start_y)
        else:
            pass

    def __init__(self, color='white', figure='I', turn=0):
        BlockContainer.__init__(self)

        self._figure = figure
        self._turn = turn

        self._blocks = [block.Block(color) for _ in range(4)]
        self.add(*self._blocks)
        self._rerectering(turn, 0, 0, PROMPT_POINT[0], PROMPT_POINT[1])

    def get_figure(self):
        return self._figure

    def get_turn(self):
        return self._turn

    def move(self, turn, a, b):
        self._rerectering(turn, a, b)
