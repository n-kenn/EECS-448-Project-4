from title_screen import Title_Screen


class Scene_Manager(object):
    """Facilitates scene transitions.

    :param size: Size of the display to determine how large to make the title screen.
    :param font: Used to construct the title screen's text.
    :param images: "Dictionary of images that will eventually be used in the Game constructor"
    """

    def __init__(self, size, font, images):
        self.active_scene = Title_Screen(size, ['Start', 'Quit'], font, images)

    def update(self, display, events, keys):
        """Called every frame to update self and process user input.
        """
        self.active_scene.update(display,
                                 events,
                                 keys)
        self.active_scene = self.active_scene.next
