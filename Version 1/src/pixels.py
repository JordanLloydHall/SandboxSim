import pygame

# ---- Pixel Objects
class Pixel:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.Color = (25,25,25)

    def draw_pixel(self, screen, width, fullwidth):
        pygame.draw.rect(screen, self.Color, (self.posX - fullwidth * 0.75, self.posY - fullwidth * 0.75, width, width))


class Sand(Pixel):
    def __init__(self, posX, posY):
        
        Pixel.__init__(self, posX, posY)
        self.Color = (0,255,255)


class Pixel_Cursor(Pixel):
    def __init__(self, posX, posY):
        
        Pixel.__init__(self, posX, posY)
        self.Color = (100,0,100)
