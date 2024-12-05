from enum import Enum

# screen dimensions
HEIGHT = 720
WIDTH = 1200

# frames per second
FPS = 60

class GameState(Enum):
    MENU = 1
    GAMEPLAY = 2
    WIN = 3
    LOSE = 4
    CREDITS = 5
    LEADERBOARD = 6
