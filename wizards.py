import sys
import pygame as pg
from ground import Ground
from player import Player
from explosive import Explosive

width, height = 1024, 512
FPS = 60

world = {
    'gravity': 5
}

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground((width, height / 2), (display.get_rect().left, height / 2), pg.Color('white'))
player = Player((height / 16, width / 16), ground.rect.topleft, pg.Color('red'))

fallables = pg.sprite.Group(player)
statics = pg.sprite.Group(ground)


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                player.move(5, 0)
            elif event.key == pg.K_LEFT:
                player.move(-5, 0)
            elif event.key == pg.K_SPACE:
                fallables.add(Explosive((32, 32), display.get_rect().midtop,
                                        pg.Color('green'), [ground, player]))


while True:
    check_keys()
    display.fill(pg.Color('black'))
    statics.update()
    fallables.update(world['gravity'], ground)
    # draw will take the sprite's image as surface and its rect as the position
    fallables.draw(display)
    statics.draw(display)
    pg.display.update()
    pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
    # force the program to run at 60 frames per second
    clock.tick(FPS)
