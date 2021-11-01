class Settings:
    FRAMERATE = 60
    HIGHSCORE_FILE = './highscore.txt'

    SCREEN_WIDTH = 799
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = 'Flappy Bird'

    GROUND_LEVEL = 570

    BIRD_POS_X = 200
    BIRD_POS_Y = 200
    BIRD_SIZE = 21
    BIRD_INTRO_OFFSET = 20

    PIPE_NMB = 3
    PIPE_WIDTH = 80
    PIPE_MIN_HEIGHT = 150
    PIPE_MAX_HEIGHT = 350
    PIPE_GAP = 150
    PIPE_DISTANCE = 213
    PIPE_INITIAL_OFFSET = 100
    PIPE_ADD_VELOCITY_INTERVAL = 15

    SCORE_TEXT_SIZE = 64
    HIGHSCORE_TEXT_SIZE = 42
    GAME_OVER_TEXT_SIZE = 42
    INTRO_TEXT_SIZE = 50

    SOUND_VOLUME = 0.4

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (50, 50, 50)

class Font:
    COMIC_SANS = 'Comic Sans MS'
    ARIAL = 'Arial'

class Physics:
    GRAVITY_V = 0.2
    UP_V = -0.6
    CEILING_BOUNCE_V = 0.08
    PIPE_INIT_V = -0.22
    PIPE_ADDED_V = -0.03
    BIRD_INTRO_V = 0.2
    BIRD_ROTATION_ANGLE_STEP = 12
    BIRD_ROTATION_DOWN_MAX = -90


if __name__ == '__main__':
    pass