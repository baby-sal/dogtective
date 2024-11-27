import pygame
from logic.components.button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
BACKGROUND = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/city_backgroud.png")

def menu():
    pygame.display.set_caption("Main Menu")

    while True:
        SCREEN.blit(BACKGROUND,(0, 0))

