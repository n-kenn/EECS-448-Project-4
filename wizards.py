from os import path
from sys import exit

import pygame as pg

from handler import Handler
from menu import Menu
from world import World

pg.init()
display = pg.display.set_mode((1024, 512))

images = {
    'sky': pg.image.load(path.join('images', 'sky.png')).convert(),
    'ground': pg.image.load(path.join('images', 'ground.png')).convert_alpha(),
    'player_ss': pg.image.load(path.join('images', 'wizard_ss.png')).convert_alpha()
}

font = pg.font.Font(path.join('font', 'kindergarten.ttf'), 64)
clock = pg.time.Clock()
handler = Handler(images['player_ss'], World(images['sky'], images['ground']))


def run(mode):
    def wrapper(*args, **kwargs):
        get_events()
        return mode(*args, **kwargs)
    return wrapper


@run
def play():
    handler.update(pg.key.get_pressed())
    handler.draw(display)
# text = font.render('Winner: ' + handler.active.name,
#                    False,
#                    pg.Color('yellow'))
# display.blit(text, text.get_rect(center=(display.get_rect().center)))


menu = Menu(pg.Surface(display.get_size()), ['Start', 'Quit'], font)


def get_events():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            handler.active.fire(pg.mouse.get_pos(),
                                handler.players.sprites() + [handler.world.ground])
            handler.switch_turns()


if __name__ == '__main__':
    while not handler.game_over():
        play()
        pg.display.update()
        clock.tick(60)
