import pygame
import sys

# Game window set-up
def initial_game_window():
    # Initialize pygame
    pygame.init()

    display_width = 1200
    display_height = 780

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Dogtective")
    clock = pygame.time.Clock()

    dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_image.png')
    dogtective_coords = [10, 700]

    return game_display, clock, dogtective, dogtective_coords


# Game loop: Keeps window open until quit
def game_loop():
    game_display, clock, dogtective, dogtective_coords = initial_game_window()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        game_display.fill((255, 255, 255))  # Fill with white

        # Draw the dogtective image
        game_display.blit(dogtective, dogtective_coords)

        # Update the display
        pygame.display.flip()

        # Manage frame rate
        clock.tick(60)  # 60 frames per second


def run():
    game_loop()


if __name__ == '__main__':
    run()
