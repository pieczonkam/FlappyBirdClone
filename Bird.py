from imports import *

class Bird:
    def __init__(self, x, y, size, image, image_offset_x, image_offset_y, context):
        self.x = x
        self.y = y
        self.vy = 0
        self.size = size
        self.image = pygame.image.load(image).convert_alpha()
        self.init_image = self.image.copy()
        self.image_offset_x = image_offset_x
        self.image_offset_y = image_offset_y
        self.context = context

    def draw(self):
        rect = self.image.get_rect(center=self.init_image.get_rect(topleft=(self.x - self.size + self.image_offset_x, self.y - self.size + self.image_offset_y)).center)
        self.context.blit(self.image, rect)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.init_image, angle)

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def moveY(self, delta_time): # If True - bird is dead
        if self.y + self.size >= Settings.GROUND_LEVEL:
            return True
        if self.y - self.size <= 0:
            self.vy = Physics.CEILING_BOUNCE_V
        self.y += self.vy * delta_time
        return False

    def setVelocityY(self, vy):
        self.vy = vy

    def addVelocityY(self, vy):
        self.vy += vy

    def checkCollision(self, rect):
        dist_x = abs(self.x - (rect.left + rect.width / 2))
        dist_y = abs(self.y - (rect.top + rect.height / 2))

        if dist_x > rect.width / 2 + self.size:
            return False
        if dist_y > rect.height / 2 + self.size:
            return False
        if dist_x <= rect.width / 2:
            return True
        if dist_y <= rect.height / 2:
            return True
        return math.pow(dist_x - rect.width / 2, 2) + math.pow(dist_y - rect.height / 2, 2) <= math.pow(self.size, 2)


if __name__ == '__main__':
    pass