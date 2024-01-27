import pygame as pg
import pygame.mouse

from pygame import Vector2
from Settings import *
from main import *
from DrawTiles import *

tools = pg.sprite.Group()


class Color(pg.sprite.Sprite):
    def __init__(self, pos, size, color):
        super().__init__()
        self.pos = pos
        self.size = size
        self.color = color

        self.image = pg.Surface((size.x, size.y))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=self.pos)

    def choose_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                return True


class Setup:
    def __init__(self):
        self.num_of_colors = 5
        self.cords_of_colors = []
        self.size = (WIDTH+50)/self.num_of_colors
        self.cords()

    def cords(self):
        for i in range(self.num_of_colors):
            self.cords_of_colors.append((self.size * i + self.size/2, HEIGHT + 25))

        for i, cords in enumerate(self.cords_of_colors):
            tools.add(Color(cords, Vector2(25, 25), COLOR_PALLET[i]))# noqa