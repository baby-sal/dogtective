import pygame
import get_sprite_image

pygame.init()
screen_width = 1200
screen_height = 720

#temporary screen
screen = pygame.display.set_mode((screen_width,screen_height))
background_colour = (50, 50, 50) #screen bg colour

'''sprite image loops for character sprites 
attack = 4 images - might not need attack animation
death = 4 images 
hurt = 2 images 
idle = 4 images
walk = 6 images
'''


#add to class function?
def sprite_motion(link, steps: int):
    # arguments link to sprite sheet, with step number depending on animation
    sprite_sheet_image = pygame.image.load(link).convert_alpha()
    sprite_sheet = get_sprite_image.SpriteSheet(sprite_sheet_image)

    black = (0, 0, 0)  # background of image

    #Create animation list i.e., list containing each animation frame
    animation_list = []

    for x in range(steps):
        #sprite sheet images are 48x48 pixels, therefore increase size by factor of 2 for 96x96
        #this can be changed
        animation_list.append(sprite_sheet.get_image(x, 48, 48, 2, black))
    return animation_list

dogtective_walk_right = sprite_motion('../assets/images/characters/dogtective_sprite/Walk.png', 6)
dogtective_walk_left = [pygame.transform.flip(frame, True, False).convert_alpha() for frame in dogtective_walk_right]

# uncomment when required
# dogtective_death = sprite_motion("logic/assets/images/characters/dogtective_sprite/Death.png", 4)
# dogtective_idle = sprite_motion("logic/assets/images/characters/dogtective_sprite/Idle.png", 4)
# dogtective_hurt = sprite_motion("logic/assets/images/characters/dogtective_sprite/Hurt.png", 2)

'''MOVING SPRITES 
There are two options:
1. Keep the sprite stationary in the middle of the screen and have the background move as you press the keys

2. Keep the background stationary and have the sprite move 

Typically, we would use option 1. I think this would make the most sense for the game.
We could have a lopping/scrolling background (as I think was discussed at some point?). 
This would mean that the sprite would stay centre in the screen. 

'''

# Starting frame, position and speed
first_frame = dogtective_walk_right[0]
dogtective_x = screen_width // 2 - first_frame.get_width() // 2 # center of x_axis
dogtective_y = screen_height // 2 - first_frame.get_height() // 2 # center of y_axis
dogtective_speed = 0.5  # Speed of movement

# Animation frames
last_update = pygame.time.get_ticks()  # need this to refresh animation, see line x
animation_cooldown = 75  # in milliseconds, how long to cycle through each frame
frame = 0

run = True
while run:
    screen.fill(background_colour)  # temporary screen

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    direction = None  # None = Dog doesn't animate in starting position, change to a direction i.e. right if you want dog to animate on the spot

    if keys[pygame.K_LEFT]:
        dogtective_x -= dogtective_speed  # speed is required to move the dog along the x-axis
        direction = 'left'
    if keys[pygame.K_RIGHT]:
        dogtective_x += dogtective_speed
        direction = 'right'
    if keys[pygame.K_UP]:
        dogtective_y -= dogtective_speed  # speed is required to move the dog along the y-axis
        direction = 'up'
    if keys[pygame.K_DOWN]:
        dogtective_y += dogtective_speed
        direction = 'down'

    # Handle frame updates for animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(dogtective_walk_left):  #loops back to first image in sprite sheet
            frame = 0

    # Get the correct frame based on direction
    if direction == 'left':
        current_frame = dogtective_walk_left[frame]
    elif direction == 'right':
        current_frame = dogtective_walk_right[frame]
    else:
        current_frame = dogtective_walk_right[0]  # Default to walking right if no direction is set

    # Draw the sprite at the updated position
    screen.blit(current_frame, (dogtective_x, dogtective_y))

    # Update the display
    pygame.display.update()

if __name__ == "__main__":
    pass