import numpy as np
from pixels import *
import time
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

    def draw_layers(self):
        for layer in self.layer_list:
            self.draw_grid(layer.grid)

    def make_layers(self, num_layers):
        self.layer_list = []
        for i in range(num_layers):
            self.layer_list.append(Grid_Layer(self.rows, self.cols))
        return self.layer_list

class Grid_Layer:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty((rows, cols), dtype=object)

    def get_pixel(self, x, y):
        return self.grid[self.rows - y][x]
    
    def set_pixel(self, x, y, type_string):
        if type_string == "DEFAULT":
            self.grid[y][x] = Grey(x,y)
        elif type_string == "SAND":
            self.grid[y][x] = Sand(x,y)
        elif type_string == "Water":
            self.grid[y][x] = Water(x,y)

    def fill_grid(self, type_string):
        for y in range(0, self.rows):
            for x in range(0, self.cols):
                pos_x = x
                pos_y = y
    
                if type_string == "DEFAULT":
                    self.grid[y][x] = Grey(x,y)
                elif type_string == "SAND":
                    self.grid[y][x] = Sand(x,y)
                elif type_string == "Water":
                    self.grid[y][x] = Water(x,y)
                          