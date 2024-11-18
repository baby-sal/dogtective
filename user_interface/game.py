# game render and loop

import pygame


# Game window set-up
def initial_game_window():
    # Initialise pygame
    pygame.init()

    display_width = 1200
    display_height = 780

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Dogtective")

    dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_image.png')
    dogtective_coords = [10, 700]
    game_display.blit(dogtective, dogtective_coords)
    pygame.display.update()

    clock = pygame.time.Clock()

    return dogtective_coords, dogtective, game_display

# This is incorrect and needs to be deleted or re-written!
def movement(dogtective_coords, dogtective, game_display):
    collision = False
    while not collision:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dogtective_coords += [-10, 0]
                elif event.key == pygame.K_RIGHT:
                    dogtective_coords += [10, 0]
                elif event.key == pygame.K_UP:
                    dogtective_coords += [0, -10]
                elif event.key == pygame.K_DOWN:
                    dogtective_coords += [0, 10]
        game_display.blit(dogtective, dogtective_coords)


def run():
    dogtective_coords, dogtective, game_display = initial_game_window()
    movement(dogtective_coords, dogtective, game_display)


if __name__ == '__main__':
    run()
