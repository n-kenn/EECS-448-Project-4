from os import path
from sys import exit

import pygame as pg

from game_handler import Game_Handler
from player import Player
from world import World

pg.init()
display = pg.display.set_mode((1024, 512))

images = {
    'sky': pg.image.load(path.join('images', 'sky.png')).convert(),
    'ground': pg.image.load(path.join('images', 'ground.png')).convert_alpha(),
    'player_ss': pg.image.load(path.join('sprite_sheets', 'wizard.png')).convert_alpha()
}

font = pg.font.Font(path.join('font', 'kindergarten.ttf'), 64)

clock = pg.time.Clock()
world = World(images['sky'], images['ground'])
fallables = pg.sprite.Group()
statics = pg.sprite.GroupSingle(world)
handler = Game_Handler(pg.sprite.Group(
    [Player(images['player_ss'], loc, fallables) for loc in world.start_locs]))


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
        statics.update()
        fallables.update(world)
        statics.draw(display)
        fallables.draw(display)
        if handler.game_over():
            text = font.render(handler.winner, False, pg.Color('yellow'))
            display.blit(text, text.get_rect(
                center=(map(lambda x: x / 2, display.get_size()))))
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(60)
