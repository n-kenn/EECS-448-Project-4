from title_screen import Title_Screen


class Scene_Manager(object):
    """Facilitates scene transitions.

    :param images: Dictionary of images that will eventually be used in the Game constructor.
    :param font: Used to construct the title screen's text.
    """

    def __init__(self, images, font):
        self.active_scene = Title_Screen(images, font)

    def update(self, display, events, keys):
        """Called every frame to update self and process user input.

        :param display: The game display.
        :param events: The events to be processed.
        :param keys: The list of keys and whether they are pressed down or not.
        """
        self.active_scene.update(display, events, keys)
        self.active_scene = self.active_scene.next
