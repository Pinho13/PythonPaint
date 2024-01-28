import pygame as pg
import sys

import pygame.sprite

from Settings import *
from pygame import Vector2
from DrawTiles import *
from Tools import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH + 50, HEIGHT + 50))
        pg.display.set_caption("Python Paint")
        self.mouse_pos = Vector2(pg.mouse.get_pos())
        self.delta_time = 0
        self.tiles = Tiles()
        self.tools = Setup()
        self.background = pg.Surface(RES, pygame.SRCALPHA)
        self.background.get_rect(center=(WIDTH/2, HEIGHT/2))

    @staticmethod
    def check_events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.delta_time = pg.time.Clock().tick(60) / 1000
        self.mouse_pos = Vector2(pg.mouse.get_pos())
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.background, (0, 0))
        sprites.draw(self.background)
        tools.draw(self.screen)
        self.tiles.paint_tiles(self.mouse_pos, self.redraw_background, self.background)
        self.screen.blit(self.tiles.previewer.image, self.tiles.previewer.rect)
        for tool in tools:
            if isinstance(tool, Color):
                if tool.choose_color(self.mouse_pos):
                    self.tiles.selected_color = tool.color
            if isinstance(tool, Tool):
                tool.tool_use(self.mouse_pos, self.background, self.tiles)
        pg.display.update()

    def redraw_background(self):
        self.background = pg.Surface(RES, pygame.SRCALPHA)

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
