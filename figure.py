import pygame
from constant import BLOCK_SIZE, PROMPT_POINT
import block

figure_dict = {'I': 0, 'J': 1, 'L': 2, 'O': 3, 'S': 4, 'T': 5, 'Z': 6}


class Figure(pygame.sprite.Group):

    def _rerectering(self, turn, x, y):
        if figure_dict[self._figure] == figure_dict['I']:
            if turn % 2 == 0:
                for i in range(4):
                    self._blocks[i].update(x, y + BLOCK_SIZE*i)
            else:
                for i in range(4):
                    self._blocks[i].update(x + BLOCK_SIZE*i, y)

        elif figure_dict[self._figure] == figure_dict['J']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE, y + BLOCK_SIZE*i)
                self._blocks[3].update(x, y + BLOCK_SIZE*2)
            elif turn % 4 == 1:
                self._blocks[0].update(x, y)
                for i in range(1, 4):
                    self._blocks[i].update(x+BLOCK_SIZE*(i-1), y+BLOCK_SIZE)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(x, y+BLOCK_SIZE*i)
                self._blocks[3].update(x+BLOCK_SIZE, y)
            else:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE*i, y)
                self._blocks[3].update(x+BLOCK_SIZE*2, y+BLOCK_SIZE)

        elif figure_dict[self._figure] == figure_dict['L']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(x, y+BLOCK_SIZE*i)
                self._blocks[3].update(x+BLOCK_SIZE, y+BLOCK_SIZE*2)
            elif turn % 4 == 1:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE*i, y)
                self._blocks[3].update(x, y+BLOCK_SIZE)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE, y+BLOCK_SIZE*i)
                self._blocks[3].update(x, y)
            else:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE*i, y+BLOCK_SIZE)
                self._blocks[3].update(x+BLOCK_SIZE*2, y)

        elif figure_dict[self._figure] == figure_dict['O']:
            self._blocks[0].update(x, y)
            self._blocks[1].update(x+BLOCK_SIZE, y)
            self._blocks[2].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
            self._blocks[3].update(x, y+BLOCK_SIZE)

        elif figure_dict[self._figure] == figure_dict['S']:
            if turn % 2 == 0:
                self._blocks[0].update(x, y+BLOCK_SIZE)
                self._blocks[1].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
                self._blocks[2].update(x+BLOCK_SIZE, y)
                self._blocks[3].update(x+BLOCK_SIZE*2, y)
            else:
                self._blocks[0].update(x, y)
                self._blocks[1].update(x, y+BLOCK_SIZE)
                self._blocks[2].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
                self._blocks[3].update(x+BLOCK_SIZE, y+BLOCK_SIZE*2)

        elif figure_dict[self._figure] == figure_dict['T']:
            if turn % 4 == 0:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE*i, y)
                self._blocks[3].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
            elif turn % 4 == 1:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE, y+BLOCK_SIZE*i)
                self._blocks[3].update(x, y+BLOCK_SIZE)
            elif turn % 4 == 2:
                for i in range(3):
                    self._blocks[i].update(x+BLOCK_SIZE*i, y+BLOCK_SIZE)
                self._blocks[3].update(x+BLOCK_SIZE, y)
            else:
                for i in range(3):
                    self._blocks[i].update(x, y+BLOCK_SIZE*i)
                self._blocks[3].update(x+BLOCK_SIZE, y+BLOCK_SIZE)

        elif figure_dict[self._figure] == figure_dict['Z']:
            if turn % 2 == 0:
                self._blocks[0].update(x, y)
                self._blocks[1].update(x+BLOCK_SIZE, y)
                self._blocks[2].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
                self._blocks[3].update(x+BLOCK_SIZE*2, y+BLOCK_SIZE)
            else:
                self._blocks[0].update(x+BLOCK_SIZE, y)
                self._blocks[1].update(x+BLOCK_SIZE, y+BLOCK_SIZE)
                self._blocks[2].update(x, y+BLOCK_SIZE)
                self._blocks[3].update(x, y+BLOCK_SIZE*2)
        else:
            pass

    def __init__(self, color='white', figure='I', turn=0):
        pygame.sprite.Group.__init__(self)

        self._figure = figure
        self._turn = turn

        self._blocks = [block.Block(color) for _ in range(4)]
        self.add(*self._blocks)
        self._rerectering(turn, PROMPT_POINT[0], PROMPT_POINT[1])
