import pygame
import itertools

class SpriteSheet():
    def __init__(self, link, scale, steps):
        sprite_sheet_image = pygame.image.load(link).convert_alpha()
        self.sheet = sprite_sheet_image
        self.scale = scale
        self.animation_list = itertools.cycle(self.sprite_motion(steps))
        self.frame = next(self.animation_list)
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 75

    def get_image(self, frame, width, height, scale, colour):
        # first need to make a blank surface
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))  # has taken the whole sprite sheet and only taken part of it
        # scale image and resize to make bigger
        image = pygame.transform.scale(image, (width * scale, height * scale))  # make sprite bigger or smaller
        image.set_colorkey(colour)  # transparent background instead of black background
        return image

    def sprite_motion(self, steps: int):
        # step number depending on animation
        black = (0, 0, 0)  # background of image

        # Create animation list i.e., list containing each animation frame
        animation_list = []

        for x in range(steps):
            # sprite sheet images are 48x48 pixels
            animation_list.append(self.get_image(x, 48, 48, self.scale, black))
        return animation_list

    def cycle_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = next(self.animation_list)
            self.last_update = current_time
        return self.frame
