# game render and loop

import pygame
import sys
from logic.components.enviromental import Obstacle


class GameRunner:
    # Game window set-up

    def __init__(self, dis_width, dis_height):
        # Initialise pygame
        pygame.init()

        self.dis_width = dis_width
        self.dis_height = dis_height

        self.game_display = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("Dogtective")
        self.clock = pygame.time.Clock()

        dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_image.png')
        dogtective_coords = [10, 700]

        car_image = pygame.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
        car1 = Obstacle("car", 10, 10, [1, 0], car_image, 0, 0, 0.25)
        car2 = Obstacle("car", 10, 10, [-1, 0], car_image, 1000, 200, 0.25)
        self.cars = [car1, car2]

        self.game_display.blit(dogtective, dogtective_coords)
        pygame.display.update()

    # Game loop: Keeps window open until quit
    def game_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # releases pygame resources
                    sys.exit()

            self.game_display.fill((0, 0, 0))

            for car in self.cars:
                car.update()
                car.draw(self.game_display)

            pygame.display.update()
            self.clock.tick(20)


def run():
    game = GameRunner(1200, 720)
    game.game_loop()


if __name__ == '__main__':
    run()
