import sys
import pygame
import user_interface.game_config as config
from logic.components.button import Button
from user_interface.screens.screen import Screen


class Credits(Screen):

    def credit_blit(self, text, pos_y):
        credit_text = self.text.pixel_font(40).render(text, True, "crimson")
        rect = credit_text.get_rect(center=(config.WIDTH / 2, pos_y))
        self.display.blit(credit_text, rect)

    def credit_screen(self):

        while self.runner.current_state == config.GameState.CREDITS:
            width = config.WIDTH
            height = config.HEIGHT
            pygame.display.set_caption("Dogtective: Credits")
            mouse_pos_credits = pygame.mouse.get_pos()

            self.display.fill("pink")
            bg = pygame.transform.smoothscale(
                pygame.image.load(
                    "../logic/assets/images/menu/urban-landscape-background-Preview.png").convert_alpha(),
                self.display.get_size())
            self.display.blit(bg, (0, 0))

            self.text.text_blit("CREDITS:", 100, "orange", width // 2, height // 7)
            self.image.dog_walk_image(600, 175, self.display)

            # Adding space between each credit
            y_offset = 250  # Initial offset
            line_height = 50  # Space between lines

            credits = [
                "Abbeygayle Potts",
                "Estelle Walford",
                "Iman Abdelgani",
                "Melanie Clark",
                "Sally Davies",
                "Zarrin Rahman",
            ]

            # Loops through the credits list and renders each name, i adds an index so Abbeygayle would be index 0
            for i, credit in enumerate(credits):
                self.credit_blit(credit, y_offset + i * line_height)

            self.text.text_blit("with special thanks to:\nAhmed Abdi - Sound Engineering & Design", 30, "darkblue",
                                width // 2, y_offset + 7 * line_height)

            button_go_back = Button(image=None, pos_x=width - 80, pos_y=50, font=self.text.pixel_font(40),
                                    colour="purple4",
                                    text_in="go back")
            button_go_back.update_button(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and button_go_back.check_input(mouse_pos_credits):
                        self.runner.current_state = config.GameState.MENU

            pygame.display.update()
