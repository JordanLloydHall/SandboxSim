import pygame

# ---- Pixel Objects
class Pixel:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.Color = (25,25,25)

    def draw_pixel(self, screen):
        pygame.draw.rect(screen, self.Color, (self.posX * 50 + 50 * 0.25, self.posY * 50 +50 * 0.25, 25, 25))


class Sand(Pixel):
    def __init__(self, posX, posY):
        
        Pixel.__init__(self, posX, posY)
        self.Color = (0,255,255)


class Pixel_Cursor(Pixel):
    def __init__(self, posX, posY):
        
        Pixel.__init__(self, posX, posY)
        self.Color = (100,0,100)
