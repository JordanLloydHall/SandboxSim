from constants import *
import pygame
import numpy as np
from pixels import *

def mouse_grid_plot(pxPos, pxObj, cursor_layer):
    cursor_layer.grid.fill(None)
    cursor_layer.grid[pxPos[1]][pxPos[0]] = pxObj

def update_pixel_grid_mouse_hover(world_grid):
    mousePos = pygame.mouse.get_pos()

    if(
        ((mousePos[0] < GRID_X + GRID_WIDTH) and (mousePos[0] > GRID_X)) and 
        ((mousePos[1] < GRID_Y + GRID_HEIGHT) and (mousePos[1] > GRID_Y))):

        objPos = (int(np.trunc((mousePos[0] - GRID_X)/world_grid.pxwidth)), int(np.trunc((mousePos[1] - GRID_Y)/world_grid.pxwidth)))
        #print(objPos)
        mouse_grid_plot(objPos, Pixel_Cursor(objPos[0],objPos[1]), world_grid.layer_list[1])
    else:
        world_grid.layer_list[1].grid.fill(None)

