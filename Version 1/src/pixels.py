import pygame

# ---- Pixel Objects
class Pixel:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.buoyancy = 0

    def draw_pixel(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos_x * 50 + 50 * 0.25, self.pos_y * 50 +50 * 0.25, 25, 25))

class Grey(Pixel):

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = (25,25,25)

    def update(self, world_grid):
        return

    def getType(self):
        return "DEFAULT"


class Sand(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (0,255,255)

        self.buoyancy = 0.5

    def update(self, world_grid):

        if world_grid.get_current_pixel(self.pos_x, self.pos_y) != self:
            for x in range(-1,2):
                if world_grid.get_next_pixel(self.pos_x+x, self.pos_y+1) == None:
                    world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y+y))
                    return
        
        for x in range(-1,2):
            if world_grid.get_current_pixel(self.pos_x+x, self.pos_y-1).buoyancy < self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return


    def getType(self):
        return "SAND"

class Water(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (156,211,219)

        self.buoyancy = 1

    def update(self, world_grid):
        if world_grid.get_current_pixel(self.pos_x, self.pos_y) != self:
            for x in range(-1,2):
                if world_grid.get_next_pixel(self.pos_x+x, self.pos_y+1) == None:
                    world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y+y))
                    return

        for x in range(-1,2):
            
            if world_grid.get_current_pixel(self.pos_x+x, self.pos_y-1).buoyancy < self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return

    def getType(self):
        return "WATER"

class Pixel_Cursor(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (100,0,100)
