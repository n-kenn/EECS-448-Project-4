from random import sample

from pygame.key import get_pressed
from pygame.locals import MOUSEBUTTONDOWN, QUIT
from pygame.transform import scale

from player import Player
from scene import Scene
from team import Team
from world import World


class Game(Scene):
    """Scene that implements the actual game.

    :param images: Image surfaces for various things.
    :param num_members: How many sprites are on a team.
    :param font: The font to load up.
    """

    def __init__(self, images, num_members, font):
        super(Game, self).__init__()
        self.world = World(images)
        self.teams = self.make_teams(images, num_members)
        self.font = font
        self.banner = self.make_banner('Go, {}!'.format(
            self.teams[0].name), self.teams[0].color)

    def draw(self, surf):
        """Draws players to the display using the sprites' image and rect.

        :param surf: Surface to draw to.
        """
        self.world.draw(surf)
        for team in self.teams:
            team.draw(surf)
        if not self.game_over():
            surf.blit(self.banner,
                      self.banner.get_rect(midtop=surf.get_rect().midtop))
            power = self.make_banner(str(self.teams[0].active.power),
                                     (255, 0, 255 * self.teams[0].active.power // 50))
            power = scale(power, map(lambda x: x // 4, power.get_size()))
            surf.blit(power,
                      power.get_rect(midtop=self.teams[0].active.rect.midbottom))

    def game_over(self):
        """Returns true when one player remains in the team sprite group.
        """
        return len(self.teams) is 1

    def collidables(self):
        """Adds every sprite to a collidables list.
        """
        temp = [self.world.ground]
        for team in self.teams:
            for sprite in team.sprites():
                temp.append(sprite)
        return temp

    def process_input(self, events):
        """Handles all user input

        :param events: The events to be handled, which in this case correspond to either quit or mousebuttondown
        """
        for event in events:
            if event.type is QUIT:
                self.switch_scene(None)
            elif event.type is MOUSEBUTTONDOWN:
                self.teams[0].active.fire(event.pos, self.collidables())
                self.switch_turns()

    def make_banner(self, text, col):
        """Helper function to render whose turn it is.

        :param text: Text to render.
        :param col: Color to render the font in.
        """
        return self.font.render(text,
                                False,
                                col).convert()

    def make_teams(self, images, num_players):
        """Generates two lists of players for each time based on the quantity of starting locations.

        :param images: Used to get the spritesheet for the players.
        """
        return [Team(name, (156, 68, 108) if name == 'Wizards' else (255, 20, 55), [Player(images['wizard_spritesheet' if name == 'Wizards' else 'clown_spritesheet'], loc)
                                                                                    for loc in sample(self.world.start_locs, num_players)])
                for name in ['Wizards', 'Clowns']]

    def switch_turns(self):
        """When a player's actions are done, switch active player and render new text.
        """
        if not self.game_over():
            self.teams.reverse()
            self.teams[0].next()
            self.banner = self.make_banner('Go {}!'.format(
                self.teams[0].name), self.teams[0].color)

    def update_teams(self):
        """Tells the game to update the conditions of the teams.
        """
        for team in self.teams:
            if team:
                team.update(self.world)
            else:
                self.teams.remove(team)

    def update(self, display, events):
        """Updates self and processes user input.

        :param display: The game display.
        :param events: The events to be handled.
        """
        self.process_input(events)
        self.teams[0].active.check_movement(self.world.ground, get_pressed())
        self.world.update()
        self.update_teams()
        self.draw(display)
        if self.game_over():
            for team in self.teams:
                if team:
                    win = self.make_banner('Winner: {}'.format(team.name),
                                           team.color)
            display.blit(win, win.get_rect(midtop=display.get_rect().midtop))
