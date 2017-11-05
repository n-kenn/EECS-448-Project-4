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
    os.path.join('images', 'ground.png')).convert_alpha(), (display.get_rect().left, height / 2)), 5)

players = [
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.topleft, 10),
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.midtop, 10)
]

turn_handler = Turn_Handler(players)

fallables = pg.sprite.Group(players)
statics = pg.sprite.Group(world)


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            turn_handler.active_player.check_keys(pg.key.get_pressed())
            if event.key == pg.K_RETURN:
                Explosive((16, 16), turn_handler.active_player.angle, turn_handler.active_player.rect.topright if turn_handler.active_player.angle <
                          90 else turn_handler.active_player.rect.topleft, pg.Color('green'), fallables)
                turn_handler.switch_turns()
        elif event.type is pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                turn_handler.active_player.vel.x = 0


if __name__ == '__main__':
    while True:
        check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
