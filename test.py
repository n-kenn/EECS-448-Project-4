from os.path import join

import pygame as pg

from game import Game

from player import Player

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
    """The single click test suite.
    """

    def test_game_process_input(self):
        """Tests to see if the game can process events.
        """
        assert hasattr(game, 'process_input')

    def test_game_update(self):
        """Tests to see if the game can update.
        """
        assert hasattr(game, 'update')

    def test_game_over_init(self):
        """ Tests to make sure the game isn't over by default.
        """
        assert game.game_over() is False

    def test_game_next_scene(self):
        """ Tests to see if the game can move from the title screen.
        """
        assert game.next is game

    def test_team_names(self):
        """ Checks the name of the teams.
        """
        assert game.teams[0].name is 'Wizards' and game.teams[1].name is 'Clowns'

    def test_team_count(self):
        """ Checks to see if there are only two teams.
        """
        assert len(game.teams) is 2

    def test_len_team(self):
        """ Tests to see if the length of each team is two.
        """
        for i, team in enumerate(game.teams):
            assert len(team) is num_members

    def test_len_collidables(self):
        """ Tests to see if the ground and every player are added to the list of collidables
        """
        assert len(game.collidables()) is (2 * num_members) + 1

    def test_switch_turns(self):
        """ Checks to see if teams can switch turns.
        """
        game.switch_turns()
        assert game.teams[0].name is 'Clowns' and game.teams[1].name is 'Wizards'

    def test_cycling(self):
        """ Checks to see which team is active after a rotation.
        """
        assert game.teams[0].active is not game.teams[0].cycler.next()

    def test_kill_team(self):
        """ Checks to see if the game is over when a team is empty.
        """
        for member in game.teams[0]:
            member.kill()
        game.update_teams()
        assert len(game.teams) is 1 and game.game_over()

    def test_other_team(self):
        """ Checks to make sure the other team is still alive.
        """
        assert len(game.teams[0]) is num_members

    def test_damage(self):
        """ Tests to see if a player can die from the take damage method.
        """
        game.teams[0].active.apply_damage(game.teams[0].active.rect.width)
        game.teams[0].next()
        assert len(game.teams[0]) is 1 and game.teams[0].active

    def test_game_input_quit(self):
        """ Tests to see if the game can quit.
        """
        game.process_input([pg.event.Event(pg.QUIT)])
        assert game.next is None

    def test_game_mouse_button_down(self):
        """ Tests to see if a projectile is made from pressing down on the mouse.
        """
        game.process_input([pg.event.Event(pg.MOUSEBUTTONDOWN, pos=(0, 0))])
        assert game.teams[0].active.projectile

    def test_player_collision(self):
        """ Checks to see if the player can collide with a projectile.
        """
        game.process_input([pg.event.Event(pg.MOUSEBUTTONDOWN, pos=(game.teams[0].active.get))])
        game.teams[0].active

