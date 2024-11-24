import pygame
from get_sprite_image import SpriteSheet

pygame.init()
screen_width = 1200
screen_height = 720

#temporary screen
screen = pygame.display.set_mode((screen_width,screen_height))
BG = (50, 50, 50) #screen bg colour

'''sprite image loops for character sprites 
attack = 4 images - might not need attack animation
death = 4 images 
hurt = 2 images 
idle = 4 images
walk = 6 images
'''

# #add to class function?
# def sprite_motion(link, steps:int):
#     # arguments link to sprite sheet, with step number depending on animation
#     sprite_sheet_image = pygame.image.load(link).convert_alpha()
#     sprite_sheet = SpriteSheet(sprite_sheet_image)
#
#     black = (0,0,0) #background of image
#
#     #Create animation list i.e., list containing each animation frame
#     animation_list = []
#
#     last_update = pygame.time.get_ticks() # need this to refresh animation, see line x
#     animation_cooldown = 75 #in milliseconds, how long to cycle through each frame
#     frame = 0
#
#     for x in range(steps):
#         #sprite sheet images are 48x48 pixels, therefore increase size by factor of 2 for 96x96
#         #this can be changed
#         animation_list.append(sprite_sheet.get_image(x,48,48,2,black))
#
#     current_time = pygame.time.get_ticks()
#     if current_time - last_update >= animation_cooldown:
#         frame += 1
#         last_update = current_time
#         if frame >= len(animation_list): #loops back to first image in sprite sheet
#             frame = 0
#
#
#     # #show frame image
#     return screen.blit(animation_list[frame],(0, 0))

    # need tp blit image from this onto surface, and animate motion

dogtective_walk_left = SpriteSheet("logic/assets/images/characters/dogtective_sprite/Walk.png", 6)
dogtective_walk_right = pygame.transform.flip(dogtective_walk_left, True, False) #flip animation on y axis?
dogtective_death = sprite_motion("logic/assets/images/characters/dogtective_sprite/Death.png", 4)
dogtective_idle = sprite_motion("logic/assets/images/characters/dogtective_sprite/Idle.png", 4)
dogtective_hurt = sprite_motion("logic/assets/images/characters/dogtective_sprite/Hurt.png", 2)


current_direction = "left"

'''MOVING SPRITES 
There are two options:
1. Keep the sprite stationary in the middle of the screen and have the background move as you press the keys

2. Keep the background stationary and have the sprite move 

Typically, we would use option 1. I think this would make the most sense for the game.
We could have a lopping/scrolling background (as I think was discussed at some point?). 
This would mean that the sprite would stay centre in the screen. 

'''


run = True
while run:
    screen.fill(BG) # temporary screen
    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # so you can continually press the key to make sprite move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        current_direction = "right"
        dogtective_walk_right



    pygame.display.update()




if __name__ == "__main__":
    pass
