import pygame
import os


def pixel_font(self, size):
    return pygame.font.Font("../assets/StayPixelRegular.ttf", size)


def dog_image(self, pos_x, pos_y):
    smol_dog_pic = pygame.image.load("../assets/images/characters/dogtective_sprite/Walk.png").convert_alpha()
    rect_dog = smol_dog_pic.get_rect(center=(pos_x, pos_y))
    self.display.blit(smol_dog_pic, rect_dog)


def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
    rendered_text = self.pixel_font(size).render(text, True, colour)
    rect = rendered_text.get_rect(center=(rect_pos_x, rect_pos_y))
    self.display.blit(rendered_text, rect)


def credit_blit(self, text, pos_y):
    rendered_text = self.pixel_font(40).render(text, True, "crimson")
    rect = rendered_text.get_rect(center=(640, pos_y))
    self.display.blit(rendered_text, rect)


def background_image(self):
    background_path = "../assets/images/menu/city_backgroud.png"

    if not os.path.exists(background_path):
        raise FileNotFoundError(f"No file '{background_path}' found in the working directory '{os.getcwd()}'.")

    self.background = pygame.image.load(background_path).convert_alpha()
    self.background = pygame.transform.smoothscale(self.background, self.display.get_size())
    self.display.blit(self.background, (0, 0))
