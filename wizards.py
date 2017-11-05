import sys
import os
from random import randint
import pygame as pg
from ground import Ground
from world import World
from player import Player
from explosive import Explosive

width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground(os.path.join('images', 'ground.png'), (display.get_rect().left,
                                                       height / 2), pg.Color('white'))

player = Player(os.path.join('sprite_sheets', 'wizard.png'),
                (0, 0, 32, 32), 10, ground.rect.midtop, 10)

fallables = pg.sprite.Group(player)
statics = pg.sprite.Group(ground)

world = World(pg.image.load(os.path.join('images', 'sky.png')), ground, 5)


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            player.check_keys(pg.key.get_pressed())
            if event.key == pg.K_RETURN:
                player.health -= player.image.get_width() / 4
                fallables.add(Explosive((16, 16), (randint(
                    0, display.get_width()), 0), pg.Color('green'), [ground, player]))
        elif event.type is pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player.vel.x = 0


if __name__ == '__main__':
    while True:
        check_keys()
        display.blit(world.image, display.get_rect().topleft)
        fallables.update(world)
        statics.update()
        fallables.draw(display)
        statics.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
