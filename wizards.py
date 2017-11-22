from os import path

import pygame as pg

from scene_manager import Scene_Manager

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

images = {
    'sky': pg.image.load(path.join('images', 'sky.png')).convert(),
    'ground': pg.image.load(path.join('images', 'ground.png')).convert_alpha(),
    'player_ss': pg.image.load(path.join('images', 'wizard_ss.png')).convert_alpha()
}

font = pg.font.Font(path.join('font', 'kindergarten.ttf'), 64)
scene_manager = Scene_Manager(display.get_size(), font, images)

if __name__ == '__main__':
    while scene_manager.active_scene is not None:
        scene_manager.update(display, pg.event.get(), pg.key.get_pressed())
        pg.display.update()
        clock.tick(60)
