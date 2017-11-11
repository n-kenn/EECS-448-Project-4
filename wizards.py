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


world = World(pg.image.load(os.path.join('images', 'sky.png')).convert(), Ground(pg.image.load(
    os.path.join('images', 'ground.png')).convert_alpha(), (display.get_rect().left, height / 2)), 0.1)

statics = pg.sprite.LayeredUpdates(world)
fallables = pg.sprite.LayeredUpdates()

players = [Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(), start_pos, fallables)
    for start_pos in world.start_positions]

game_handler = Game_Handler(players)

def check_keys():
    active = game_handler.active
    active.check_keys(pg.key.get_pressed())
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            active.fire(pg.mouse.get_pos(), [
                world.ground, game_handler.inactive])
            game_handler.switch_turns()


if __name__ == '__main__':
    while True:
        check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        if game_handler.game_over():
            text = pg.font.Font(os.path.join('font', 'kindergarten.ttf'), 64).render(
                game_handler.winner, False, pg.Color('yellow'))
            display.blit(text, text.get_rect(center=(width / 2, height / 2)))
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
