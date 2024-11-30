import pygame
from user_interface.game_config import HEIGHT, WIDTH

def background_image(self):
    self.image = pygame.image.load('../logic/assets/images/background/Background2_freepik_draft1.png').convert_alpha()
    self.image_width = self.image.get_width()
    self.screen_width = WIDTH
    self.screen_height = HEIGHT
    self.add(background_image)