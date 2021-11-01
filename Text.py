from imports import *

class Text:
    def __init__(self, x, y, text, text_size, context):
        self.x = x
        self.y = y
        self.text = text
        self.text_size = text_size
        self.context = context
        self.font = pygame.font.Font(utils.resourcePath('fonts/The Bomb Sound.ttf'), self.text_size)
        self.bg_color = Color.WHITE
        self.outline_color = Color.GREY
        
        self.circle_cache = {}

    def draw(self):
        for i, line in enumerate(self.text.splitlines()):
            text_rect = self.font.render(line, True, Color.BLACK).get_rect(center=(self.x, self.y + i * self.text_size))
            self.context.blit(self.prepareSurf(line), text_rect)

    def prepareSurf(self, text, opx=3):
        text_surface = self.font.render(text, True, self.bg_color).convert_alpha()
        width = text_surface.get_width() + 2 * opx
        height = self.font.get_height()

        outline_surface = pygame.Surface((width, height + 2 * opx)).convert_alpha()
        outline_surface.fill((0, 0, 0, 0))
        surface = outline_surface.copy()

        outline_surface.blit(self.font.render(text, True, self.outline_color).convert_alpha(), (0, 0))
        for dx, dy in self.circlePoints(opx):
            surface.blit(outline_surface, (dx + opx, dy + opx))
        surface.blit(text_surface, (opx, opx))
        
        return surface

    def circlePoints(self, r):
        r = int(round(r))
        if r in self.circle_cache:
            return self.circle_cache[r]
        x, y, e = r, 0, 1 - r
        self.circle_cache[r] = points = []
        while x >= y:
            points.append((x, y))
            y += 1
            if e < 0:
                e += 2 * y - 1
            else:
                x -= 1
                e += 2 * (y - x) - 1
        points += [(y, x) for x, y in points if x > y]
        points += [(-x, y) for x, y in points if x]
        points += [(x, -y) for x, y in points if y]
        return points
    
if __name__ == '__main__':
    pass