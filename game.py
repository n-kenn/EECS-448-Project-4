from random import sample

from pygame.key import get_pressed
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from player import Player
from scene import Scene
from team import Team
from world import World


class Game(Scene):
    """Scene that implements the actual game.

    :param images: Image surfaces for various things.
    :param font: The font to load up.
    """

    def __init__(self, images, font):
        super(Game, self).__init__()
        self.world = World(images)
        self.teams = self.make_teams(images)
        self.font = font
        self.wiz_col, self.clown_col = (156, 68, 108), (255, 20, 55)
        self.banner = self.make_banner()

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

    def game_over(self):
        """Returns true when one player remains in the team sprite group.
        """
        return not len(self.teams[1])

    def collidables(self):
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

    def make_banner(self):
        """Helper function to render whose turn it is.
        """
        return self.font.render('Go, {}!'.format(self.teams[0].name),
                                False,
                                self.wiz_col if self.teams[0].name is 'Wizards' else self.clown_col).convert()

    def make_teams(self, images):
        return [Team(name, [Player(images['wizard_spritesheet' if name == 'Wizards' else 'clown_spritesheet'], loc) for loc in sample(self.world.start_locs, 2)]) for name in ['Wizards', 'Clowns']]

    def switch_turns(self):
        """When a player's actions are done, switch active player and render new text.
        """
        if not self.game_over():
            self.teams.reverse()
            self.teams[0].next()
            self.banner = self.make_banner()

    def update_teams(self):
        for team in self.teams:
            team.update(self.world)

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
            win = self.font.render('Winner: {}'.format(self.teams[0].name),
                                   False,
                                   self.wiz_col if self.teams[0].name is 'Wizards' else self.clown_col).convert()
            display.blit(win, win.get_rect(center=display.get_rect().center))
