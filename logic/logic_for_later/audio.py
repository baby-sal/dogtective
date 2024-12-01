import pygame

pygame.init()

#music for menu (already added to the file)
menu_music = pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_menu.mp3")
pygame.mixer.music.play(-1)

#music for game loop
loop_music = pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_game.mp3")
pygame.mixer.music.play(-1)

