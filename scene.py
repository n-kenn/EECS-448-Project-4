class Scene(object):
    """Class that encompasses a 'mode' of the game.
    """

    def __init__(self):
        self.next = self

    def process_input(self, events, keys):
        """Each scene must define how it processes user input
        
        :param display: The size of the window.
        :param events: The events to be handled.
        :param keys: The list of all keys and whether they are pressed or not.
        """
        raise NotImplementedError

    def update(self):
        """Each scene must define how it updates itself
        """
        raise NotImplementedError

    def switch_scene(self, next):
        """Used to change the current scene to a new one.
        
        :param next: The scene to be swapped with the current scene.
        """
        self.next = next
