import sys
import pygame as pg
from ground import Ground
from player import Player
from projectile import Projectile

width, height = 1024, 512
FPS = 30

# dict for color rgb values
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0 , 0)
}
# dict for world constants
world = {
    'gravity': 1
}

pg.init()
display = pg.display.set_mode((width, height))
pg.display.set_caption('Wizards')
clock = pg.time.Clock()

ground = Ground((width, 20), colors['white'])
player = Player((25, 25), colors['red'], world['gravity'])
has_clicked = False
# make a sprite group
sprites = pg.sprite.Group(ground, player)

def quit_check():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

while True:
    quit_check()
    display.fill(colors['black'])
    if (pg.mouse.get_pressed() == (True,False,False) and has_clicked == False):
        proj = Projectile(player, world['gravity'])
        sprites.add(proj)
        has_clicked = True
    # get_rect will draw from the top-left corner of the rect
    sprites.draw(display)
    # need to move this if statement somewhere else
    if player.rect.colliderect(ground.rect) and player.in_air:
        player.land()
    # call the update method on all sprites in the group
    sprites.update()
    pg.display.update()
    # force the program to run at 60 frames per second
    clock.tick(FPS)
