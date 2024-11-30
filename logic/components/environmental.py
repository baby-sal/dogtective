import pygame
from user_interface.game_config import HEIGHT, WIDTH

class Environmental(pygame.sprite.Sprite):

    def __init__(self, name, image, x, y, scale, width, height):
        super().__init__()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def __str__(self):
        return f"Name: {self.name}"


class Obstacle(Environmental):

    def __init__(self, name, image, x, y, scale, damage, speed, width, height):
        super().__init__(name, image, x, y, scale)
        self.damage = damage
        self.speed = speed
        width = 155
        height = 355

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
        return f"Name: {self.name}, Damage:{self.speed}, Speed: {self.speed}, "


if __name__ == "__main__":
    # insert sample outputs here
    pass
