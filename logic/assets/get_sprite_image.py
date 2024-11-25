import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        # first need to make a blank surface
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0),((frame * width), 0, width, height))  # has taken the whole sprite sheet and only taken part of it
        # scale image and resize to make bigger
        image = pygame.transform.scale(image, (width * scale, height * scale))  # make sprite bigger or smaller
        image.set_colorkey(colour)  # transparent background instead of black background
        return image


'''
Tried to incorporate everything into a SpriteSheet class but I haven't done that properly so commenting it out

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image
        self.frame = 0
        self.last_update = pygame.time.get_ticks()  # need this to refresh animation, see line x
        self.animation_cooldown = 75 #in milliseconds
        # Create animation list i.e., list containing each animation frame
        self.animation_list = []

    def get_image(self, frame, width, height, scale, colour):
        # first need to make a blank surface
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0),((frame * width), 0, width, height))  # taken part of sprite sheet image
        # scale image and resize to make bigger
        image = pygame.transform.scale(image, (width * scale, height * scale))  # make sprite bigger or smaller
        image.set_colorkey(colour)  # transparent background instead of black background
        return image

    def sprite_motion(self,link , steps):
        # arguments link to sprite sheet, with step number depending on animation
        sprite_sheet_image = pygame.image.load(link).convert_alpha()
        # sprite_sheet = self.get_image(sprite_sheet_image) #do I put more arguments here?

        black = (0, 0, 0)  # background of image

        for x in range(steps):
            # sprite sheet images are 48x48 pixels, therefore increase size by factor of 2 for 96x96
            # this can be changed
            #do the lines below make sense? I feel like I'm adding a lot of self.stuff here
            image = self.get_image(x, 48, 48, 2, black)
            self.animation_list.append(image)


    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):  # loops back to first image in sprite sheet
                frame = 0


    def on_screen(self, screen, x, y):
        #assuming the character goes in the middle of a 1200x720 screen, x = 600 and y = 360
        screen.blit(self.animation_list[self.frame], (x, y))

'''