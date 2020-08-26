import pygame

# ---- Pixel Objects
class Pixel:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = (25,25,25)

    def draw_pixel(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos_x*50 - 50 * 0.75, self.pos_y*50 -50 * 0.75, 25, 25))

    def update(self, worldGrid):
        return

    def getType(self):
        return "DEFAULT"



class Sand(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (0,255,255)

    def update(self, worldGrid):

        for x in range(-1,2):
            if worldGrid.getPixel(self.pos_x+x, self.pos_y-1) in ["AIR", "WATER"]:
                worldGrid.swapPixels((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return

    def getType(self):
        return "SAND"

class Water(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (156,211,219)

    def update(self, worldGrid):
        for y in range(-1,1):
            for x in range(-1,2):
                if worldGrid.getPixel(self.pos_x+x, self.pos_y+y) in ["AIR"]:
                    worldGrid.swapPixels((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y+y))
                    return

    def getType(self):
        return "WATER"

class Pixel_Cursor(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (100,0,100)
