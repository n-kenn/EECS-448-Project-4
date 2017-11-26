from title_screen import Title_Screen


class Scene_Manager(object):
    """Facilitates scene transitions.

    :param images: Dictionary of images that will eventually be used in the Game constructor.
    :param font: Used to construct the title screen's text.
    """

    def __init__(self, images, font):
        self.active_scene = Title_Screen(images, ['Start', 'Quit'], font)

    def update(self, display, events, keys):
        """Called every frame to update self and process user input.
        """
        self.active_scene.update(display, events, keys)
        self.active_scene = self.active_scene.next
