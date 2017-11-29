from os.path import join
import pygame as pg

from game import Game

pg.init()
display = pg.display.set_mode((1024, 512))
clock = pg.time.Clock()

images = {
    'sky': pg.image.load(join('images', 'sky.png')).convert(),
    'ground': pg.image.load(join('images', 'ground.png')).convert_alpha(),
    'wizard_spritesheet': pg.image.load(join('images', 'wizard_spritesheet.png')).convert_alpha(),
    'clown_spritesheet': pg.image.load(join('images', 'clown_spritesheet.png')).convert_alpha()
}

font = pg.font.Font(join('font', 'kindergarten.ttf'), 128)

num_players = 2
team_names = ['Wizards', 'Clowns']
game = Game(images, num_players, font)

if __name__ == '__main__':
    assert hasattr(game, 'process_input') and hasattr(game, 'update'), 'Game does not have a required scene attribute.'
    assert game.game_over() is False, 'Game over from the beginning.'
    assert game.next is game, 'Next scene is self.'
    assert len(game.teams) is 2, 'Number of teams is not 2 upon game creation.'
    for i, team in enumerate(game.teams):
        assert len(team) is num_players, 'Members on team is not equal to num_players.'
        assert game.teams[i].name is team_names[i], 'Turn order not initialized correctly'
