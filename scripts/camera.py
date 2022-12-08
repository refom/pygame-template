
from pygame.sprite import Group

class Camera(Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self, screen):
        for sprite in self.sprites():
            screen.blit(sprite.image, sprite.rect)

