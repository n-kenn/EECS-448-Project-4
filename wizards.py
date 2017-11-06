import sys
import os
import pygame as pg
from explosive import Explosive
from turn_handler import Turn_Handler
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

players = [
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.topleft, 5),
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.midtop, 5)
]

turn_handler = Turn_Handler(players)

fallables = pg.sprite.Group(players)
statics = pg.sprite.Group(world)


def check_keys():
    active_player = turn_handler.active_player
    for event in pg.event.get():
        active_player.check_keys(pg.key.get_pressed())
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            active_player.fire(pg.mouse.get_pos(), [
                               world.ground, turn_handler.inactive_player])
            active_player = turn_handler.switch_turns()


if __name__ == '__main__':
    while True:
        print fallables
        check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
