import pygame
from constant import FILE_MUSIC

class Sound:

    def __init__(self):
        pygame.mixer.music.load(FILE_MUSIC)

    def play(self):
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()