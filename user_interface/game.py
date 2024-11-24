# game render and loop

import pygame
import sys
from logic.components.environmental import Obstacle


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

        # to be replaced with instance of Player/Character
        dogtective = pygame.image.load('../logic/assets/images/characters/dogtective_sprite/walk.png')
        dogtective_coords = [10, 700]

        # may need to refactored into its own function
        car_right_img = pygame.image.load('../logic/assets/images/obstacles/car/car_right_img.png').convert_alpha()
        car_left_img = pygame.image.load('../logic/assets/images/obstacles/car/car_left_img.png').convert_alpha()
        car_up_img = pygame.image.load('../logic/assets/images/obstacles/car/car_up_img.png').convert_alpha()
        car_down_img = pygame.image.load('../logic/assets/images/obstacles/car/car_down_img.png').convert_alpha()
        car_right = Obstacle("car_right", car_right_img, 0, 0, 0.2, 10, 10, [1, 0])
        car_left = Obstacle("car_left", car_left_img, 1000, 100, 0.2, 10, 10, [-1, 0])
        car_up = Obstacle("car_up", car_up_img, 100, 700, 0.2, 10, 10, [0, -1])
        car_down = Obstacle("car_up", car_down_img, 500, 0, 0.2, 10, 10, [0, 1])
        self.cars = [car_left, car_right, car_up, car_down]

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
                if self.game_display.get_rect().colliderect(car.rect):  # checks if car is still on screen
                    car.update()
                    print(car.rect.topright)
                    car.draw(self.game_display)

            pygame.display.update()
            self.clock.tick(20)


def run():
    game = GameRunner(1200, 720)
    game.game_loop()


if __name__ == '__main__':
    run()
