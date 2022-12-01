# colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
BLUE = 0, 0, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
GRAY = 127, 127, 127

# game window dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT
SCREEN_HEIGHT = round(WINDOW_HEIGHT * 0.7) # height of pong play field

WIDTH_UNIT = round(WINDOW_WIDTH / 100) # width unit used for scaling the game

# number of the qubits for the quantum circuit
NUM_QUBITS=3

PADDLE_HEIGHT = round(SCREEN_HEIGHT / 2**NUM_QUBITS)
# cool down time (in milliseconds) before the next measurement is allowed
MEASUREMENT_COOLDOWN_TIME = 4000
# score to win a game
WIN_SCORE = 1