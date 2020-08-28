import numpy as np
from pixels import *

class World_Grid:

    def __init__(self, width, height, rows, cols):
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
        # y = self.rows - y - 1
        return self.current_pixel_grid[y,x] if self.current_pixel_grid[y,x] else Pixel(x,y)

    def get_next_pixel(self, x, y):
        # y = self.rows - y - 1
        return self.next_pixel_grid[y,x] if self.next_pixel_grid[y,x] else Pixel(x,y)

    def move_pixel(self, old_pos, new_pos):
        # old_pos = (old_pos[0], self.rows - old_pos[1] -1)
        # new_pos = (new_pos[0], self.rows - new_pos[1] -1)
        if 0 <= old_pos[0] < self.width and 0 <= old_pos[1] < self.height and 0 <= new_pos[0] < self.width and 0 <= new_pos[1] < self.height:

            self.next_pixel_grid[old_pos[1], old_pos[0]] = self.current_pixel_grid[new_pos[1], new_pos[0]]
            if self.next_pixel_grid[old_pos[1], old_pos[0]] != None:
                self.current_pixel_grid[new_pos[1], new_pos[0]].pos_x = old_pos[0]
                self.current_pixel_grid[new_pos[1], new_pos[0]].pos_y = old_pos[1]
                self.current_pixel_grid[new_pos[1], new_pos[0]].has_stepped = True

            self.next_pixel_grid[new_pos[1], new_pos[0]] = self.current_pixel_grid[old_pos[1], old_pos[0]]
            self.current_pixel_grid[old_pos[1], old_pos[0]].pos_x = new_pos[0]
            self.current_pixel_grid[old_pos[1], old_pos[0]].pos_y = new_pos[1]

    def set_pixel(self, x, y, type_string):
        if type_string == "DEFAULT":
            self.current_pixel_grid[y][x] = Grey(x,y)
        elif type_string == "SAND":
            self.current_pixel_grid[y][x] = Sand(x,y)
        elif type_string == "WATER":
            self.current_pixel_grid[y][x] = Water(x,y)
        elif type_string == "WOOD":
            self.current_pixel_grid[y][x] = Wood(x,y)
        elif type_string == "FLAME":
            self.current_pixel_grid[y][x] = Flame(x,y)



# class Grid_Layer:
    
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.grid = np.empty((rows, cols), dtype=object)

#     def get_pixel(self, x, y):
#         # y = self.rows - y -1
#         return self.grid[y][x]

#     def set_specific_pixel(self, x, y, pixel):
#         pixel.pos_y = y
#         pixel.pos_x = x

#         # y = self.rows - y - 1
#         self.grid[y][x] = pixel


#     def remove_pixel(self, x, y):
#         # y = self.rows - y - 1
#         self.grid[y][x] = None

    
#     def set_pixel(self, x, y, type_string):
#         # ny = self.rows - y - 1
#         if type_string == "DEFAULT":
#             self.grid[y][x] = Grey(x,y)
#         elif type_string == "SAND":
#             self.grid[y][x] = Sand(x,y)
#         elif type_string == "WATER":
#             self.grid[y][x] = Water(x,y)
#         elif type_string == "WOOD":
#             self.grid[y][x] = Wood(x,y)
#         elif type_string == "FLAME":
#             self.grid[y][x] = Flame(x,y)



#     def fill_grid(self, type_string):
#         for y in range(0, self.rows):
#             for x in range(0, self.cols):
    
#                 if type_string == "DEFAULT":
#                     self.grid[y][x] = Grey(x,y)
#                 elif type_string == "SAND":
#                     self.grid[y][x] = Sand(x,y)
#                 elif type_string == "WATER":
#                     self.grid[y][x] = Water(x,y)
#                 elif type_string == "WOOD":
#                     self.grid[y][x] = Wood(x,y)
#                 elif type_string == "FLAME":
#                     self.grid[y][x] = Flame(x,y)