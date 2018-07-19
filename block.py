import pygame
import constant

color_dict = {'red': 0, 'green': 1, 'blue': 2, 'black': 3, 'white': 4}

main_image = None

class Block(pygame.sprite.Sprite):

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        global main_image
        if main_image is None:
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