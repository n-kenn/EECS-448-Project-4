from pygame.sprite import Group


class Team(Group):
    def __init__(self, name, members):
        super(Team, self).__init__(members)
        self.name = name
