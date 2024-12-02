import pygame

pygame.init()

#music for menu (already added to the file)
menu_music = pygame.mixer.music.load("../logic/assets/audio/BGM_menu.mp3")
pygame.mixer.music.play(-1)

#music for game loop ( can be added to the beginning)
loop_music = pygame.mixer.music.load("../logic/assets/audio/BGM_game.mp3")
pygame.mixer.music.play(-1)

#bark button add to character class?
bark_sound = pygame.mixer.Sound("../logic/assets/audio/Detective_Dog_Bark.mp3")

# if event.type == pygame.KEYDOWN:
#   if event.key == pygame.K_b
#     pygame.mixer.Sound.play(bark_sound)
