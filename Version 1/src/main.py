import sys, pygame, time
import numpy as np

pygame.init()
size = width, height = 500, 500
bgColour = 0,0,0

pixelColour = 25,25,25

screen = pygame.display.set_mode(size)

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


# ---- Mouse Cursor

def mouse_grid_plot(pxPos, pxObj):
    cursor_layer.fill(None)
    cursor_layer[pxPos[1]][pxPos[0]] = pxObj

def update_pixel_grid_mouse_hover():
    mousePos = pygame.mouse.get_pos()
    objPos = (int(np.trunc(mousePos[0]/50)), int(np.trunc(mousePos[1]/50)))
    mouse_grid_plot(objPos, Pixel_Cursor((objPos[0]+1)*50,(objPos[1]+1)*50))

# ---- Rendering Functions

def draw_grid(pixelGrid):
    for pixelRow in pixelGrid:
        for pixel in pixelRow:
            if pixel != None:
                pixel.draw_pixel() 

# ---- Initialisation
run = True
debug_ticker = 0


void_layer = np.empty((10, 10), dtype=object)
objs_layer = np.empty((10, 10), dtype=object)
cursor_layer = np.empty((10, 10), dtype=object)
print(void_layer)
pixel_grid()

# ---- Main Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    screen.fill(bgColour)

    update_pixel_grid_mouse_hover()

    layer_buffer = [void_layer, objs_layer, cursor_layer]
    for layer in layer_buffer:
        draw_grid(layer)
    #obj_grid()
    
    pygame.display.flip() 
    time.sleep(0.02)
