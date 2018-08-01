import pygame
from pygame.locals import *
import constant
import logic

class Game:
    def __init__(self):
        self._display_surf = None
        self._running = True
        self._background = None
        self._logic = None
        self._font = None

    def init(self):
        pygame.init()
        pygame.display.set_caption(constant.WINDOW_NAME)
        self._display_surf = pygame.display.set_mode((constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))
        self._running = True
        self._background = pygame.image.load(constant.FILE_BACKGROUND).convert()
        self._logic = logic.Logic()
        self._logic.start()

        self._font = pygame.font.SysFont("Arial", 20)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False

            elif event.type == constant.GAME_PERIOD_EVENT:
                self._logic.period()
            elif event.type == constant.BEFORE_SHIFT_EVENT:
                self._logic.begin_shift()
            elif event.type == constant.SHIFT_EVENT:
                self._logic.shift()
            elif event.type == constant.GAME_OVER_EVENT:
                self.game_over()

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                event.key == pygame.K_RIGHT or event.key == pygame.K_UP):
                self._logic.key_down(event.key)
            elif event.type == pygame.KEYUP and (event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or
                event.key == pygame.K_RIGHT or event.key == pygame.K_UP):
                self._logic.key_up(event.key)

    def loop(self):
        pass

    def render(self):
        self._display_surf.blit(self._background, (0, 0))
        self._logic.render(self._display_surf)
        self._display_surf.blit(self.render_score(), (220, 130))
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

    def game_over(self):
        self._running = False
        print("GAME OVER")

    def render_score(self):
        return self._font.render(str(self._logic.get_score()), 1, (200, 10, 10))


if __name__ == "__main__":
    game = Game()
    game.execute()
