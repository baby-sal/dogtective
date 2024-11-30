# game render and loop

import pygame
import sys
from logic.components.environmental import Obstacle, Environmental
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config


class GameRunner:
    # Game window set-up

    def __init__(self):
        # Initialise pygame
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT

        self.game_display = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("Dogtective")
        self.clock = pygame.time.Clock()

        self.background_image = self.load_background_image()
        self.scroll_background = ScrollBackground()

        health = Health(5)
        self.health_group = pygame.sprite.Group()
        self.health_group.add(health)

        self.dog = Character("dog", health)
        self.dog_group = pygame.sprite.Group()
        self.dog_group.add(self.dog)

        car_img1 = pygame.image.load('../logic/assets/images/obstacles/blue_car.png').convert_alpha()
        car_img2 = pygame.image.load('../logic/assets/images/obstacles/green_car.png').convert_alpha()
        car_img3 = pygame.image.load('../logic/assets/images/obstacles/red_car.png').convert_alpha()
        car1 = Obstacle("car1", car_img1, 140, 0, 0.2, 1, 3)
        car2 = Obstacle("car2", car_img2, 490, 600, 0.2, 2, -5)
        car3 = Obstacle("car3", car_img3, 915, 800, 0.2, 1, 3)
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2, car3)

        # ball sprite for loading onto final background
        # may need factoring into separate function/different name?
        ball_img = pygame.image.load(
            '../logic/assets/images/objects/ball.png').convert_alpha()
        ball = Environmental("ball", ball_img, self.dis_width * 0.96,
                             self.dis_height * 0.95, 0.1)
        self.final_screen_ball_group = pygame.sprite.Group()
        self.final_screen_ball_group.add(ball)

        pygame.display.update()

    def load_background_image(self):
        image = pygame.image.load('../logic/assets/images/background/Background2_freepik_draft1.png').convert_alpha()
        return image

    def render_background_image(self):
        self.game_display.blit(self.background_image, (0, 0))

    def render_all(self, *groups):
        for group in groups:
            group.draw(self.game_display)
            group.update()

    def render_dog(self, car_group):
        self.dog_group.draw(self.game_display)
        self.dog_group.update(car_group)

    def render_final_screen_ball(self, ball):
        self.final_screen_ball_group.draw(self.game_display)
        self.final_screen_ball_group.update(ball)

    # Game loop: Keeps window open until quit
    def game_loop(self):
        run = True
        ball_active = False

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if self.dog.health.current > 0:
                self.game_display.fill((50, 150, 50))

                self.render_all(self.car_group, self.health_group)

                # # placeholder for ball to show after 3 seconds only until background is sorted - can be deleted
                # if not ball_active and pygame.time.get_ticks() > 3000:
                #     self.final_screen_ball_group = pygame.sprite.Group()
                #     self.final_screen_ball_group.add(self.ball)
                #     ball_active = True

                # added here so it renders behind the dog, but will need changing when linking to the background
                self.render_final_screen_ball(self.final_screen_ball_group)
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
