import pygame
from user_interface.game_config import HEIGHT, WIDTH

class Road(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.x = 150 #where it is on the x axis
            
        else:
            self.x = 420 #where it is on the x axis
        
        self.image = pygame.image.load('Pygame_ideas\src\Road.png').convert_alpha()            
        self.width = 90#image width
        self.height = 480#image height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.y = 0
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

road1 = Road(1)
road2 = Road(2)
road_group = pygame.sprite.Group(road1, road2)
road_group.add(road1, road2)

win = pygame.display.set_mode((WIDTH, HEIGHT))
road_group.draw(win)
road_group.update()