import sys, pygame, time
import numpy as np
from pixels import *
from grid_system import *

pygame.init()
screen_size = screen_width, screen_height = 500, 500
bgColour = 0,0,0

pixelColour = 25,25,25

screen = pygame.display.set_mode(screen_size)

# ---- Creates Pixel Grid
def pixel_grid():
    for x in range(0, 10):
        for y in range(0, 10):
            void_layer.grid[y][x] = (Grey(x, y))


# ---- Mouse Cursor Funcs

def mouse_grid_plot(pxPos, pxObj):
    cursor_layer.grid.fill(None)
    cursor_layer.grid[pxPos[1] -1 ][pxPos[0] -1] = pxObj

def update_pixel_grid_mouse_hover():
    mousePos = pygame.mouse.get_pos()
    objPos = (int(np.trunc(mousePos[0]/50)), int(np.trunc(mousePos[1]/50)))
    mouse_grid_plot(objPos, Pixel_Cursor((objPos[0]),(objPos[1])))

# ---- Initialisation
run = True
debug_ticker = 0

"""
void_layer = np.empty((10, 10), dtype=object)
objs_layer = np.empty((10, 10), dtype=object)

cursor_layer = np.empty((10, 10), dtype=object)

"""

void_layer = Grid_Layer(10,10)
objs_layer = Grid_Layer(10,10)
cursor_layer = Grid_Layer(10,10)
pixel_grid()

#void_layer.fill_grid()

world_grid = World_Grid(10, 10, 25, screen)
# ---- Main Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(bgColour)

    update_pixel_grid_mouse_hover()

    layer_buffer = [void_layer, objs_layer, cursor_layer]
    world_grid.draw_layers(layer_buffer)
    #obj_grid()
    
    pygame.display.flip() 
    time.sleep(0.02)
