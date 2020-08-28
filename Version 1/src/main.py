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
bg_colour = 0,0,0

screen = pygame.display.set_mode(screen_size)
button_pressed = False
held_pixel = "WATER"

# ---- Calculate width of pixel (including padding) = 50
def pixel_fullwidth():
    return screen_width/NO_ROWS

# ---- Calculate width of pixel (not including padding) = 25
def pixel_width():
    return pixel_fullwidth()/2


def event_update():
    global button_pressed
    update_pixel_grid_mouse_hover(world_grid_main)
    
    if not button_pressed and pygame.mouse.get_pressed()[0] == 1:
        mouse_pos = pygame.mouse.get_pos()
        if(check_in_surface_bounds(mouse_pos, world_grid_main.x_pos, world_grid_main.y_pos, world_grid_main.width, world_grid_main.height)):
            temp_obj_pos = get_mouse_pos_relative_to_grid(mouse_pos, world_grid_main)
            obj_pos = (temp_obj_pos[0], world_grid_main.rows - temp_obj_pos[1] -1)
            if(objs_layer.get_pixel(obj_pos) == None or objs_layer.get_pixel(obj_pos).get_type != held_pixel):
                objs_layer.set_pixel(obj_pos, held_pixel)
                print(obj_pos)

    """
    if (pygame.mouse.get_pressed()[0] == 1):
        button_pressed = True
    else:
        button_pressed = False
    """


    



# ---- Initialisation
if __name__ == "__main__":
    run = True
    debug_ticker = 0
    
    world_grid_main = World_Grid(GRID_WIDTH, GRID_HEIGHT, NO_ROWS, NO_COLS)
    # layer_buffer = world_grid_main.make_layers(1)
    objs_layer = world_grid_main.current_pixel_grid

    # objs_layer.set_pixel(5,5, "SAND")


    # ---- Main Loop
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.fill(bg_colour)

        world_grid_main.screen.fill((25,25,25))
        event_update()

        world_grid_main.draw_layers()   
        screen.blit(world_grid_main.screen, (world_grid_main.x_pos,world_grid_main.y_pos))
        pygame.display.flip() 
        time.sleep(0.02)

        world_grid_main.step_pixels()
