import pygame
import sys
from logic.components.button import Button
from game import run

pygame.init()

menu_music = pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_menu.mp3")
pygame.mixer.music.play(-1)

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dogtective: Main Menu")
background = pygame.image.load("../logic/assets/images/menu/city_backgroud.png").convert_alpha()
background = pygame.transform.smoothscale(background, display.get_size())

def pixel_font(size):
    return pygame.font.Font("../logic/assets/StayPixelRegular.ttf", size)

def text_blit(text, size, colour, rect_pos_x, rect_pos_y):
    text = pixel_font(size).render(text,True, colour)
    rect = text.get_rect(center=(rect_pos_x, rect_pos_y))
    display.blit(text, rect)

def credit_blit(text, pos_y):
    text = pixel_font(40).render(text, True,"crimson")
    rect = text.get_rect(center=(640,pos_y))
    display.blit(text,rect)

def dog_walk_image(pos_x, pos_y):
    smol_dog_pic = pygame.image.load("../logic/assets/images/characters/dogtective_sprite/Walk.png").convert_alpha()
    rect_dog = smol_dog_pic.get_rect(center=(pos_x, pos_y))
    display.blit(smol_dog_pic, rect_dog)

def dogtective_image(pos_x, pos_y):
    dogtective_pic = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/characters/Dogtective_icon_no_background_1.png").convert_alpha()
    rect_dog = dogtective_pic.get_rect(center=(pos_x, pos_y))
    display.blit(dogtective_pic, rect_dog)

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
        bg = pygame.transform.smoothscale(pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(), display.get_size())
        display.blit(bg, (0, 0))

        text_blit("CREDITS:", 100, "orange", 640, 150)
        dog_walk_image(640, 175)
        credit_blit("Abbeygayle Potts - co-Project Lead & architect", 250)
        credit_blit("Estelle Walford - UI/UX", 300)
        credit_blit("Iman Abdelgani - UI/UX & Documentation Lead", 350)
        credit_blit("Mel Clarke - Testing", 400)
        credit_blit("Sally Davies - UI/UX", 450)
        credit_blit("Zarrin Rahman - co-Project Lead & architect", 500)
        text_blit("with special thanks to:\nAhmed Abdi - Sound Engineering & Design", 30, "darkblue", 640, 600)


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

def you_lose():
    while True:
        mouse_pos_end = pygame.mouse.get_pos()

        display.fill("pink")
        bg = pygame.transform.smoothscale(
            pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
            display.get_size())
        display.blit(bg, (0, 0))

        text_blit("GAME OVER", 200, "crimson", 640, 300)
        dogtective_image(640, 575)

        button_go_back = Button(image=None, pos_x=1200, pos_y=50, font=pixel_font(40),
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

        text_blit("Dogtective", 200, "royalblue4", 640, 175)
        text_blit("MENU", 100,"royalblue4", 640, 275)
        dog_walk_image(640, 600)

        button_play = Button(image = None, pos_x = 640, pos_y = 350, font=pixel_font(75),
         colour="brown", text_in="play")
        button_ldr = Button(image = None, pos_x = 640, pos_y = 425, font=pixel_font(75),
         colour="lightsalmon", text_in="LEADERBOARD")
        button_credits = Button(image = None, pos_x = 640, pos_y = 500, font=pixel_font(75),
         colour="lightsalmon", text_in="CREDITS")


        for button in [button_play, button_ldr, button_credits]:
            # button.click_colour(mouse_pos_menu)
            button.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.check_input(mouse_pos_menu):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/audio/BGM_game.mp3")
                    pygame.mixer.music.play(-1)
                    run()
                # if button_ldr.check_input(mouse_pos_menu):
                #     leaderboard()
                if button_credits.check_input(mouse_pos_menu):
                    credit_screen()
        pygame.display.update()

menu()

