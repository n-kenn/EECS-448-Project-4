from operator import sub

from pygame.draw import ellipse

from explosive import Explosive


class Beam_Shot(Explosive):
    """A class for any weapon that has the ability to explode.

    :param anim: The sprite sheet to use for animating.
    :param start_pos: Will get passed to projectile.
    :param angle: Will get passed to projectile.
    :param collidables: Sprites that the Beam_Shot can collide with.
    """

    def __init__(self, anim, start_pos, angle, collidables, power, damage, radius):
        super(Beam_Shot, self).__init__(anim, start_pos, angle, collidables, power, damage, radius)


    def update(self, world):
        self.rect.move_ip(self.vel)
        if not world.rect.contains(self.rect):
            self.kill()
        self.active_timer -= 1
        if self.active_timer <= 0:
            self.collision_check()
