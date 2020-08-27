from constants import *
import pygame
import numpy as np
from pixels import *


def update_pixel_grid_mouse_hover(world_grid):
    mousePos = pygame.mouse.get_pos()

    if(
        ((mousePos[0] < GRID_X + GRID_WIDTH) and (mousePos[0] > GRID_X)) and 
        ((mousePos[1] < GRID_Y + GRID_HEIGHT) and (mousePos[1] > GRID_Y))):

        objPos = (int(np.trunc((mousePos[0] - GRID_X)/world_grid.pxwidth)), int(np.trunc((mousePos[1] - GRID_Y)/world_grid.pxwidth)))

        pixel_cursor = Pixel_Cursor(objPos[0], objPos[1])
        pixel_cursor.draw_pixel(world_grid.screen, PX_SIZE)

