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


class Tool(pg.sprite.Sprite):
    def __init__(self, pos, size, tool_type, image):
        super().__init__()
        self.pos = pos
        self.size = size

        self.image = pygame.image.load(image).convert()
        self.image = pg.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=self.pos)

        self.tool_type = tool_type
        self.can_click_to_change = True

    def tool_use(self, mouse_pos, surf, tiles):
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                match self.tool_type:
                    case 0:
                        self.change_pen("pen", tiles)
                    case 1:
                        self.change_pen("rubber", tiles)
                    case 2:
                        self.save(surf)
                    case 3:
                        self.change_pensize(True, tiles)
                    case 4:
                        self.change_pensize(False, tiles)

    @staticmethod
    def change_pen(pen, tiles):
        tiles.pen_type = pen

    @staticmethod
    def save(surf):
        name = input("Name: ")
        pg.image.save(surf, name + ".png")

    def change_pensize(self, change, tiles):
        if self.can_click_to_change:
            if change:
                tiles.pen_size += 1
            elif tiles.pen_size > 1:
                tiles.pen_size -= 1
            self.can_click_to_change = False


class Setup:
    def __init__(self):
        self.num_of_colors = len(COLOR_PALLET)
        self.num_of_tools = len(UI_IMAGES)
        self.cords_of_colors = []
        self.cords_of_tools = []
        self.size = Vector2((WIDTH+50)/self.num_of_colors, HEIGHT/self.num_of_tools)
        self.cords()

    def cords(self):
        for i in range(self.num_of_colors):
            self.cords_of_colors.append((self.size.x * i + self.size.x/2, HEIGHT + 25))

        for i in range(self.num_of_tools):
            self.cords_of_tools.append((WIDTH + 25, self.size.y * i + self.size.y/2))

        for i, cords in enumerate(self.cords_of_colors):
            tools.add(Color(cords, Vector2(25, 25), COLOR_PALLET[i]))# noqa

        for i, cord in enumerate(self.cords_of_tools):
            tools.add(Tool(cord, Vector2(35, 35), i, UI_IMAGES[i]))# noqa