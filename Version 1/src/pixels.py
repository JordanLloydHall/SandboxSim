import pygame

# ---- Pixel Objects
class Pixel:

    pixel_types = list(enumerate(["DEFAULT", "SAND", "WATER"], 0))

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

    def update(self, world_grid):

        for x in [0,-1,1]:
            if world_grid.is_valid_position(self.pos_x+x,self.pos_y+1) and world_grid.get_current_pixel(self.pos_x+x, self.pos_y+1).buoyancy > self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y+1))
                return

class Water(Pixel):
    def __init__(self, pos_x, pos_y):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (156,211,219)

        self.buoyancy = 0.5

    def update(self, world_grid):

        for x in [0,-1,1]:
            if world_grid.is_valid_position(self.pos_x+x,self.pos_y+1) and world_grid.get_current_pixel(self.pos_x+x, self.pos_y+1).buoyancy > self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y+1))
                return

class Wood(Pixel):

    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (149, 85, 0)
        self.buoyancy = 0.75
        self.flammable = 1

    def update(self, world_grid):

        for x in [0,-1,1]:
            if world_grid.get_current_pixel(self.pos_x+x, self.pos_y-1).buoyancy > self.buoyancy:
                world_grid.move_pixel((self.pos_x,self.pos_y), (self.pos_x+x, self.pos_y-1))
                return
        
class Flame(Pixel):

    def __init__(self, pos_x, pos_y):
        Pixel.__init__(self, pos_x, pos_y)
        self.color = (255,0,0)

    def update(self, world_grid):
        #If surrounded by nothing (by air), the Flame Pixel should be deleted
        # => This might be on a timer just so that the Flame doesnt extinguish too quickly.
        # => Alternatively, Flame could rise, and after a certain number of pixels moved it could disappear.
        #If a flammable object is in adjacent square(flammable > 0; currently only flammable = 1),
        #Flame should replace the other pixel.
        #Flame should be extinguished by some pixels i.e water, which could be checked as flammable < 0
        #i.e Water could have flammable = -1.
        pass

    

class Pixel_Cursor(Pixel):
    def __init__(self, pos_x, pos_y, color):
        
        Pixel.__init__(self, pos_x, pos_y)
        self.color = color

if __name__ == "__main__":

    print(Wood(0,0).get_type())
