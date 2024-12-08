import pygame


class Image:

    def __init__(self, display):
        self.display = display

    def dogtective_image(self, pos_x, pos_y, display):
        dogtective_pic = pygame.image.load(
            "../logic/assets/images/characters/Dogtective_icon_no_background_1.png").convert_alpha()
        rect_dog = dogtective_pic.get_rect(center=(pos_x, pos_y))
        self.display.blit(dogtective_pic, rect_dog)

    def dog_walk_image(self, pos_x, pos_y, display):
        smol_dog_pic = pygame.image.load("../logic/assets/images/characters/dogtective_sprite/Walk.png").convert_alpha()
        rect_dog = smol_dog_pic.get_rect(center=(pos_x, pos_y))
        self.display.blit(smol_dog_pic, rect_dog)
