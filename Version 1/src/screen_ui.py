import pixels
import pygame
import os
from grid_system import grid_pixel_factory as pixel_factory
from mouse_events import *
import time

class SurfaceHolder:
    """
    This class exists because in python we can't pass integers
    by reference
    """

    def __init__(self, s, x, y):
        self.s, self.x, self.y = s, x, y

class Cursor:
    def __init__(self):
        self.active_pixel = [0, None]

class UI:
    def ru(self, n, unit):
        if unit == "vw":
            return int(n * (pygame.display.Info().current_w / 100))
        elif unit == "vh":
            return int(n * (pygame.display.Info().current_h / 100))

        return 0

    def __init__(self, world_grid, screen):
        self.screen = screen
        self.mousedown = False
        self.world_grid = world_grid
        self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h

        pygame.font.init()
        self.standard_font = pygame.font.Font(os.path.abspath('.') + '/Version 1/font/Inconsolata-Light.ttf', 50)
        self.small_font = pygame.font.Font(os.path.abspath('.') + '/Version 1/font/Inconsolata-Light.ttf', 25)

        self.cursor = Cursor()
        self.info_panel = InfoPanel(self.ru(53, "vw"), 50, self)
        self.pixel_select = PixelSelect(self.ru(53, "vw"), self.ru(50, "vh") + 25, self)

        self.ui_items = [self.info_panel, self.pixel_select]
    
    def draw(self):
        # world_grid doesn't use a surfaceholder
        self.screen.blit(self.world_grid.screen, (self.world_grid.x_pos, self.world_grid.y_pos))

        for item in self.ui_items:
            item.draw()
            self.screen.blit(item.surface.s, (item.surface.x, item.surface.y))
    
    def update(self):
        if (pygame.mouse.get_pressed()[0] == 1):
            self.mousedown = True
        else:
            self.mousedown = False

def write_text(s, to_render, font, height_offset, mc, mw, color):
    while 1:
        if mc < len(to_render):
            last_space = mc
            for i,c in enumerate(to_render[:mc]):
                if c == " ":
                    last_space = i
            st = to_render[:last_space]
        else:
            st = to_render 
        line = font.render(st, True, color, (255,255,255))
        s.blit(line, (mw - line.get_width(), height_offset))
        height_offset += line.get_height()

        if len(to_render) < mc:
            return height_offset
        else:
            to_render = to_render[last_space:]

class InfoPanel():
    def __init__(self, x, y, screen):
        self.x, self.y, self.screen = x, y, screen
        self.surface = SurfaceHolder(pygame.Surface([screen.ru(40, "vw"), screen.ru(50, "vh")], pygame.SRCALPHA), self.x, self.y)
        self.max_width = screen.ru(40, "vw")
        self.max_chars = {
            25: self.max_width // self.screen.small_font.size(' ')[0],
            50: self.max_width // self.screen.standard_font.size(' ')[0]
        }
    
    def draw(self):
        self.surface.s.fill((255,255,255))
        pix = pixel_factory(0,0,self.screen.cursor.active_pixel[1])
        if pix is None:
            return

        height_offset = write_text(self.surface.s, pix.get_type(), self.screen.standard_font, 0, self.max_chars[50], self.max_width,
            pix.get_color())
        height_offset = write_text(self.surface.s, pix.desc, self.screen.small_font, height_offset + 10, self.max_chars[25], self.max_width,
            (100,100,100))

        buoyancy_info, flammability_info = "Buoyancy:  " + str(pix.buoyancy), "Flammability:  " + str(pix.flammable)

        height_offset = write_text(self.surface.s, buoyancy_info, self.screen.small_font, height_offset + 20, self.max_chars[25],
            self.max_width, (0,0,0))
        height_offset = write_text(self.surface.s, flammability_info, self.screen.small_font, height_offset + 5, self.max_chars[25],
            self.max_width, (0,0,0))
    

class PixelSelect:
    def __init__(self, x, y, screen):
        self.x, self.y, self.screen = x, y, screen
        self.surface = SurfaceHolder(pygame.Surface([screen.ru(40, "vw"), screen.ru(40, "vh")], pygame.SRCALPHA), self.x, self.y)
        self.max_width = screen.ru(40, "vw")
        self.max_chars = {
            25: self.max_width // self.screen.small_font.size(' ')[0],
            50: self.max_width // self.screen.standard_font.size(' ')[0]
        }
        self.pixels = [(i, pixel_factory(0,0,p)) for i,p in pixels.Pixel.pixel_types]
    
    def draw(self):
        abs_mouse_pos = pygame.mouse.get_pos()
        for i,p in self.pixels:
            x_pos = (i % 3) * (self.max_width // 3)
            label = self.screen.standard_font.render(p.get_type().lower(), True, p.get_color(), (255,255,255))
            y_pos = label.get_height() * (i // 3)
            if self.screen.mousedown:
                if check_in_surface_bounds(abs_mouse_pos, self.x + x_pos, self.y + y_pos, label.get_width(), label.get_height()):
                    self.screen.cursor.active_pixel = [i, p.get_type()]
            self.surface.s.blit(label, (x_pos, y_pos))
        

