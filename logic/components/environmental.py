import pygame
from user_interface.game_config import HEIGHT, WIDTH

# this will need more functionality to justify its existence at some point
class Environmental(pygame.sprite.Sprite):

    def __init__(self, name, image, x, y, scale):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def __str__(self):
        return f"Name: {self.name}"


class Obstacle(Environmental):

    def __init__(self, name, image, x, y, scale, damage, speed, direction):
        super().__init__(name, image, x, y, scale)
        self.damage = damage
        self.speed = speed
        self.direction = direction  # vector, [1, 0] = right, [-1, 0] = left, [0, 1] = down, [0, -1] = up

    def update(self):
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.rect.y = 0
            self.speed *= -1

        elif self.rect.y + self.rect.height > HEIGHT:
            self.rect.y = HEIGHT - self.rect.height
            self.speed *= -1
            #prevents cars from going off the edge of the background image

    def __str__(self):
        return f"Name: {self.name}, Damage:{self.speed}, Speed: {self.speed}, "


if __name__ == "__main__":
    # insert sample outputs here
    pass
