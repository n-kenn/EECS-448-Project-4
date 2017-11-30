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

num_members = 2
font = pg.font.Font(join('font', 'kindergarten.ttf'), 64)
game = Game(images, num_members, font)


class Test(object):
    def test_game_process_input(self):
        assert hasattr(game, 'process_input')

    def test_game_update(self):
        assert hasattr(game, 'update')

    def test_game_over_init(self):
        assert game.game_over() is False

    def test_game_next_scene(self):
        assert game.next is game

    def test_team_count(self):
        assert len(game.teams) is 2

    def test_len_team(self):
        for i, team in enumerate(game.teams):
            assert len(team) is num_members

    def test_team_names(self):
        assert game.teams[0].name is 'Wizards' and game.teams[1].name is 'Clowns'
