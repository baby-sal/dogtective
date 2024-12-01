import pygame
import math as m
from user_interface.game_config  import WIDTH

class ScrollBackground:
    def __init__(self):
        #do not need transparency for image background therefore do not need convert_alpha
        self.image = pygame.image.load('../logic/assets/images/background/Background2_freepik_draft1.png').convert()
        self.image_width = self.image.get_width()
        self.screen_width = WIDTH
        self.scroll = 0
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.tiles = m.ceil(self.screen_width / self.image_width) + 1

    def endless_scroll(self, screen):
        self.clock.tick(self.fps)
        #draw background
        for i in range(0, self.tiles):
            screen.blit(self.image,(i * self.image_width * self.scroll, 0))
        #scroll
        self.scroll -= 5

        #reset with overlap
        if abs(self.scroll) > self.image_width:
            self.scroll = 0



