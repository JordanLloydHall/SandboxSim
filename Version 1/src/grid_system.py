import numpy as np
from pixels import *

class World_Grid:

    def __init__(self, width, height, pxwidth, screen):
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
        

        self.current_pixel_grid = current_pixel_grid
        self.next_pixel_grid = Grid_Layer(current_pixel_grid.n_hor, current_pixel_grid.n_ver)

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

    def step_pixels(self):
        self.next_pixel_grid = Grid_Layer(self.current_pixel_grid.n_hor, self.current_pixel_grid.n_ver)

        for y in range(self.current_pixel_grid.n_ver):
            for x in range(self.current_pixel_grid.n_hor):
                pixel = self.current_pixel_grid.grid[y,x]
                if pixel != None:
                    pixel.has_stepped = False
                    self.next_pixel_grid.grid[y,x] = pixel

        for row in self.current_pixel_grid.grid:
            for pixel in row:
                if pixel != None and pixel.has_stepped == False:
                    pixel.update(self)
                    pixel.has_stepped = True

        self.current_pixel_grid = self.next_pixel_grid

    def get_current_pixel(self, x, y):
        return self.current_pixel_grid.grid[y,x] if self.current_pixel_grid.grid[y,x] else Pixel(x,y)

    def get_next_pixel(self, x, y):
        return self.next_pixel_grid.grid[y,x] if self.next_pixel_grid.grid[y,x] else Pixel(x,y)

    def move_pixel(self, old_pos, new_pos):
        if 0 <= old_pos[0] < self.width and 0 <= old_pos[1] < self.height and 0 <= new_pos[0] < self.width and 0 <= new_pos[1] < self.height:

            self.next_pixel_grid.grid[old_pos[1], old_pos[0]] = self.current_pixel_grid.grid[new_pos[1], new_pos[0]]
            if self.next_pixel_grid.grid[old_pos[1], old_pos[0]] != None:
                self.current_pixel_grid.grid[new_pos[1], new_pos[0]].pos_x = old_pos[0]
                self.current_pixel_grid.grid[new_pos[1], new_pos[0]].pos_y = old_pos[1]
                self.current_pixel_grid.grid[new_pos[1], new_pos[0]].has_stepped = True

            self.next_pixel_grid.grid[new_pos[1], new_pos[0]] = self.current_pixel_grid.grid[old_pos[1], old_pos[0]]
            self.current_pixel_grid.grid[old_pos[1], old_pos[0]].pos_x = new_pos[0]
            self.current_pixel_grid.grid[old_pos[1], old_pos[0]].pos_y = new_pos[1]



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
