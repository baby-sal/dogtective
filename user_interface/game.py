import pygame
import sys
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config
from logic.assets.scrolling_background import ScrollBackground
from logic.assets.images.sprites import car_group, ball_group
from logic.assets.internal_sprite import has_internal, add_internal, add_sprite

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

        car_group(self)
        ball_group(self)

        self.groups = {
            'car': self.car_group,
            'dog': self.dog_group,
            'ball': self.ball_group
        }

        pygame.display.update()

    def has_internal(self, sprite):
        has_internal(self, sprite)

    def add_internal(self, sprite, group_name):
        add_internal(self, sprite, group_name)

    def add_sprite(self, sprite):
        add_sprite(self, sprite)

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

    # Game loop: Keeps window open until quit
    def game_loop(self):
        run = True
        ball_active = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if self.dog.health.current > 0:
                self.render_background_image()
                self.render_all(self.car_group, self.health_group, self.ball_group)
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
