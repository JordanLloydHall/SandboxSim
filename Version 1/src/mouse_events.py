from constants import *
import pygame
import numpy as np
from pixels import *
from grid_system import grid_pixel_factory

def update_pixel_grid_mouse_hover(world_grid, held_pixel):
    mouse_pos = pygame.mouse.get_pos()
    objPos = get_mouse_pos_relative_to_grid(mouse_pos, world_grid)

    if(check_in_surface_bounds(mouse_pos, world_grid.x_pos, world_grid.y_pos, world_grid.width, world_grid.height)):

        colour = grid_pixel_factory(0,0,Pixel.pixel_types[held_pixel][1]).get_color()
        

        pixel_cursor = Pixel_Cursor(objPos[0], objPos[1], colour)
        pixel_cursor.draw_pixel(world_grid.screen, world_grid.get_pixel_width())

def get_mouse_pos_relative_to_grid(abs_mouse_pos, world_grid):
    return (int(np.trunc((abs_mouse_pos[0] - world_grid.x_pos)/world_grid.pxwidth)), int(np.trunc((abs_mouse_pos[1] - world_grid.y_pos)/world_grid.pxwidth)))


def check_in_surface_bounds(abs_mouse_pos,x, y, width, height, bounds_bool = False):
    if ((abs_mouse_pos[0] < x + width) and (abs_mouse_pos[0] > x)) and ((abs_mouse_pos[1] < y + height) and (abs_mouse_pos[1] > y)):
        bounds_bool = not bounds_bool

    return bounds_bool