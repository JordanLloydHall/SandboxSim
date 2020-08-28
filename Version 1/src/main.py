"""
Main entry point of the application
So far defines the initial loop 
"""

import sys, pygame, time
import numpy as np
from pixels import *
from grid_system import *
from mouse_events import *
from constants import *

# ---- start
pygame.init()
screen_size = screen_width, screen_height = 1200, 700
bgColour = 0,0,0

screen = pygame.display.set_mode(screen_size)



# ---- Calculate width of pixel (including padding) = 50
def pixel_fullwidth():
    return screen_width/NO_ROWS

# ---- Calculate width of pixel (not including padding) = 25
def pixel_width():
    return pixel_fullwidth()/2

def event_update():
        update_pixel_grid_mouse_hover(world_grid_main)

# ---- Initialisation
if __name__ == "__main__":
    run = True
    debug_ticker = 0

    world_grid_main = World_Grid(GRID_WIDTH, GRID_HEIGHT, NO_ROWS, NO_COLS)
    layer_buffer = world_grid_main.make_layers(1)
    objs_layer = layer_buffer[0]

    # ---- Main Loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.fill(bgColour)

        world_grid_main.screen.fill((25,25, 25))
        event_update()
        world_grid_main.draw_layers()   
        screen.blit(world_grid_main.screen, (GRID_X,GRID_Y))
        pygame.display.flip() 
        time.sleep(0.02)

        world_grid_main.step_pixels()
