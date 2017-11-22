from title_screen import Title_Screen


class Scene_Manager(object):
    def __init__(self, size, font, images):
        self.active_scene = Title_Screen(size, ['Start'], font, images)

    def update(self, display, events, keys):
        print self.active_scene
        self.active_scene.update(display,
                                 events,
                                 keys)
        self.active_scene = self.active_scene.next
