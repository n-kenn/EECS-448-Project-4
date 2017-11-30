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


class Test_Game(object):
    def test_game_process_input(self):
        assert hasattr(game, 'process_input')

    def test_game_update(self):
        assert hasattr(game, 'update')

    def test_game_over_init(self):
        assert game.game_over() is False

    def test_game_next_scene(self):
        assert game.next is game

    def test_team_names(self):
        assert game.teams[0].name is 'Wizards' and game.teams[1].name is 'Clowns'

    def test_team_count(self):
        assert len(game.teams) is 2

    def test_len_team(self):
        for i, team in enumerate(game.teams):
            assert len(team) is num_members

    def test_len_collidables(self):
        assert len(game.collidables()) is (2 * num_members) + 1

    def test_switch_turns(self):
        game.switch_turns()
        assert game.teams[0].name is 'Clowns' and game.teams[1].name is 'Wizards'

    def test_cycling(self):
        assert game.teams[0].active is not game.teams[0].cycler.next()

    def test_kill_team(self):
        for member in game.teams[0]:
            member.kill()
        game.update_teams()
        assert len(game.teams) is 1 and game.game_over()

    def test_other_team(self):
        assert len(game.teams[0]) is num_members

    def test_damage(self):
        game.teams[0].active.apply_damage(game.teams[0].active.rect.width)
        game.teams[0].next()
        assert len(game.teams[0]) is 1 and game.teams[0].active

    def test_game_input_quit(self):
        game.process_input([pg.event.Event(pg.QUIT)])
        assert game.next is None

    def test_game_mouse_button_down(self):
        game.process_input([pg.event.Event(pg.MOUSEBUTTONDOWN, pos=(0, 0))])
        assert game.teams[0].active.projectile
