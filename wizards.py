import sys
import pygame as pg
from ground import Ground

width, height = 1024, 512
FPS = 30
# dictionary for color rgb values
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

pg.init()
display = pg.display.set_mode((width, height))
pg.display.set_caption('Wizards')
clock = pg.time.Clock()

ground = Ground((width, height / 2), colors['white'])
# make a sprite group
objects = pg.sprite.Group(ground)


def quit_check():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


while True:
    quit_check()
    display.fill(colors['black'])
    # get_rect will draw from the top-left corner of the rect
    display.blit(ground.image, ground.image.get_rect())
    # call the update method on all sprites in the group
    objects.update()
    pg.display.update()
    # force the program to run at 30 frames per second
    clock.tick(FPS)
