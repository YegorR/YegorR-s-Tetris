from pygame import USEREVENT

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 300

FILE_BACKGROUND = "img/background.png"
FILE_BLOCK = "img/block.png"

WINDOW_NAME = "YegorR's Tetris"

BLOCK_SIZE = 15
STARTING_POINT = (50, 50)
PROMPT_POINT = (220, 50)

GAME_PERIOD = [100, 1000, 1000, 750, 500, 400, 250, 200, 100]
SHIFT_PERIOD = 100
BEFORE_SHIFT_PERIOD = 500

GAME_PERIOD_EVENT = USEREVENT + 1
SHIFT_EVENT = USEREVENT + 2
BEFORE_SHIFT_EVENT = USEREVENT + 3
