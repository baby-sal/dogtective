# game render and loop

import pygame
import sys

# Game window set-up
def initial_game_window():
    # Initialise pygame
    pygame.init()

    display_width = 1200
    display_height = 780

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Dogtective")
    clock = pygame.time.Clock()

    dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_image.png')
    dogtective_coords = [10, 700]
    game_display.blit(dogtective, dogtective_coords)
    pygame.display.update()


# Game loop: Keeps window open until quit
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def run():
    initial_game_window()
    game_loop()


if __name__ == '__main__':
    run()
