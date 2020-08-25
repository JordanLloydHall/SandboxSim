import sys, pygame, time
import numpy as np
from pixels import *

# ---- CONSTANTS
NO_ROWS = 10
NO_COLS = 10

# ---- start
pygame.init()
screen_size = screen_width, screen_height = 500, 500
bgColour = 0,0,0

pixelColour = 25,25,25

screen = pygame.display.set_mode(screen_size)





# ---- Calculate width of pixel (including padding) = 50
def pixel_fullwidth():
    return screen_width/NO_ROWS

# ---- Calculate width of pixel (not including padding) = 25
def pixel_width():
    return pixel_fullwidth()/2

# ---- Creates Pixel Grid
def pixel_grid():
    for x in range(0, NO_ROWS):
        for y in range(0, NO_COLS):
            void_layer[y][x] = (Pixel((x+1) * pixel_fullwidth(), (y+1) * pixel_fullwidth()))

# ---- World Grid
class World_Grid:

    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    def draw_grid(self, pixelGrid):
        for pixelRow in pixelGrid:
            for pixel in pixelRow:
                if pixel != None:
                    pixel.draw_pixel(self.screen, pixel_width(), pixel_fullwidth())

    def draw_layers(self, layer_buffer):
        for layer in layer_buffer:
            self.draw_grid(layer)
    
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def set_width(self, width):
        self.width = width
    def set_heigth(self, height):
        self.height = height


# ---- Mouse Cursor Funcs

def mouse_grid_plot(pxPos, pxObj):
    cursor_layer.fill(None)
    cursor_layer[pxPos[1]][pxPos[0]] = pxObj

def update_pixel_grid_mouse_hover():
    mousePos = pygame.mouse.get_pos()
    objPos = (int(np.trunc(mousePos[0]/pixel_fullwidth())), int(np.trunc(mousePos[1]/pixel_fullwidth())))
    mouse_grid_plot(objPos, Pixel_Cursor((objPos[0]+1)*pixel_fullwidth(),(objPos[1]+1)*pixel_fullwidth()))

# ---- Initialisation
run = True
debug_ticker = 0


void_layer = np.empty((NO_ROWS, NO_COLS), dtype=object)
objs_layer = np.empty((NO_ROWS, NO_COLS), dtype=object)

cursor_layer = np.empty((NO_ROWS, NO_COLS), dtype=object)
pixel_grid()

world_grid = World_Grid(NO_ROWS, NO_COLS, screen)
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
