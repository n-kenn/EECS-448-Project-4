from pygame import draw, sprite
from projectile import Projectile


class Explosive(Projectile):
    """ A class for any weapon that has the ability to explode.
    """

    def __init__(self, file_name, rect, frame_rate, angle, pos, groups, power, damage, collidables):
        """Initialize the Explosive weapon.
            :param file_name: The file to load for the surface.
            :param rect: The size of the explosive weapon.
            :param frame_rate: The frame rate to play the animation at.
            "param" angle: Will get passed to projectile.
            :param pos: The position of the explosive weapon.
            :param groups: A sprite.Group of all player objects.
            :param power: The launch power of the explosive weapon.
            :param damage: The amount of damage the explosive does to a player
            :collidables: Sprites that the Explosive can collide with
        """
        super(Explosive, self).__init__(file_name, rect,
                                        frame_rate, angle, pos, power, groups)
        self.collidables = collidables
        self.damage = damage

    def collision_check(self):
        """ Looks to see if the explosive projectile has collided with anything.
            If it has, then remove the projectile, and draw an elipse to represent the blast
            of the explosion.

        :param collidables: The objects that an explosion can collide with.
        """
        # this will probably get refactored somehow.
        for collidable in self.collidables:
            # check for rectangular collision
            if (self.rect.colliderect(collidable.rect) and collidable):
                # then check for per pixel collision to make algorithm more efficient

                if (sprite.collide_mask(self, collidable)):
                    self.kill()
                    if collidable.__class__.__name__ is 'Ground':
                        # ellipse is relative to the Surface being drawn on
                        draw.ellipse(collidable.image, (0, 0, 0, 0), self.rect.inflate(map(
                            lambda x: x * 4, self.image.get_size())).move(0, self.image.get_rect().centery - collidable.rect.height))
                        break
                    elif collidable.__class__.__name__ is 'Player':
                        collidable.take_damage(self.damage)

    def update(self, world):
        """Update the explosive weapon.
        :param world: The world in which the explosive exists.
        """
        super(Explosive, self).update(world)
        self.collision_check()
        if self.rect.left < world.rect.left or self.rect.right > world.rect.right:
            self.kill()
        self.rect.move_ip((0, world.gravity))
