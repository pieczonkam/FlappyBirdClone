from imports import *

class Background:
    def __init__(self, x, y, image, context):
        self.image_1 = pygame.image.load(image).convert_alpha()
        self.image_2 = pygame.image.load(image).convert_alpha()
        self.width = self.image_1.get_width()
        self.x_1 = x
        self.x_2 = x + self.width
        self.y = y
        self.vx = Physics.PIPE_INIT_V
        self.context = context

    def draw(self):
        self.context.blit(self.image_1, (self.x_1, self.y))
        self.context.blit(self.image_2, (self.x_2, self.y))

    def moveX(self, delta_time):
        if self.x_1 + self.width < 0:
            self.x_1 = self.x_2 + self.width
        elif self.x_2 + self.width < 0:
            self.x_2 = self.x_1 + self.width
        self.x_1 += self.vx * delta_time
        self.x_2 += self.vx * delta_time

    def setVelocityX(self, vx):
        self.vx = vx

    def addVelocityX(self, vx):
        self.vx += vx

if __name__ == '__main__':
    pass