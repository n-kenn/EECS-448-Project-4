from pygame import Surface, sprite


class Ground(sprite.Sprite):
    def __init__(self, size, pos, color, color_key):
        super(Ground, self).__init__()
        self.image = Surface(size).convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(color)
        self.color_key = color_key
        self.image.set_colorkey(self.color_key)

    # def resolve_explosion(self, explosion):
    #     draw.ellipse(explosion.image, self.color_key,
    #                  explosion.pos, explosion.rect)
    #
    # def resolve_explosions(self, explosions):
    #     for explosion in explosions:
    #         resolve(explosion)

    def update(self):
        pass
