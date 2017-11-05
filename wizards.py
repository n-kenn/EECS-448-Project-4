import sys
import os
from random import randint
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

ground = Ground(pg.image.load(os.path.join('images', 'ground.png')),
                (display.get_rect().left, height / 2))

players = [
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')),
           (0, 0, 32, 32), 10, ground.rect.topleft, 10),
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')),
           (0, 0, 32, 32), 10, ground.rect.midtop, 10)
]

game_handler = Turn_Handler(players)

fallables = pg.sprite.Group(players)
statics = pg.sprite.Group(ground)

world = World(pg.image.load(os.path.join(
    'images', 'sky.png')).convert(), ground, 5)


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            game_handler.active_player.check_keys(pg.key.get_pressed())
            if event.key == pg.K_RETURN:
                game_handler.switch_turns()
                fallables.add(Explosive((16, 16), (randint(
                    0, display.get_width()), 0), pg.Color('green'), [ground]))
        elif event.type is pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                game_handler.active_player.vel.x = 0


if __name__ == '__main__':
    while True:
        check_keys()
        display.blit(world.image, display.get_rect().topleft)
        fallables.update(world)
        statics.update()
        fallables.draw(display)
        game_handler.active_player.rect.clamp_ip(world.rect)
        statics.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
