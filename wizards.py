import sys
import math
import pygame as pg
from ground import Ground
from player import Player
from projectile import Projectile

width, height = 1024, 512
FPS = 60

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
proj = 0
fired = False
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
    #This checks to see if the left mous button is pressed
    #It then calculates the angle and power of the shot and updates player accordingly
    #Then it creates a new projectile, and adds it to the sprites group
    for event in pg.event.get():
        print(event)
    if (pg.mouse.get_pressed() == (True,False,False) and fired == False):
        (m_x,m_y) = pg.mouse.get_pos()
        x_dist = (m_x-player.rect.x)
        y_dist = (player.rect.y-m_y)
        angle = math.degrees(math.atan2(y_dist,x_dist))
        p_num = pow((pow(x_dist,2) + pow(y_dist,2)),(1.0/2.0))
        p_den = pow((pow(width,2) + pow(height,2)),(1.0/2.0))
        power = (1.25) * p_num / p_den * 50.0
        print (power)
        player.set_angle(angle)
        player.set_power(power)
        proj = Projectile(player, world['gravity'])
        sprites.add(proj)
        fired = True


    #If a projectile has been fired, this checks to see if the projectile should still exist.
    #If not, this deletes it
    if(fired):
        delete_proj = False
        if (not(proj.alive()) or proj.rect.colliderect(ground.rect)):
            delete_proj = True
            if (delete_proj):
                del proj
                fired = False




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
