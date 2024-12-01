import pygame
import sys

def leaderboard(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if go_back.check_input(mouse_pos_ldr):
                #     self.menu()
                pass
        pygame.display.update()

#this will likely call the score function and import the score function when it has been created