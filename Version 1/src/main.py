"""
Main entry point of the application
So far defines the initial loop 
"""

import sys, pygame, time
import numpy as np
from pixels import *
from pygame.locals import *
from grid_system import *
from mouse_events import *
from constants import *
import screen_ui

# ---- start
pygame.init()

padding = 20
#screen_size = screen_width, screen_height = GRID_WIDTH + padding*2, GRID_HEIGHT + padding*2
screen_size = screen_width, screen_height = 1520, 720

bg_colour = 255,255,255

screen = pygame.display.set_mode(screen_size, RESIZABLE)
held_pixel = 0

cycle_left_button = False
cycle_right_button = False


def event_update(cursor):
    global cycle_left_button
    global cycle_right_button
    update_pixel_grid_mouse_hover(world_grid_main, cursor.active_pixel[0])
    
    
    mouse_pos = pygame.mouse.get_pos()
    if(check_in_surface_bounds(mouse_pos, world_grid_main.x_pos, world_grid_main.y_pos, world_grid_main.width, world_grid_main.height)):
        obj_pos = get_mouse_pos_relative_to_grid(mouse_pos, world_grid_main)
        if pygame.mouse.get_pressed()[0] == 1:
            if(world_grid_main.get_current_pixel(obj_pos[0], obj_pos[1]).get_type() == Pixel.pixel_types[0][1]):
                world_grid_main.set_pixel(obj_pos[0], obj_pos[1], cursor.active_pixel[1])
        if pygame.mouse.get_pressed()[2] == 1:
            world_grid_main.set_pixel(obj_pos[0], obj_pos[1])
    
    keys = pygame.key.get_pressed()
    if not cycle_left_button and keys[pygame.K_LEFT]:
        cursor.active_pixel[0] = (cursor.active_pixel[0] - 1) % len(Pixel.pixel_types)
        cursor.active_pixel[1] = Pixel.pixel_types[cursor.active_pixel[0]][1]
    if not cycle_right_button and keys[pygame.K_RIGHT]:
        cursor.active_pixel[0] = (cursor.active_pixel[0] + 1) % len(Pixel.pixel_types)
        cursor.active_pixel[1] = Pixel.pixel_types[cursor.active_pixel[0]][1]
    
    if (keys[pygame.K_LEFT]):
        cycle_left_button = True
    else:
        cycle_left_button = False
    
    if (keys[pygame.K_RIGHT]):
        cycle_right_button = True
    else:
        cycle_right_button = False



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
    
    world_grid_main = World_Grid(GRID_WIDTH, GRID_HEIGHT, NO_ROWS, NO_COLS, padding, padding)
    # layer_buffer = world_grid_main.make_layers(1)
    objs_layer = world_grid_main.current_pixel_grid

    world_grid_main.set_pixel(5,5,"SAND")

    is_resized = False

    main_ui = screen_ui.UI(world_grid_main, screen)

    # ---- Main Loop
    while run:
        frame_start_time = int(time.time() * 1000000)

        screen.fill(bg_colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            if event.type == VIDEORESIZE:
                is_resized = True
                screen_size = event.size
                screen_width = screen_size[0]
                screen_height = screen_size[1]

            if event.type == pygame.ACTIVEEVENT and is_resized:
                screen = pygame.display.set_mode(screen_size, RESIZABLE)
                world_grid_main.update_dimensions(screen_width, screen_height, padding)

                is_resized = False

        world_grid_main.screen.fill((25,25,25))
        event_update(main_ui.cursor)
        world_grid_main.draw_layers()   
        #screen.blit(world_grid_main.screen, (world_grid_main.x_pos,world_grid_main.y_pos))
        main_ui.update()
        main_ui.draw()

        pygame.display.update()

        render_speed = int(time.time() * 1000000) - frame_start_time
        time.sleep(max(0, 0.02 - (render_speed / 1000000)))
        
        world_grid_main.step_pixels()
