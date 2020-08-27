import pygame

# ---- Pixel Objects
class Pixel:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.buoyancy = 1

        self.has_stepped = False

    def draw_pixel(self, screen, pxwidth):
        px_fac = 1
        pygame.draw.rect(screen, self.color, ((self.pos_x +(1-px_fac)/2) * pxwidth, (self.pos_y + (1-px_fac)/2) * pxwidth, pxwidth * px_fac, pxwidth * px_fac))

    def get_type(self):
        return "DEFAULT"

class Grey(Pixel):
    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (25,25,25)

    def update(self, world_grid):
        return
    
    def get_type(self):
        return "DEFAULT"


class Sand(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (239, 221, 111)

        self.buoyancy = 0

    def update(self, world_grid):

        for x in [0,-1,1]:
            if world_grid.get_current_pixel(self.pos_x+x, self.pos_y-1).buoyancy > self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return

    def get_type(self):
        return "SAND"

class Water(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (156,211,219)

        self.buoyancy = 0.5

    def update(self, world_grid):

        for x in [0,-1,1]:
            if world_grid.get_current_pixel(self.pos_x+x, self.pos_y-1).buoyancy > self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return

    def get_type(self):
        return "WATER"

class Pixel_Cursor(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (100,0,100)
