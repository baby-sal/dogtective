import pygame


class Text():

    def __init__(self, display):
        self.display = display

    def pixel_font(self, size):
        return pygame.font.Font("../logic/assets/fonts/StayPixelRegular.ttf", size)

    def pixel_number_font(self, size):
        return pygame.font.Font("../logic/assets/fonts/PixelGame.otf", size)

    def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text = self.pixel_font(size).render(text, True, colour)
        rect = text.get_rect(center=(rect_pos_x, rect_pos_y))
        self.display.blit(text, rect)

    def number_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text = self.pixel_number_font(size).render(text, True, colour)
        rect = text.get_rect(center=(rect_pos_x, rect_pos_y))
        self.display.blit(text, rect)