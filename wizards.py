import sys
import os
import pygame as pg
from ground import Ground
from player import Player
from explosive import Explosive

width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground(os.path.join('world', 'ground.png'), (display.get_rect().left,
                                                      height / 2), pg.Color('white'))

player = Player(os.path.join('sprite_sheets', 'spiral.png'),
                (0, 0, 32, 32), 10, ground.rect.topleft)

fallables = pg.sprite.Group(player)
statics = pg.sprite.Group(ground)

world = {
    'gravity': 5,
    'ground': ground
}


def quit_check():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.KEYDOWN:
            player.check_keys(pg.key.get_pressed())
        elif event.type is pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player.vel.x = 0
            # fallables.add(Explosive((32, 32), display.get_rect().midtop, pg.Color('green'), [ground, player]))


if __name__ == '__main__':
    while True:
        quit_check()
        display.blit(pg.image.load(os.path.join('world', 'sky.png')), (0, 0))
        fallables.update(world)
        statics.update()
        fallables.draw(display)
        statics.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
