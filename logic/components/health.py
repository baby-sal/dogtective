import pygame
from user_interface.game_config import HEIGHT, WIDTH


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

        self.image = pygame.image.load('../logic/assets/images/objects/Bone.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, -25)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw_bones(self, screen): 
        for i in range(self.current):
            screen.blit(self.image, (self.x + i * (self.width + -30), self.y))

    def update(self, screen):
        if self.visible:
            self.rect.center = (self.x, self.y)
            self.draw_bones(screen)

# """Health_hit = pygame.sprite.spritecollide(self, dog_group, False, pygame.sprite.collide_mask)"""
#
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# health = Health(5)
# health.draw_bones(win)