import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        self._display_surf = None
        self._running = True

    def init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((300, 400))
        self._running = True

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False

    def loop(self):
        pass

    def render(self):
        pass

    def destroy(self):
        pygame.quit()

    def execute(self):
        self.init()
        while self._running:
            self.event()
            self.loop()
            self.render()
        self.destroy()


if __name__ == "__main__":
    game = Game()
    game.init()
    game.execute()