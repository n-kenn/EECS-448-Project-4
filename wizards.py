from os import path
from sys import exit

import pygame as pg

from player_handler import Player_Handler
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
world = World(images['sky'], images['ground'])
handler = Player_Handler(images['player_ss'], world.start_locs)


def get_events():
    handler.active.check_keys(pg.key.get_pressed(), world.ground)
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            handler.active.fire(pg.mouse.get_pos(),
                                handler.players.sprites() + [world.ground])
            handler.switch_turns()


if __name__ == '__main__':
    while True:
        get_events()
        world.update()
        handler.update(world)
        world.draw(display)
        handler.draw_players(display)
        if handler.game_over():
            text = font.render('Winner: ' + handler.active.name,
                               False,
                               pg.Color('yellow'))
            display.blit(text,
                         text.get_rect(center=(display.get_rect().center)))
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(60)
