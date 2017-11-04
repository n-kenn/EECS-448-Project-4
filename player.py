from pygame import mask
from animated_sprite import Animated_Sprite


class Player(Animated_Sprite):
    """ Player class that the user will control.
    """
    def __init__(self, file_name, size, frame_rate, start_pos):
        """ Initialize the player sprite.
        :param file_name: The file to be used for the picture of the sprite.
        :param size: The size of the player character.
        :param frame_rate: The frame rate for the particular player character.
        :param start_pos: Starting position for the Player.
        """
        super(Player, self).__init__(file_name, size, frame_rate)
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(bottomleft=start_pos)

    def update(self, world):
        """ Update the Player
        :param world: The world the player inhabits.
        """
        super(Player, self).update()
