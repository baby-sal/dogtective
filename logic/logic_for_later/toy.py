import pygame
from logic.components.environmental import Collectable

class Toy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        toy_img = pygame.image.load('../logic/assets/images/objects/toy.png').convert_alpha()
        self.collectable = Collectable("toy", toy_img, 1100, 320, 0.5)
        self.image = self.collectable.image
        self.rect = self.collectable.rect