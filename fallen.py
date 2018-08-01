import pygame
import block
from constant import BLOCK_SIZE, STARTING_POINT
from blockContainer import BlockContainer


class Fallen(BlockContainer):

    def __init__(self):
        BlockContainer.__init__(self)
        self._blocks = [[None for _ in range(20)] for _ in range(10)]

    def destroy_line(self, line):
        for j in range(10):
            self._blocks[j][line].kill()
        for i in range(line, 0, -1):
            for j in range(10):
                if self._blocks[j][i-1] is not None:
                    self._blocks[j][i-1].update(j, i)
                self._blocks[j][i] = self._blocks[j][i-1]

    def add(self, *sprites):
        BlockContainer.add(self, *sprites)
        for i in sprites:
            pos = i.get_coord()
            self._blocks[pos[0]][pos[1]] = i
