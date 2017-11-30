from itertools import cycle

from pygame.sprite import Group


class Team(Group):
    """Defines a type team for which players will belong to. This class helps with the cycling
    of turns, and determining the winner.

    :param name: Name of the team.
    :param color: Color of the team text.
    :param members: The players.
    """

    def __init__(self, name, color, members):
        super(Team, self).__init__(members)
        self.name = name
        self.color = color
        self.reset_cycle()
        self.curr_len = len(self)

    def next(self):
        """Sets the next player to take a turn.
        """
        self.active = self.cycler.next()

    def reset_cycle(self):
        """Begins the cycling process. (Used especially when a player dies so that the game will not get stuck.)
        """
        self.cycler = cycle(self.sprites())
        try:
            self.next()
        except StopIteration:
            pass

    def update(self, world):
        """Updates the sprites in the group and checks if the group length has changed.

        :param world: Reference to world.
        """
        for sprite in self.sprites():
            sprite.update(world)
        if len(self) is not self.curr_len:
            self.curr_len = len(self)
            self.reset_cycle()
