import sys
import pygame as pg
from ground import Ground
from player import Player
from explosive import Explosive

width, height = 1024, 512
FPS = 60
# dict for world constants
world = {
    'gravity': 2
}

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground((width, height / 2), (display.get_rect().left,
                                      height / 2), pg.Color('white'))
player = Player((height / 8, width / 8), ground.rect.topleft, pg.Color('red'))

# make a sprite group
sprites = pg.sprite.Group(ground, player)


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
                sprites.add(Explosive((32, 32), display.get_rect().midtop,
                                      pg.Color('green'), [ground, player]))
                player.health -= 50


while True:
    check_keys()
    display.fill(pg.Color('black'))
    # presumably we'll want to send the gravity constant to all the sprites
    sprites.update()
    # draw will take the sprite's image as surface and it's rect as the position
    sprites.draw(display)
    pg.display.update()
    # force the program to run at 60 frames per second
    pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
    clock.tick(FPS)
