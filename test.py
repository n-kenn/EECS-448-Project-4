import pygame as pg
import sys
import os

from explosive import Explosive
from game_handler import Game_Handler
from ground import Ground
from player import Player
from world import World
#Define World As Per Usual
width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()

world = World(pg.image.load(os.path.join('images', 'sky.png')).convert(), Ground(pg.image.load(
    os.path.join('images', 'ground.png')).convert_alpha(), (display.get_rect().left, height / 2)), 0.1)

statics = pg.sprite.LayeredUpdates(world)
fallables = pg.sprite.LayeredUpdates()

players = [Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
         world.ground.rect.midtop, fallables), None] #Breaks when less than two values are created.
game_handler = Game_Handler(players)

#World is Instantiated, now let's say some things about it.
print "Player Object is Able to be Instantiated. ",
try:
    game_handler.players.index(Player)
except:
    print "False"
#TODO: MAKE TEST FOR MOVEMENT!
print "Player is Able to Move from original position."
try:
    pos = game_handler.active_player.rect.x
except:
    pass
def check_keys():
    active_player = game_handler.active_player
    active_player.check_keys(pg.key.get_pressed())
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        '''elif event.type is pg.MOUSEBUTTONDOWN:
            active_player.fire(pg.mouse.get_pos(), [
                               world.ground, game_handler.inactive_player])
            active_player = game_handler.switch_turns()
        '''
if __name__ == '__main__':
    while True:
        check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
