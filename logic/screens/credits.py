import pygame
import sys
from logic.components.button import Button
import user_interface.game_config as config

def credit_screen(self):
    while True:
        width = config.WIDTH
        height = config.HEIGHT
        pygame.display.set_caption("Dogtective: Credits")
        mouse_pos_credits = pygame.mouse.get_pos()

        self.display.fill("pink")
        bg = pygame.transform.smoothscale(
            pygame.image.load("../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
            self.display.get_size())
        self.display.blit(bg, (0, 0))

        self.text_blit("CREDITS:", 100, "orange", width // 2, height // 7)
        self.dog_image(width // 2, height // 6)

        # Adding space between each credit
        y_offset = 250  # Initial offset
        line_height = 50  # Space between lines

        self.credit_blit("Abbeygayle Potts - co-Project Lead & architect", y_offset)
        self.credit_blit("Estelle Walford - UI/UX", y_offset + line_height)
        self.credit_blit("Iman Abdelgani - UI/UX & Documentation Lead", y_offset + 2 * line_height)
        self.credit_blit("Mel Clarke - Testing", y_offset + 3 * line_height)
        self.credit_blit("Sally Davies - UI/UX", y_offset + 4 * line_height)
        self.credit_blit("Zarrin Rahman - co-Project Lead & architect", y_offset + 5 * line_height)
        self.text_blit("with special thanks to:\nAhmed Abdi - Sound Engineering & Design", 30, "darkblue",
                       width // 2, y_offset + 8 * line_height)

        button_go_back = Button(image=None, pos_x=width - 80, pos_y=50, font=self.pixel_font(40), colour="purple4",
                                text_in="go back")
        button_go_back.update_button(self.display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_go_back.check_input(mouse_pos_credits):
                    self.menu()

        pygame.display.update()