import sys
import pygame as pg
from ground import Ground

width, height = 1024, 512
FPS = 30
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

pg.init()
display = pg.display.set_mode((width, height))
pg.display.set_caption('Wizards')
clock = pg.time.Clock()


def quit_check():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


while True:
    quit_check()
    display.fill(colors['black'])
    ground = Ground((width, height / 2), colors['white'])
    display.blit(ground.image, ground.image.get_rect())
    ground.update()
    pg.display.update()
    clock.tick(FPS)
