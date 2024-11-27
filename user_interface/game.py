# game render and loop

import pygame
import sys
from logic.components.environmental import Obstacle
from logic.components.character import Character


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

        self.dog_group = pygame.sprite.Group()
        self.dog_group.add(Character("dog"))

        car_img = pygame.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
        car1 = Obstacle("car1", car_img, 190, 0, 0.2, 1, 10, [1, 0])
        car2 = Obstacle("car2", car_img, 460, 100, 0.2, 2, 10, [-1, 0])
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2)

        # self.game_display.blit(dogtective, dogtective_coords)
        pygame.display.update()

    def render_all(self, *groups):
        for group in groups:
            group.draw(self.game_display)
            group.update()

    def render_dog(self, car_group):
        self.dog_group.draw(self.game_display)
        self.dog_group.update(car_group)

    # Game loop: Keeps window open until quit
    def game_loop(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # releases pygame resources
                    sys.exit()

            self.game_display.fill((0, 0, 0))

            self.render_all(self.car_group)
            self.render_dog(self.car_group)

            pygame.display.update()
            self.clock.tick(20)


def run():
    game = GameRunner(1200, 720)
    game.game_loop()


if __name__ == '__main__':
    run()
