from os.path import join

import pygame as pg

from scene_manager import Scene_Manager

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

music = pg.mixer.Sound(join('music', 'BadMusic.ogg'))
music.set_volume(0.5)
music.play(-1)

images = {
    'sky': pg.image.load(join('images', 'sky.png')).convert(),
    'ground': pg.image.load(join('images', 'ground.png')).convert_alpha(),
    'wizard_spritesheet': pg.image.load(join('images', 'wizard_spritesheet.png')).convert_alpha(),
    'clown_spritesheet': pg.image.load(join('images', 'clown_spritesheet.png')).convert_alpha()
}

font = pg.font.Font(join('font', 'kindergarten.ttf'), 64)
scene_manager = Scene_Manager(images, font)

if __name__ == '__main__':
    while scene_manager.scene is not None:
        scene_manager.update(display, pg.event.get())
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(60)
