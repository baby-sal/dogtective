import pygame
import sys
from logic.components.button import Button
from game import run

pygame.init()

DISPLAY = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Main Menu")
BACKGROUND = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/city_backgroud.png").convert()
BACKGROUND= pygame.transform.smoothscale(BACKGROUND, DISPLAY.get_size())


def pixel_font(size):
    return pygame.font.Font("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf", size)

def play():
    while True:
        MOUSE_POS_PLAY = pygame.mouse.get_pos()

        DISPLAY.fill("blue4")

        TEXT_PLAY = pixel_font(50).render("Play screen", True, "blue4")
        RECT_PLAY = TEXT_PLAY.get_rect(center=(640,240))
        DISPLAY.blit(TEXT_PLAY, RECT_PLAY)

        GO_BACK = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/back01.png"), pos_x = 640, pos_y = 240)
        GO_BACK.update_button(DISPLAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GO_BACK.check_input(MOUSE_POS_PLAY):
                    menu()
        pygame.display.update()


def credits():
    while True:
        MOUSE_POS_CREDITS = pygame.mouse.get_pos()

        DISPLAY.fill("blue4")

        TEXT_CREDITS = pixel_font(50).render("Credits screen", True, "blue4")
        RECT_CREDITS = TEXT_CREDITS.get_rect(center=(640, 240))
        DISPLAY.blit(TEXT_CREDITS, RECT_CREDITS)

        GO_BACK = Button(image=pygame.image.load(
            "/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/back01.png"), pos_x = 640, pos_y = 240)
        GO_BACK.update_button(DISPLAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GO_BACK.check_input(MOUSE_POS_CREDITS):
                    menu()
        pygame.display.update()


def leaderboard():
    while True:
        MOUSE_POS_LDR = pygame.mouse.get_pos()

        DISPLAY.fill("blue4")

        TEXT_LDR = pixel_font(50).render("Leaderboard screen", True, "blue4")
        RECT_LDR = TEXT_LDR.get_rect(center=(640, 240))
        DISPLAY.blit(TEXT_LDR, RECT_LDR)

        GO_BACK = Button(image=pygame.image.load(
            "/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/back01.png"),pos_x = 640, pos_y = 240)
        GO_BACK.update_button(DISPLAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GO_BACK.check_input(MOUSE_POS_LDR):
                    menu()
        pygame.display.update()

def menu():
    while True:
        DISPLAY.blit(BACKGROUND, (0, 0))

        MOUSE_POS_MENU = pygame.mouse.get_pos()

        TEXT_MENU = pixel_font(100).render("MENU", True, "teal")
        RECT_MENU = TEXT_MENU.get_rect(center=(640,100))

        BUTTON_PLAY = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/play01.png"), pos_x = 640, pos_y = 240)
        BUTTON_LDR = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/leaderboard01.png"),pos_x = 640, pos_y = 400)
        BUTTON_CREDITS = Button(image = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/about01.png"), pos_x = 640, pos_y = 500)

        DISPLAY.blit(TEXT_MENU, RECT_MENU)

        """if time, make the buttons change on mouse pos"""
        # for button in [BUTTON_PLAY,BUTTON_CREDITS,BUTTON_LDR]:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BUTTON_PLAY.check_input(MOUSE_POS_MENU):
                    run()
                # if BUTTON_LDR.check_input(MOUSE_POS_MENU):
#                     show leaderboard
#                 if BUTTON_CREDITS.check_input(MOUSE_POS_MENU):
#                     show credits
        pygame.display.update()

menu()

