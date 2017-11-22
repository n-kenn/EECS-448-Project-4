class Scene(object):
    def __init__(self):
        self.next = self

    def process_input(self, events, keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def switch_scene(self, next):
        self.next = next
