from imports import *

class Pipe:
    def __init__(self, x, y, width, height, image, image_upside_down, context):
        self.x = x
        self.y = y
        self.vx = Physics.PIPE_INIT_V
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.image_upside_down = pygame.image.load(image_upside_down).convert_alpha()
        self.image_upside_down_height = self.image_upside_down.get_height()
        self.context = context
        self.scored = False
        
    def draw(self):
        self.context.blit(self.image_upside_down, (self.x, Settings.SCREEN_HEIGHT - self.height - Settings.PIPE_GAP - self.image_upside_down_height))
        self.context.blit(self.image, (self.x, self.y))

    def moveX(self, delta_time):
        if self.x + self.width <= 0:
            self.height = random.randint(Settings.PIPE_MIN_HEIGHT, Settings.PIPE_MAX_HEIGHT)
            self.x = Settings.SCREEN_WIDTH
            self.y = Settings.SCREEN_HEIGHT - self.height
            self.scored = False
        self.x += self.vx * delta_time

    def setVelocityX(self, vx):
        self.vx = vx

    def addVelocityX(self, vx):
        self.vx += vx

    def isScored(self):
        if not self.scored:
            if self.x + self.width <= Settings.BIRD_POS_X:
                self.scored = True
                return True
        return False

    def getRects(self):
        lower_pipe = pygame.Rect(self.x, self.y, self.width, self.height)
        upper_pipe = pygame.Rect(self.x, 0, self.width, Settings.SCREEN_HEIGHT - self.height - Settings.PIPE_GAP)
        return lower_pipe, upper_pipe


if __name__ == '__main__':
    pass