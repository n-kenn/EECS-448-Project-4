import os
import sys

import pygame as pg

from explosive import Explosive
from game_handler import Game_Handler
from ground import Ground
from player import Player
from world import World

width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

world = World(pg.image.load(os.path.join('images', 'sky.png')).convert(),
              pg.image.load(os.path.join('images', 'ground.png')).convert_alpha(), 0.1)

statics = pg.sprite.Group(world)
fallables = pg.sprite.Group()

handler = Game_Handler([Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(), start_pos, fallables)
                        for start_pos in world.start_positions])


def check_keys():
    handler.active.check_keys(pg.key.get_pressed())
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            handler.active.fire(pg.mouse.get_pos(), [
                world.ground, handler.inactive])


if __name__ == '__main__':
    while True:
        print len(fallables)
        check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        if handler.game_over():
            text = pg.font.Font(os.path.join('font', 'kindergarten.ttf'), 64).render(
                handler.winner, False, pg.Color('yellow'))
            display.blit(text, text.get_rect(center=(width / 2, height / 2)))
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
