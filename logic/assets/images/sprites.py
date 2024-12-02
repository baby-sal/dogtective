import pygame
from logic.components.environmental import Obstacle, Collectable

def car_group(self):
    car_img1 = pygame.image.load('../logic/assets/images/obstacles/blue_car.png').convert_alpha()
    car_img2 = pygame.image.load('../logic/assets/images/obstacles/green_car.png').convert_alpha()
    car_img3 = pygame.image.load('../logic/assets/images/obstacles/red_car.png').convert_alpha()
    car1 = Obstacle("car1", car_img1, 200, 0, 0.2, 1, 3)
    car2 = Obstacle("car2", car_img2, 550, 600, 0.2, 2, -5)
    car3 = Obstacle("car3", car_img3, 975, 800, 0.2, 1, 3)
    self.car_group = pygame.sprite.Group()
    self.car_group.add(car1, car2, car3)

def toy_group(self):
    toy_img = pygame.image.load('../logic/assets/images/objects/toy.png').convert_alpha()
    self.toy = Collectable("ball", toy_img, 1100, 320, 0.5)
    self.toy_group = pygame.sprite.Group()
    self.toy_group.add(self.toy)