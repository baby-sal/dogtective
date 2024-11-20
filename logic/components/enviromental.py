from logic.components.entity import Entity
import pygame


# this will need more functionality to justify its existence at some point
class Environmental(Entity):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        pass

    def __str__(self):
        return f"Name: {self.name}"


class Obstacle(Environmental):

    def __init__(self, name, damage, speed, direction, image, x, y, scale):
        super().__init__(name)
        self.damage = damage
        self.speed = speed
        self.direction = direction  # vector, [1, 0] = right, [-1, 0] = left, [0, 1] = down, [0, -1] = up

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def __str__(self):
        return f"Name: {self.name}, Damage:{self.speed}, Speed: {self.speed}, "


if __name__ == "__main__":
    tree = Environmental("tree")
    print(tree)
    car = Obstacle("car", 10, 2)
    print(car)
