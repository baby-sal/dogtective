import pygame
import get_sprite_image


#When I tried, I did not put the info from lies 6-22 in a function. However, I think a function will make more sense no?
def sprite_motion(link:str): #link to walk, attack, death or idle animation
    sprite_sheet_image = pygame.image.load(link).convert_alpha()
    sprite_sheet = get_sprite_image.SpriteSheet(sprite_sheet_image)

    black = (0,0,0) #what the background of our image is?

    #Create animation list i.e., list containing each animation frame
    animation_list = []
    animation_steps = 6 #number of animation frames in sprite sheets
    last_update = pygame.time.get_ticks() # need this to refresh animation, see line x
    animation_cooldown = 75 #in milliseconds, how long to cycle through each frame
    frame = 0

    for x in range(animation_steps):
        #sprite sheet images are 48x48 pixels, therefore increase by factor of 2 for 96x96
        #this can be changed as needed
        animation_list.append(sprite_sheet.get_image(x,48,48,2,black))


'''NOT SURE WHAT TO DO AFTER THIS! 
When I tried on my owen repo I had made a small game loop to showcase the walking animation. 
Not sure if this can be incorporated into a function? 
I have been meaning to watch this https://www.youtube.com/watch?v=nXOVcOBqFwM&ab_channel=CodingWithRuss which I think is useful
See below

run = True
while run:
    #update background, needs to be done before loading images ontop

    #update animation
    # if 75ms have passed between last update and current one, update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list): #loops back to first image in sprite sheet
            frame = 0

    #show frame image
    screen.blit(animation_list[frame],(0, 0))

    pygame.display.update()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

'''
