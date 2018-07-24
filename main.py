import pygame
from pygame.locals import *
import constant
import block
import figure

class Game:
    def __init__(self):
        self._display_surf = None
        self._running = True
        self._background = None
        self.group = None

    def init(self):
        pygame.init()
        pygame.display.set_caption(constant.WINDOW_NAME)
        self._display_surf = pygame.display.set_mode((constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))
        self._running = True
        self._background = pygame.image.load(constant.FILE_BACKGROUND).convert()

        self.f = figure.Figure('blue', 'T', 1)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False

    def loop(self):
        pass

    def render(self):
        self._display_surf.blit(self._background, (0, 0))
        #self.group.draw(self._display_surf)
        self.f.draw(self._display_surf)
        pygame.display.update()

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
    game.execute()