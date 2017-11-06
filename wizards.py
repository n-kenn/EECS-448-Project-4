import sys
import os
import pygame as pg
from explosive import Explosive
from turn_handler import Turn_Handler
from ground import Ground
from player import Player
from world import World


width, height = 1024, 512
FPS = 60

pg.init()
display = pg.display.set_mode((width, height))
clock = pg.time.Clock()
game_over = False
world = World(pg.image.load(os.path.join('images', 'sky.png')).convert(), Ground(pg.image.load(
    os.path.join('images', 'ground.png')).convert_alpha(), (display.get_rect().left, height / 2)), 0.1)

players = [
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.topleft),
    Player(pg.image.load(os.path.join('sprite_sheets', 'wizard.png')).convert_alpha(),
           (0, 0, 32, 32), 5, world.ground.rect.topright)
]

turn_handler = Turn_Handler(players)

fallables = pg.sprite.Group(players)
statics = pg.sprite.Group(world)


def check_keys():
    active_player = turn_handler.active_player
    active_player.check_keys(pg.key.get_pressed())
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type is pg.MOUSEBUTTONDOWN:
            active_player.fire(pg.mouse.get_pos(), [
                               world.ground, turn_handler.inactive_player])
            active_player = turn_handler.switch_turns()

def check_players():
    for i in range(0,2):
        if (not players[i].alive()):
            fon = pg.font.SysFont("comicsansms",40)
            victor = "Player 1 wins" if i == 1 else "Player 2 wins"
            display.blit(fon.render(victor, 0, pg.Color('black')),(10,10))
            return True
    return False


if __name__ == '__main__':
    while True:
        if not game_over:
            check_keys()
        fallables.update(world)
        statics.update()
        statics.draw(display)
        fallables.draw(display)
        if not game_over:
            game_over = check_players()
        pg.display.update()
        pg.display.set_caption('Wizards {:.2f}'.format(clock.get_fps()))
        clock.tick(FPS)
