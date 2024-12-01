import pygame

pygame.init()

#music for menu (already added to the file)
menu_music = pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_menu.mp3")
pygame.mixer.music.play(-1)

#music for game loop ( can be added to the beginning)
loop_music = pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_game.mp3")
pygame.mixer.music.play(-1)

#collision sound to be added to character class
c_sound = pygame.mixer.Sound("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/Car_Collision.mp3")

#bark button add to character class?
bark_sound = pygame.mixer.Sound("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/Detective_Dog_Bark.mp3")

# elif keys[p.K_b]:
#     pygame.mixer.Sound.play(bark_sound)
