import sys
import pygame as pg
from ground import Ground
from player import Player

width, height = 1024, 512
FPS = 60

# dict for color rgb values
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0)
}
# dict for world constants
world = {
    'gravity': 2
}

pg.init()
display = pg.display.set_mode((width, height))
pg.display.set_caption('Wizards')
clock = pg.time.Clock()

ground = Ground((width, height / 2), colors['white'])
player = Player((height / 8, width / 8), ground.rect.top, colors['red'])

# make a sprite group
sprites = pg.sprite.Group(ground, player)


def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            # move player if key is right or left. may change this later on
            if event.key == pg.K_RIGHT:
                player.move(5, 0)
            elif event.key == pg.K_LEFT:
                player.move(-5, 0)


while True:
    check_keys()
    display.fill(colors['black'])
    # draw will take the sprite's image as surface and it's rect as the position
    sprites.draw(display)
    # call each sprite's update method. currently no sprites do anything with update
    sprites.update()
    pg.display.update()
    # force the program to run at 60 frames per second
    clock.tick(FPS)
