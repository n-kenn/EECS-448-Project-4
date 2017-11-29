from os.path import join

import pygame as pg

from scene_manager import Scene_Manager

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

music = pg.mixer.Sound('music/BadMusic.ogg')
music.set_volume(0.5)
music.play(-1)

images = {
    'sky': pg.image.load(join('images', 'sky.png')).convert(),
    'ground': pg.image.load(join('images', 'ground.png')).convert_alpha(),
    'player_spritesheet': pg.image.load(join('images', 'wizard_spritesheet.png')).convert_alpha()
}

font = pg.font.Font(join('font', 'kindergarten.ttf'), 96)
scene_manager = Scene_Manager(images, font)

if __name__ == '__main__':
    while scene_manager.active_scene is not None:
        scene_manager.update(display, pg.event.get(), pg.key.get_pressed())
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(60)
