"""
Main entry point of the application

So far defines the initial loop 
"""

import sys, pygame, time
import numpy as np
from pixels import *
from grid_system import *

# ---- CONSTANTS
NO_ROWS = 10
NO_COLS = 10

# ---- start
pygame.init()
screen_size = screen_width, screen_height = 500, 500
bgColour = 0,0,0

screen = pygame.display.set_mode(screen_size)

# ---- Calculate width of pixel (including padding) = 50
def pixel_fullwidth():
    return screen_width/NO_ROWS

# ---- Calculate width of pixel (not including padding) = 25
def pixel_width():
    return pixel_fullwidth()/2

# ---- Mouse Cursor Funcs

def mouse_grid_plot(pxPos, pxObj):
    cursor_layer.grid.fill(None)
    cursor_layer.grid[pxPos[1] -1 ][pxPos[0] -1] = pxObj

def update_pixel_grid_mouse_hover():
    mousePos = pygame.mouse.get_pos()

    objPos = (int(np.trunc(mousePos[0]/50)), int(np.trunc(mousePos[1]/50)))
    mouse_grid_plot(objPos, Pixel_Cursor(objPos[0],objPos[1]))

# ---- Initialisation
if __name__ == "__main__":
    run = True
    debug_ticker = 0

    world_grid = World_Grid(NO_ROWS, NO_COLS, 25, screen)
    layer_buffer = world_grid.make_layers(3)
    void_layer = layer_buffer[0]
    objs_layer = layer_buffer[1]
    cursor_layer = layer_buffer[2]

    

    void_layer.fill_grid("DEFAULT")

    # ---- Main Loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.fill(bgColour)

        update_pixel_grid_mouse_hover()

        world_grid.draw_layers(layer_buffer)
        #obj_grid()
        
        pygame.display.flip() 
        time.sleep(0.02)
