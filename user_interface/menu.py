import pygame
from logic.components.button import Button
from game import run

pygame.init()

SCREEN = pygame.display.set_mode((1200, 720))
BACKGROUND = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/city_backgroud.png")

def pixel_font(size):
    return pygame.font.Font("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf")

def menu():
    pygame.display.set_caption("Main Menu")

    while True:
        SCREEN.blit(BACKGROUND,(0, 0))

        MOUSE_POS_MENU = pygame.mouse.get_pos()

        TEXT_MENU = pixel_font(100).render("MENU", True, "black")
        RECT_MENU = TEXT_MENU.get_rect(center=(640,100))

        BUTTON_PLAY = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/play01.png"), pos= (640, 250))
        BUTTON_LEADERBOARD = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/leaderboard01.png"), pos=(640, 400))
        BUTTON_ABOUT = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/about01.png"), pos=(640, 550))

        SCREEN.blit(TEXT_MENU, RECT_MENU)

        """if time, make the buttons change on mouse pos"""
        # for button in [BUTTON_PLAY,BUTTON_ABOUT,BUTTON_LEADERBOARD]:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_PLAY.check_input(MOUSE_POS_MENU):
                    run()
                # if BUTTON_LEADERBOARD.check_input(MOUSE_POS_MENU):
#                     show leaderboard
#                 if BUTTON_ABOUT.check_input(MOUSE_POS_MENU):
#                     show credits
        pygame.display.update()

menu()

