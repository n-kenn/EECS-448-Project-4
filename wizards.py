from os import path
from sys import exit

import pygame as pg

from handler import Handler
from menu import Menu
from world import World

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

images = {
    'sky': pg.image.load(path.join('images', 'sky.png')).convert(),
    'ground': pg.image.load(path.join('images', 'ground.png')).convert_alpha(),
    'player_ss': pg.image.load(path.join('images', 'wizard_ss.png')).convert_alpha()
}

font = pg.font.Font(path.join('font', 'kindergarten.ttf'), 64)
handler = Handler(images['player_ss'], World(images['sky'], images['ground']))
menu = Menu(pg.Surface(display.get_size()), ['Start', 'Quit'], font)


def quit():
    pg.quit()
    exit()


if __name__ == '__main__':
    while True:
        menu.update(display, pg.event.get(), quit)
        pg.display.update()
        clock.tick(60)
