class World_Grid:

    def __init__(self, width, height, pxwidth, screen):
        self.width = width
        self.height = height
        self.pxwidth = pxwidth
        self.screen = screen

    def draw_grid(self, pixelGrid):
        for pixelRow in pixelGrid:
            for pixel in pixelRow:
                if pixel != None:
                    pixel.draw_pixel(self.screen)

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