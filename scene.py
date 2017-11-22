class Scene(object):
    """Class that encompasses a 'mode' of the game.
    """

    def __init__(self):
        self.next = self

    def process_input(self, events, keys):
        """Each scene must define how it processes user input
        """
        raise NotImplementedError

    def update(self):
        """Each scene must define how it updates itself
        """
        raise NotImplementedError

    def switch_scene(self, next):
        """Used to change the current scene to a new one.
        """
        self.next = next
