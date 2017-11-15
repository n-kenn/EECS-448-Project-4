from os import path
from sys import exit

import pygame as pg

from game_handler import Game_Handler
from player import Player
from world import World

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

world = World(pg.image.load(path.join('images', 'sky.png')).convert(),
              pg.image.load(path.join('images', 'ground.png')).convert_alpha())

statics = pg.sprite.GroupSingle(world)
fallables = pg.sprite.Group()

handler = Game_Handler([Player(pg.image.load(path.join('sprite_sheets', 'wizard.png')).convert_alpha(), start_loc, fallables)
                        for start_loc in world.start_locs])


def check_keys():
    handler.active.check_keys(pg.key.get_pressed(), world.ground)
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            handler.active.fire(pg.mouse.get_pos(), [
                                world.ground, handler.inactive])


if __name__ == '__main__':
    while True:
        check_keys()
        statics.update()
        fallables.update(world)
        statics.draw(display)
        fallables.draw(display)
        if handler.game_over():
            text = pg.font.Font(path.join('font', 'kindergarten.ttf'), 64).render(
                handler.winner, False, pg.Color('yellow'))
            display.blit(text, text.get_rect(
                center=(map(lambda x: x / 2, display.get_size()))))
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(60)
