import pygame
from user_interface.game_config import HEIGHT, WIDTH #is HEIGHT and WIDTH referenced within this file?


class Health(pygame.sprite.Sprite):
    def __init__(self, max_health):
        super().__init__()
        self.max_health = max_health
        self.current = max_health

        self.visible = True
        self.x = 30     # opposite end of the screen
        self.y = 30
        self.width = 50
        self.height = 50

        self.bone = pygame.image.load('../logic/assets/images/objects/Bone.png').convert_alpha()
        self.bone = pygame.transform.rotate(self.bone, -25)
        self.image = self.bone
        self.rect = self.bone.get_rect()

    def draw_bones(self):
        health_surface = pygame.Surface((self.width * 5, self.height))
        for i in range(self.current):
            health_surface.blit(self.bone, (i * (self.width - 30), 0))
        self.image = health_surface
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        if self.visible:
            self.rect.center = (self.x, self.y)
            self.draw_bones()
