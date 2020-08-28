import numpy as np
from pixels import *

class World_Grid:

    def __init__(self, width, height, rows, cols, x_pos, y_pos):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = pygame.Surface([width,height])
        
        if (width/cols > height/rows):
            pxwidth = height/rows
        else:
            pxwidth = width/cols
        self.pxwidth = pxwidth
        

        self.current_pixel_grid = np.empty((rows, cols), dtype=object)
        self.next_pixel_grid = np.empty((rows, cols), dtype=object)

    def draw_grid(self, pixel_grid):
        for pixel_row in pixel_grid:
            for pixel in pixel_row:
                if pixel != None:
                    pixel.draw_pixel(self.screen, self.pxwidth)

    def draw_layers(self):
        self.draw_grid(self.current_pixel_grid)

    # def make_layers(self, num_layers):
    #     self.layer_list = []
    #     for i in range(num_layers):
    #         self.layer_list.append(Grid_Layer(self.rows, self.cols))
    #     return self.layer_list

    def step_pixels(self):
        self.next_pixel_grid = np.empty((self.rows, self.cols), dtype=object)

        for y in range(self.rows):
            for x in range(self.cols):
                pixel = self.current_pixel_grid[y,x]
                if pixel != None:
                    pixel.has_stepped = False
                    self.next_pixel_grid[y,x] = pixel

        for row in self.current_pixel_grid:
            for pixel in row:
                if pixel != None and pixel.has_stepped == False:
                    pixel.update(self)
                    pixel.has_stepped = True

        self.current_pixel_grid = self.next_pixel_grid

    def get_current_pixel(self, x, y):
        return self.current_pixel_grid[y,x] if self.current_pixel_grid[y,x] else Pixel(x,y)

    def get_next_pixel(self, x, y):
        return self.next_pixel_grid[y,x] if self.next_pixel_grid[y,x] else Pixel(x,y)

    def is_valid_position(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def move_pixel(self, old_pos, new_pos):
        # old_pos = (old_pos[0], self.rows - old_pos[1] -1)
        # new_pos = (new_pos[0], self.rows - new_pos[1] -1)
        if self.is_valid_position(old_pos[0],old_pos[1]) and self.is_valid_position(new_pos[0],new_pos[1]):

            self.next_pixel_grid[old_pos[1], old_pos[0]] = self.current_pixel_grid[new_pos[1], new_pos[0]]
            if self.next_pixel_grid[old_pos[1], old_pos[0]] != None:
                self.current_pixel_grid[new_pos[1], new_pos[0]].pos_x = old_pos[0]
                self.current_pixel_grid[new_pos[1], new_pos[0]].pos_y = old_pos[1]
                self.current_pixel_grid[new_pos[1], new_pos[0]].has_stepped = True

            self.next_pixel_grid[new_pos[1], new_pos[0]] = self.current_pixel_grid[old_pos[1], old_pos[0]]
            self.current_pixel_grid[old_pos[1], old_pos[0]].pos_x = new_pos[0]
            self.current_pixel_grid[old_pos[1], old_pos[0]].pos_y = new_pos[1]

    def set_pixel(self, x, y, type_string = "NONE"):
        # y = self.rows - y - 1
        self.current_pixel_grid[y][x] = grid_pixel_factory(x,y,type_string)

def grid_pixel_factory(x, y, type_string):
    if type_string == "DEFAULT":
        return Grey(x,y)
    elif type_string == "SAND":
        return Sand(x,y)
    elif type_string == "WATER":
        return Water(x,y)
    elif type_string == "WOOD":
        return Wood(x,y)
    elif type_string == "FLAME":
        return Flame(x,y)
    elif type_string == "NONE":
        return None