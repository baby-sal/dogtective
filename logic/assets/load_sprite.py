import pygame
import get_sprite_image


pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

'''sprite image loops for character sprites 
attack = 4 images 
death = 4 images 
hurt = 2 images 
idle = 4 images
walk = 6 images
'''

def sprite_motion(link, steps:int):
    # arguments link to sprite sheet, with step number depending on animation
    link = link.convert_alpha()
    sprite_sheet_image = pygame.image.load(link).convert_alpha()
    sprite_sheet = get_sprite_image.SpriteSheet(sprite_sheet_image)

    black = (0,0,0) #background of image

    #Create animation list i.e., list containing each animation frame
    animation_list = []

    #is the variable animation steps no longer needed due to the argument steps in the function?
    animation_steps = steps #number of animation frames in sprite sheets
    last_update = pygame.time.get_ticks() # need this to refresh animation, see line x
    animation_cooldown = 75 #in milliseconds, how long to cycle through each frame
    frame = 0

    for x in range(animation_steps):
        #sprite sheet images are 48x48 pixels, therefore increase by factor of 2 for 96x96
        #this can be changed as needed
        animation_list.append(sprite_sheet.get_image(x,48,48,2,black))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list): #loops back to first image in sprite sheet
            frame = 0

    # #show frame image
    screen.blit(animation_list[frame],(0, 0))

    # need tp blit image from this onto surface, and animate motion

dogtective_walk_right = sprite_motion("logic/assets/images/characters/dogtective_sprite/Walk.png", 6)

current_direction = "down"

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
    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # so you can continually press the key to make sprite move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        current_direction = "right"


    pygame.display.update()




if __name__ == "__main__":
    pass
