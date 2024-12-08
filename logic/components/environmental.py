import pygame
from user_interface.game_config import HEIGHT


# This class inherits from the in-built pygame module pygame.sprite to make use of its features such as rendering and
# collision detection
class Environmental(pygame.sprite.Sprite):
    # Class for objects on screen player may interact with

    def __init__(self, name, image, x, y, scale):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.name = name
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def __str__(self):
        return f"Name: {self.name}"


class Obstacle(Environmental):
    # Class for Environmental objects that can move and/or damage the player

    def __init__(self, name, image, x, y, scale, damage, speed):
        super().__init__(name, image, x, y, scale)
        self.damage = damage
        self.speed = speed  # all obstacles move vertically, down is positive

    def update(self):
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.rect.y = 0
            self.speed *= -1

        elif self.rect.y + self.rect.height > HEIGHT:
            self.rect.y = HEIGHT - self.rect.height
            self.speed *= -1
            # prevents obstacle from going off the edge of the background image

    def __str__(self):
        return f"Name: {self.name}, Damage:{self.damage}, Speed: {self.speed}, "


if __name__ == "__main__":
    # insert sample outputs here
    pass
