import pygame
from user_interface.game_config import HEIGHT, WIDTH

class Health(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.number = number

        self.visible = True
        self.x = 30#opposite end of the screen
        self.width = 50
        self.height = 50

        self.image = pygame.image.load('../Pygame_ideas/src/Bone.png').convert_alpha()#update name once image loaded     
        self.image = pygame.transform.rotate(self.image, -25)
        self.y = 30
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def draw_bones(self, screen): 
            for i in range(self.number): screen.blit(self.image, (self.x + i * (self.width + -30), self.y))
            

    def update(self):
        if self.visible:
            self.rect.center = (self.x, self.y)
            self.draw_bones()

"""Health_hit = pygame.sprite.spritecollide(self, dog_group, False, pygame.sprite.collide_mask)"""

win = pygame.display.set_mode((WIDTH, HEIGHT))
health = Health(5)
health.draw_bones(win)