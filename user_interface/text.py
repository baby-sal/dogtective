import pygame


class Text():
    def pixel_font(self, size):
        return pygame.font.Font("../logic/assets/StayPixelRegular.ttf", size)

    def text_blit(self, text, size, colour, rect_pos_x, rect_pos_y):
        text = self.pixel_font(size).render(text, True, colour)
        rect = text.get_rect(center=(rect_pos_x, rect_pos_y))
        self.display.blit(text, rect)