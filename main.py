import pygame
from pygame.locals import *
import constant
import logic

class Game:
    def __init__(self):
        self._display_surf = None
        self._running = True
        self._except_new_game = False
        self._background = None
        self._logic = None
        self._font = None
        self._end_font = None

    def init(self):
        pygame.init()
        pygame.display.set_caption(constant.WINDOW_NAME)
        self._display_surf = pygame.display.set_mode((constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))
        self._running = True
        self._except_new_game = False
        self._background = pygame.image.load(constant.FILE_BACKGROUND).convert()
        self._logic = logic.Logic()
        self._logic.start()

        self._font = pygame.font.SysFont("Arial", 20)
        self._end_font = pygame.font.SysFont("Arial", 30)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False

            elif self._except_new_game and event.type == pygame.KEYDOWN:
                self.new_game()

            elif event.type == constant.USER_EVENT:
                if event.user_type == constant.GAME_PERIOD_EVENT:
                    self._logic.period()
                elif (event.user_type == constant.BEFORE_SHIFT_EVENT_DOWN or
                      event.user_type == constant.BEFORE_SHIFT_EVENT_LEFT or
                      event.user_type == constant.BEFORE_SHIFT_EVENT_RIGHT or
                      event.user_type == constant.BEFORE_SHIFT_EVENT_UP):
                    self._logic.begin_shift(event.user_type)
                elif (event.user_type == constant.SHIFT_EVENT_DOWN or event.user_type == constant.SHIFT_EVENT_LEFT or
                      event.user_type == constant.SHIFT_EVENT_RIGHT or event.user_type == constant.SHIFT_EVENT_UP):
                    self._logic.shift(event.user_type)
                elif event.user_type == constant.GAME_OVER_EVENT:
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
        if self._except_new_game:
            label = self.render_end_labels()
            self._display_surf.blit(label[0], (50, 10))
            self._display_surf.blit(label[1], (20, 350))
        pygame.display.update()

    def destroy(self):
        self._logic.destroy()
        pygame.quit()

    def execute(self):
        self.init()
        while self._running:
            self.event()
            self.loop()
            self.render()
        self.destroy()

    def game_over(self):
        self._except_new_game = True

    def render_score(self):
        return self._font.render(str(self._logic.get_score()), 1, (200, 10, 10))

    def render_end_labels(self):
        return (self._end_font.render("GAME OVER", 1, (200, 10, 10)),
                self._end_font.render("Press any button!", 1, (200, 10, 10)))

    def new_game(self):
        self._logic = logic.Logic()
        self._logic.start()
        self._except_new_game = False


if __name__ == "__main__":
    game = Game()
    game.execute()
