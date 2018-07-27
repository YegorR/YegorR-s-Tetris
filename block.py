import pygame
import constant

color_dict = {'red': 0, 'green': 1, 'blue': 2, 'black': 3, 'white': 4}


class Block(pygame.sprite.Sprite):

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        main_image = pygame.image.load(constant.FILE_BLOCK).convert_alpha()
        pxarray = pygame.PixelArray(main_image)

        if color_dict[color] == color_dict['red']:
            repl_color = (255, 0, 0, 255)
        elif color_dict[color] == color_dict['green']:
            repl_color = (0, 255, 0, 255)
        elif color_dict[color] == color_dict['blue']:
            repl_color = (0, 0, 255, 255)
        elif color_dict[color] == color_dict['black']:
            repl_color = (0, 0, 0, 255)
        elif color_dict[color] == color_dict['white']:
            repl_color = (255, 255, 255, 255)
        else:
            repl_color = (128, 128, 128, 255)

        pxarray.replace((0, 0, 0, 0), repl_color)
        self.image = pxarray.make_surface()
        self.rect = self.image.get_rect()
        self._a = 0
        self._b = 0
        self._start_x = 0
        self._start_y = 0

    def update(self, a, b, start_x=constant.STARTING_POINT[0], start_y=constant.STARTING_POINT[1]):
        self.rect.x = start_x+constant.BLOCK_SIZE*a
        self.rect.y = start_y+constant.BLOCK_SIZE*b
        self._a = a
        self._b = b
        self._start_x = start_x
        self._start_y = start_y

    def get_coord(self):
        return self._a, self._b