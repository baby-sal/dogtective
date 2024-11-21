import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        # first need to make a blank surface
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0),((frame * width), 0, width, height))  # taken part of sprite sheet image
        # scale image and resize to make bigger
        image = pygame.transform.scale(image, (width * scale, height * scale))  # make sprite bigger or smaller
        image.set_colorkey(colour)  # transparent background instead of black background
        return image