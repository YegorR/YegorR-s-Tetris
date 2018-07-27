import pygame


class BlockContainer(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self._blocks = []

    def get_coord(self):
        return [i.get_coord() for i in self._blocks]
