import sys, pygame, time
import numpy as np

pygame.init()
screen_size = screen_width, screen_height = 500, 500
bgColour = 0,0,0

pixelColour = 25,25,25

screen = pygame.display.set_mode(screen_size)
# ---- World Grid

class World_Grid:

    def __init__(self, width, height, pxwidth):
        self.width = width
        self.height = height
        self.pxwidth = pxwidth

    def draw_grid(self, pixelGrid):
        for pixelRow in pixelGrid:
            for pixel in pixelRow:
                if pixel != None:
                    pixel.draw_pixel() 

    def draw_layers(self, layer_buffer):
        for layer in layer_buffer:
            self.draw_grid(layer)
    
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_pxwidth(self):
        return self.pxwidth
    
    def set_width(self, width):
        self.width = width
    def set_heigth(self, height):
        self.height = height
    def set_pxwidth(self, pxwidth):
        self.pxwidth = pxwidth



# ---- Pixel Objects
class Pixel:
    def __init__(self, posX, posY, Color):
        self.posX = posX
        self.posY = posY
        self.Color = Color

    def draw_pixel(self):
        pygame.draw.rect(screen, self.Color, (self.posX - 50 * 0.75, self.posY -50 * 0.75, 25, 25))

class Pixel_Cursor(Pixel):
    def __init__(self, posX, posY):
        self.Color = 100,0,100
        Pixel.__init__(self, posX, posY, self.Color)



# ---- Creates Pixel Grid
def pixel_grid():
    for x in range(0, 10):
        for y in range(0, 10):
            void_layer[y][x] = (Pixel((x+1) * 50, (y+1) * 50, pixelColour))


# ---- Mouse Cursor Funcs

def mouse_grid_plot(pxPos, pxObj):
    cursor_layer.fill(None)
    cursor_layer[pxPos[1]][pxPos[0]] = pxObj

def update_pixel_grid_mouse_hover():
    mousePos = pygame.mouse.get_pos()
    objPos = (int(np.trunc(mousePos[0]/50)), int(np.trunc(mousePos[1]/50)))
    mouse_grid_plot(objPos, Pixel_Cursor((objPos[0]+1)*50,(objPos[1]+1)*50))

# ---- Rendering Functions



# ---- Initialisation
run = True
debug_ticker = 0


void_layer = np.empty((10, 10), dtype=object)
objs_layer = np.empty((10, 10), dtype=object)
cursor_layer = np.empty((10, 10), dtype=object)
print(void_layer)
pixel_grid()

world_grid = World_Grid(10, 10, 25)
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
