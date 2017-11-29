from itertools import cycle

from pygame.sprite import Group


class Team(Group):
    def __init__(self, name, members):
        super(Team, self).__init__(members)
        self.name = name
        self.reset_cycle()

    def next(self):
        self.active = self.cycler.next()

    def reset_cycle(self):
        self.cycler = cycle(self)
        self.next()
