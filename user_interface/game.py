# game render and loop

import pygame
import sys
from logic.components.enviromental import Obstacle


# Game window set-up

# Initialise pygame
pygame.init()

display_width = 1200
display_height = 780

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dogtective")
clock = pygame.time.Clock()

dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_image.png')
dogtective_coords = [10, 700]


# Game loop: Keeps window open until quit
def game_loop():

    car_image = pygame.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
    car = Obstacle("car", 10, 10, -1, car_image, 900, 0, 0.25)

    game_display.blit(dogtective, dogtective_coords)
    car.draw(game_display)
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # releases pygame resources
                sys.exit()

        game_display.fill((0, 0, 0))

        car.update()
        car.draw(game_display)
        pygame.display.update()
        clock.tick(10)


def run():
    game_loop()


if __name__ == '__main__':
    run()
