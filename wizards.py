import sys
import pygame as pg

width, height = 1024, 512
FPS = 30
black = (0, 0, 0)

pg.init()
display = pg.display.set_mode((width, height))
pg.display.set_caption('Wizards')
clock = pg.time.Clock()


def quitCheck():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


while True:
    quitCheck()
    display.fill(black)
    pg.display.update()
    clock.tick(FPS)
