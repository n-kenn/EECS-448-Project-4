import sys
import math
import pygame as pg
from ground import Ground
from player import Player
from explosive import Explosive


width, height = 1024, 512
FPS = 60
# dict for color rgb values
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (40,230,40)
}
# dict for world constants
world = {
    'gravity': 0.0981
}

pg.init()
pg.event.set_blocked((3,4,6))
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

ground = Ground((width, 20), colors['white'], (0,height-20))
wall = Ground((20,height-20),colors['white'],(width-20,0))
target = Ground((30,30), colors['green'], (width-(0.1*width),height/2))
player = Player((25, 25),ground.rect.top, colors['red'], world['gravity'])
proj = 0
fired = False
# make a sprite group
sprites = pg.sprite.Group(ground, player, wall, target)
player.set_collidables(sprites)

def check_keys():
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
    # move player if key is right or left. may change this later on
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        player.player_move(-1, 0)
    elif keys[pg.K_d]:
        player.player_move(1, 0)



while True:
    check_keys()
    display.fill(pg.Color('black'))
    # presumably we'll want to send the gravity constant to all the sprites
    sprites.update()
    # draw will take the sprite's image as surface and it's rect as the position
    sprites.draw(display)
    display.fill(colors['black'])


    #This checks to see if the left mous button is pressed
    #It then calculates the angle and power of the shot and updates player accordingly
    #Then it creates a new projectile, and adds it to the sprites group

    if (pg.mouse.get_pressed() == (True,False,False) and fired == False):
        (m_x,m_y) = pg.mouse.get_pos()
        x_dist = (m_x-player.rect.x)
        y_dist = (player.rect.y-m_y)
        player.set_angle((x_dist,y_dist))

        proj = player.fire()
        sprites.add(proj)
        fired = True


    #If a projectile has been fired, this checks to see if the projectile should still exist.
    #If not, this deletes it
    if(fired):
        if (not(proj.alive())):
            del proj
            fired = False




    # get_rect will draw from the top-left corner of the rect
    sprites.draw(display)
    # call each sprite's update method. currently no sprites do anything with update
    sprites.update()

    pg.display.update()
    # force the program to run at 60 frames per second
    pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
    clock.tick(FPS)
