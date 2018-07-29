import pygame
import block
from constant import BLOCK_SIZE, STARTING_POINT
from blockContainer import BlockContainer


class Fallen(BlockContainer):

    def __init__(self):
        BlockContainer.__init__(self)
        self._blocks = [[None for _ in range(20)] for _ in range(10)]
