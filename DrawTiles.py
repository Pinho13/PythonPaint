import pygame as pg
import pygame.mouse

from pygame import Vector2
from Settings import *
from main import *
from Tools import *

sprites = pg.sprite.Group()


class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size, color):
        super().__init__()
        self.pos = pos
        self.size = size
        self.color = color

        self.image = pg.Surface((size.x, size.y))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=self.pos)

        for tile in sprites.sprites():
            if isinstance(tile, Tile):
                if tile.pos == self.pos:
                    sprites.remove(tile)# noqa

    def preview_col(self, selected_color):
        self.image.fill(selected_color)
        self.rect = self.image.get_rect(center=self.pos)
        self.image.set_alpha(100)


class Tiles:
    def __init__(self):
        self.selected_color = "yellow"
        self.size = Vector2(WIDTH/NUMBER_OF_UNITS, HEIGHT/NUMBER_OF_UNITS)
        self.cords = []
        self.coordinates()
        self.previewer = Tile((0, 0), self.size, self.selected_color)

    def coordinates(self):
        for i in range(1, NUMBER_OF_UNITS+1):
            for j in range(1, NUMBER_OF_UNITS+1):
                self.cords.append(Vector2((self.size.x * i) - (self.size.x/2), (self.size.y * j) - (self.size.y/2)))
                #self.add_tiles()

    def add_tiles(self):
        for i in self.cords:
            sprites.add(Tile(i, self.size, (255, 255, 255)))# noqa

    def paint_tiles(self, mouse_pos):
        self.previewer.preview_col(self.selected_color)
        for i in self.cords:
            if abs(i.x-mouse_pos.x) < self.size.x/2 and abs(i.y-mouse_pos.y) < self.size.y/2:
                self.previewer.pos = i
                if pygame.mouse.get_pressed()[0]:
                    sprites.add(Tile(i, self.size, self.selected_color))# noqa

