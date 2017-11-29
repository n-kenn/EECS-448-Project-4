from operator import sub

from pygame.draw import ellipse

from projectile import Projectile


class Explosive(Projectile):
    """A class for any weapon that has the ability to explode.

    :param anim: The sprite sheet to use for animating.
    :param start_pos: Will get passed to projectile.
    :param angle: Will get passed to projectile.
    :param collidables: Sprites that the Explosive can collide with.
    """

    def __init__(self, anim, start_pos, angle, collidables, power, damage, radius):
        super(Explosive, self).__init__(anim, start_pos, angle, power)
        self.collidables = collidables
        self.damage = damage
        self.explosion_radius = radius

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
                        ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(map(
                            lambda x: x * self.explosion_radius, self.image.get_size())).move(0, self.image.get_rect().centery - collidable.rect.height))
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
