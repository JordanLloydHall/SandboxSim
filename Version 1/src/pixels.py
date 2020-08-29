import pygame
import random
from behaviours import *

# ---- Pixel Objects
class Pixel:

    pixel_types = list(enumerate(["DEFAULT", "SAND", "WATER","WOOD", "FLAME", "LAVA", "STONE", "NITRO", "CLONE"], 0))

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.buoyancy = 1
        self.flammable = 0

        self.has_stepped = False
        self.color = None

        

    def draw_pixel(self, screen, pxwidth):
        px_fac = 1
        # print(screen.get_height())
        # print(screen.get_height() - ((self.pos_y + (1-px_fac)/2) * pxwidth))
        pygame.draw.rect(screen, self.color, ((self.pos_x +(1-px_fac)/2) * pxwidth, ((self.pos_y + (1-px_fac)/2) * pxwidth), pxwidth * px_fac, pxwidth * px_fac))

    def get_type(self):
        if (self.__class__.__name__.upper() == "PIXEL"):
            return "DEFAULT"
        else:
            return self.__class__.__name__.upper()
    def get_color(self):
        return self.color

class Default(Pixel):
    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (25,25,25)

    def update(self, world_grid):
        return


class Sand(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (239, 221, 111)

        self.buoyancy = 0
        self.flammable = 1

    def update(self, world_grid):

        if(gravity_fall(self, world_grid)):
            return
        if(bouyancy(self, world_grid, [0,-1,1])):
            return
        

        

class Water(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (156,211,219)

        self.buoyancy = 0.5

    def update(self, world_grid):

        if(gravity_fall(self, world_grid)):
            return

        if(bouyancy(self, world_grid, [0])):
            return

        liquid_motion(self, world_grid)


class Nitro(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (23,240,0)

        self.buoyancy = 0.5
        self.flammable = 1

    def update(self, world_grid):

        if(gravity_fall(self, world_grid)):
            return

        if(bouyancy(self, world_grid, [0])):
            return

        liquid_motion(self, world_grid)

class Clone(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (255,0,255)

        self.buoyancy = 1

    def update(self, world_grid):

        found_clonable = False
        observed_pixel = None
        for y in [-1,0,1]: # Checks the surroundings for a pixel to clone.
            for x in [-1,0,1]:
                if world_grid.is_valid_position(self.pos_x+x,self.pos_y+y) and not (x==0 and y==0):
                    candidate_pixel = world_grid.get_current_pixel(self.pos_x+x, self.pos_y+y)
                    if candidate_pixel.get_type() != "CLONE" and candidate_pixel.get_type() != "DEFAULT":
                        observed_pixel = candidate_pixel
                        found_clonable = True


        if not found_clonable:
            return

        for y1 in [-1,0,1]: # Looks for a spot to clone the found pixel and clones it
            for x1 in [-1,0,1]:

                if world_grid.is_valid_position(self.pos_x+x1,self.pos_y+y1) and not (x1==0 and y1==0):
                    candidate_place = (self.pos_x+x1, self.pos_y+y1)
                    if world_grid.get_next_pixel(*candidate_place).get_type() == "DEFAULT":
                        world_grid.set_next_pixel(*candidate_place, observed_pixel.get_type())    

class Wood(Pixel):

    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (149, 85, 0)
        self.buoyancy = 0.75
        self.flammable = 1

    def update(self, world_grid):

        pass

class Stone(Pixel):

    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (110, 110, 110)
        self.buoyancy = 0
        self.flammable = 0

    def update(self, world_grid):

        if(gravity_fall(self, world_grid)):
            return

class Lava(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (244,50,0)

        self.buoyancy = 0.5

    def update(self, world_grid):

        if(solidify(self, world_grid, "STONE", ["WATER"])):
            return

        if(gravity_fall(self, world_grid)):
            return

        if(bouyancy(self, world_grid, [0])):
            return

        if(random.randrange(0,50)/10 < 2.5):
            liquid_motion(self, world_grid)

        flame_spread(self, world_grid, False)
                  
class Flame(Pixel):

    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (149,19,19)
        self.buoyancy = 0

    def update(self, world_grid):

        if not flame_spread(self, world_grid):
            world_grid.set_next_pixel(self.pos_x, self.pos_y, "NONE")


    

class Pixel_Cursor(Pixel):
    def __init__(self, pos_x, pos_y, color):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = color
