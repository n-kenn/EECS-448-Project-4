import sys
import os
from random import randint
import pygame as pg
from ground import Ground
from player import Player
from explosive import Explosive

width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground(os.path.join('world', 'ground.png'), (display.get_rect().left,
                                                      height / 2), pg.Color('white'))

player = Player(os.path.join('sprite_sheets', 'wizard.png'),
                (0, 0, 32, 32), 10, ground.rect.midtop, 10)

player2 = Player(os.path.join('sprite_sheets', 'spiral.png'),
                 (0, 0, 32, 32), 10, ground.rect.topright, 10)

fallables = pg.sprite.Group(player, player2)
statics = pg.sprite.Group(ground)

turn = [True, False]

world = {
    'gravity': 5,
    'ground': ground
}


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            if (turn[1] == True):
                player.check_keys(pg.key.get_pressed())
            else:
                player2.check_keys(pg.key.get_pressed())
            if event.key == pg.K_RETURN:
                turn.reverse()
                fallables.add(Explosive((16, 16), (randint(
                    0, display.get_width()), 0), pg.Color('green'), [ground, player]))
                player.health -= 10
        elif event.type is pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player.vel.x = 0


if __name__ == '__main__':
    while True:
        check_keys()
        display.blit(pg.image.load(os.path.join('world', 'sky.png')), (0, 0))
        fallables.update(world)
        statics.update()
        fallables.draw(display)
        statics.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        if (len(fallables) < 2):
            print "WINNER!"
            pg.time.wait(2000)
            pg.quit()
            sys.exit()
        clock.tick(FPS)
