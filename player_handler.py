from itertools import cycle

from pygame.sprite import Group

from player import Player


class Player_Handler:
    """Handles players in the game.

    :param p_sheet: spritesheet to use for the player.
    """

    def __init__(self, player_ss, start_locs):
        self.players = Group(Player(player_ss, loc) for loc in start_locs)
        self.player_cycler = cycle(self.players)
        self.active = self.player_cycler.next()

    def draw_players(self, surf):
        """Draws players to the display using the sprites' image and rect.
        :param surf: Surface to draw to.
        """
        self.players.draw(surf)

    def game_over(self):
        """Returns true when one player remains in the players sprite group.
        """
        return len(self.players) is 1

    def switch_turns(self):
        """When a player's actions are done, switch active player.
        """
        self.active = self.player_cycler.next()

    def update(self, world):
        self.players.update(world)
