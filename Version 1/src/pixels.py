

# ---- Pixel Objects
class Pixel:
    def __init__(self, posX, posY, Color):
        self.posX = posX
        self.posY = posY
        self.Color = Color

    def draw_pixel(self):
        pygame.draw.rect(screen, self.Color, (self.posX - 50 * 0.75, self.posY -50 * 0.75, 25, 25))

class Pixel_Cursor(Pixel):
    def __init__(self, posX, posY):
        self.Color = 100,0,100
        Pixel.__init__(self, posX, posY, self.Color)