import numpy as np
from pixels import *

class World_Grid:
    
    def __init__(self,width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.screen = pygame.Surface([width,height])
        
        if (width/cols > height/rows):
            pxwidth = height/rows
        else:
            pxwidth = width/cols
        self.pxwidth = pxwidth
        

    def draw_grid(self, pixel_grid):
        for pixel_row in pixel_grid:
            for pixel in pixel_row:
                if pixel != None:
                    pixel.draw_pixel(self.screen, self.pxwidth)

    def draw_layers(self, layer_buffer):
        for layer in layer_buffer:
            self.draw_grid(layer.grid)

    def make_layers(self, num_layers):
        self.layer_list = []
        for i in range(num_layers):
            self.layer_list.append(Grid_Layer(self.rows, self.cols))
        return self.layer_list

    
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_rows(self):
        return self.rows
    def get_cols(self):
        return self.cols
    
    def set_width(self, width):
        self.width = width
    def set_heigth(self, height):
        self.height = height

class Grid_Layer:
    
    def __init__(self, n_hor, n_ver):
        self.n_hor = n_hor
        self.n_ver = n_ver
        self.grid = np.empty((n_hor, n_ver), dtype=object)

    def fill_grid(self, type_string):

        for x in range(0, self.n_hor):
            for y in range(0, self.n_ver):

                if type_string == "DEFAULT":
                    self.grid[y][x] = Grey(x, y)
                elif type_string == "SAND":
                    self.grid[y][x] = Sand(x, y)
                elif type_string == "Water":
                    self.grid[y][x] = Water(x, y)
                
    
