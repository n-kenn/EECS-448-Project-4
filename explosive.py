from operator import sub

from pygame import draw

from projectile import Projectile


class Explosive(Projectile):
    """A class for any weapon that has the ability to explode.

    :param sheet: The file to load for the surface.
    :param start_pos: Will get passed to projectile.
    :param angle: Will get passed to projectile.
    :param collidables: Sprites that the Explosive can collide with.
    :param groups: Groups to add the sprite to.
    """

    def __init__(self, strip, start_pos, angle, collidables, groups):
        super(Explosive, self).__init__(strip, start_pos, angle, groups)
        self.collidables = collidables
        self.damage = 8

    def collision_check(self):
        """Looks to see if the explosive projectile has collided with anything.
            If it has, then remove the projectile, and draw an elipse to represent the blast
            of the explosion.
        """
        for collidable in self.collidables:
            if self.rect.colliderect(collidable.rect):
                if self.mask.overlap(collidable.mask, tuple(map(sub, collidable.rect.topleft, self.rect.topleft))):
                    self.kill()
                    if type(collidable).__name__ is 'Ground':
                        draw.ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(map(
                            lambda x: x * 4, self.image.get_size())).move(0, self.image.get_rect().centery - collidable.rect.height))
                        collidable.update()
                    elif type(collidable).__name__ is 'Player':
                        collidable.apply_damage(self.damage)
                    break

    def update(self, world):
        """Update the explosive weapon.
        :param world: The world in which the explosive exists.
        """
        super(Explosive, self).update(world)
        self.collision_check()
        if not world.rect.contains(self.rect):
            self.kill()
