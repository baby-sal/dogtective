import pygame
import sys
from logic.components.environmental import Environmental, Obstacle
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config


class GameLoop:
    # Game window set-up

    def __init__(self, display, runner):
        # Initialise pygame

        self.game_display = display
        self.runner = runner
        self.clock = pygame.time.Clock()

        self.background_image = pygame.image.load("../logic/assets/images/background/Background2_freepik_draft1.png").convert_alpha()

        health = Health(5)
        self.health_group = pygame.sprite.Group()
        self.health_group.add(health)

        self.dog = Character("dog", health)
        self.dog_group = pygame.sprite.Group()
        self.dog_group.add(self.dog)

        car_img1 = pygame.image.load("../logic/assets/images/obstacles/blue_car.png").convert_alpha()
        car_img2 = pygame.image.load("../logic/assets/images/obstacles/green_car.png").convert_alpha()
        car_img3 = pygame.image.load("../logic/assets/images/obstacles/red_car.png").convert_alpha()
        car_img4 = pygame.image.load("../logic/assets/images/obstacles/compact_orange.png").convert_alpha()
        car_img5 = pygame.image.load("../logic/assets/images/obstacles/sport_yellow.png").convert_alpha()
        truck_img1 = pygame.image.load("../logic/assets/images/obstacles/truck_red.png").convert_alpha()
        car1 = Obstacle("car1", car_img1, 175, 0, 1.2, 1, 3)
        car2 = Obstacle("car2", car_img2, 525, 600, 1.2, 2, -5)
        car3 = Obstacle("car3", car_img3, 952, 800, 1.2, 1, 3)
        car4 = Obstacle("car4", car_img4, 227, 0, 1.25, 2, 6)
        car5 = Obstacle("car5", car_img5, 574, 600, 1.2, 1, 8)
        truck1 = Obstacle("truck1", truck_img1, 995, 800, 1.1, 4, 7)
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2, car3, car4, car5, truck1)

        toy_img = pygame.image.load("../logic/assets/images/objects/toy.png").convert_alpha()
        self.toy = Environmental("toy", toy_img, 1100, 450, 2.5)
        self.toy_group = pygame.sprite.Group()
        self.toy_group.add(self.toy)

        self.groups = {
            "car": self.car_group,
            "dog": self.dog_group,
            "toy": self.toy_group
        }

        pygame.display.update()

    def render_background_image(self):
        self.game_display.blit(self.background_image, (0, 0))

    def render_all(self, *groups):
        for group in groups:
            group.draw(self.game_display)
            group.update()

    def render_dog(self, car_group):
        self.dog_group.draw(self.game_display)
        self.dog_group.update(car_group)

    def reset_game(self):
        # reset health and remove existing data from health group
        self.health_group.empty()
        self.dog_group.empty()
        health = Health(5)
        self.health_group.add(health)
        self.dog = Character("dog", health)
        self.dog_group.add(self.dog)

    # Game loop: Keeps window open until quit
    def game_loop(self):
        pygame.display.set_caption("Dogtective")

        while self.runner.current_state == config.GameState.GAMEPLAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.dog.health.current > 0:
                self.render_background_image()
                self.render_all(self.car_group, self.health_group, self.toy_group)
                self.render_dog(self.car_group)

                pygame.display.update()
                self.clock.tick(config.FPS)

                if pygame.sprite.spritecollide(self.dog, self.toy_group, False, pygame.sprite.collide_mask):
                    self.runner.current_state = config.GameState.WIN
                    self.reset_game()

            else:
                # game over screen here
                self.runner.current_state = config.GameState.LOSE
                self.reset_game()
