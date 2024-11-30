import pygame
import sys
from logic.components.button import Button
from game import run

pygame.init()

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dogtective: Main Menu")
background = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/city_backgroud.png").convert()
background = pygame.transform.smoothscale(background, display.get_size())

def pixel_font(size):
    return pygame.font.Font("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf", size)

def leaderboard():
    while True:
        # mouse_pos_ldr = pygame.mouse.get_pos()
        """call the db"""
        #
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if go_back.check_input(mouse_pos_ldr):
        #             menu()
        # pygame.display.update()


def credit_screen():
    while True:
        pygame.display.set_caption("Dogtective: Credits")
        mouse_pos_credits = pygame.mouse.get_pos()

        display.fill("pink")
        bg = pygame.transform.smoothscale((pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/urban-landscape-background-Preview.png").convert()), display.get_size())
        display.blit(bg, (0, 0))

        text_title = pixel_font(150).render("CREDITS:", True, "orange")
        rect_title = text_title.get_rect(center=(640, 100))

        text_credits = pixel_font(50).render("\nAbbeygayle Potts - Project Lead \nEstelle Walford - Programmer \nIman Abdelgani- UI/UX \nMel Clarke- Testing \nSally Davies- UI/UX \nZarrin Rahman - Project Lead", True, "crimson")
        rect_credits = text_credits.get_rect(center=(640, 300))

        text_sound = pixel_font(50).render(
            "with special thanks to:\nAhmed Abdi - Sound Engineering & Design",
            True, "darkblue")
        rect_sound = text_credits.get_rect(center=(640, 720))

        display.blit(text_title,rect_title)
        display.blit(text_credits, rect_credits)
        display.blit(text_sound, rect_sound)

        button_go_back = Button(image = None, pos_x = 1200, pos_y = 50, font=pixel_font(40),
         colour="purple4", text_in="go back")

        button_go_back.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_go_back.check_input(mouse_pos_credits):
                    menu()

        pygame.display.update()

def menu():
    while True:
        display.blit(background, (0, 0))

        mouse_pos_menu = pygame.mouse.get_pos()

        text_menu = pixel_font(150).render("MENU", True, "plum4")
        rect_menu = text_menu.get_rect(center=(640,200))

        """trying to put the dog on the menu screen"""

        # dog_pic = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/characters/doctective_image/doctective_image.jpeg").convert()
        # rect_dog = dog_pic.get_rect(bottomleft=(320,500))

        button_play = Button(image = None, pos_x = 640, pos_y = 300, font=pixel_font(100),
         colour="darksalmon", text_in="play")
        button_ldr = Button(image = None, pos_x = 640, pos_y = 400, font=pixel_font(100),
         colour="lightsalmon", text_in="LEADERBOARD")
        button_credits = Button(image = None, pos_x = 640, pos_y = 500, font=pixel_font(100),
         colour="lightsalmon", text_in="CREDITS")


        display.blit(text_menu, rect_menu)

        for button in [button_play, button_ldr, button_credits]:
            # button.click_colour(mouse_pos_menu)
            button.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.check_input(mouse_pos_menu):
                    run()
                # if button_ldr.check_input(mouse_pos_menu):
                #     leaderboard()
                if button_credits.check_input(mouse_pos_menu):
                    credit_screen()
        pygame.display.update()

menu()

