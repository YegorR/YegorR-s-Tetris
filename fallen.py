import pygame
import block
from constant import BLOCK_SIZE, STARTING_POINT


class Fallen(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self._blocks = [[None for _ in range(15)] for _ in range(30)]
