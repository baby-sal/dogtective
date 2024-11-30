# game render and loop

import pygame
import sys
from logic.components.environmental import Obstacle
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config
from game_config import WIDTH, HEIGHT

class GameRunner:
    # Game window set-up

    def __init__(self):
        # Initialise pygame
        pygame.init()

        self.dis_width = WIDTH
        self.dis_height = HEIGHT

        self.game_display = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("Dogtective")
        self.clock = pygame.time.Clock()

        health = Health(5)
        self.health_group = pygame.sprite.Group()
        self.health_group.add(health)

        self.dog = Character("dog", health)
        self.dog_group = pygame.sprite.Group()
        self.dog_group.add(self.dog)

        car_img = pygame.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
        car1 = Obstacle("car1", car_img, 190, 0, 0.2, 1, 3)
        car2 = Obstacle("car2", car_img, 460, 600, 0.2, 2, -5)
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2)

        pygame.display.update()

    def background_image(self):
        image = pygame.image.load(
            '../logic/assets/images/background/Background2_freepik_draft1.png').convert_alpha()
        return image

    def render_background_image(self):
        self.game_display.blit(self.background_image())

    def render_all(self, *groups):
        for group in groups:
            group.draw(self.game_display)
            group.update()

    def render_dog(self, car_group):
        self.dog_group.draw(self.game_display)
        self.dog_group.update(car_group)

    # Game loop: Keeps window open until quit
    def game_loop(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if self.dog.health.current > 0:
                self.game_display.fill((50, 150, 50))

                self.render_all(self.car_group, self.health_group)
                self.render_dog(self.car_group)

                pygame.display.update()
                self.clock.tick(config.FPS)
            else:
                # game over screen here
                run = False


def run():
    game = GameRunner()
    game.game_loop()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
