import pygame
import sys
from logic.components.environmental import Obstacle, Collectable
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config
from logic.assets.scrolling_background import ScrollBackground


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
        car1 = Obstacle("car1", car_img1, 200, 0, 0.2, 1, 3)
        car2 = Obstacle("car2", car_img2, 550, 600, 0.2, 2, -5)
        car3 = Obstacle("car3", car_img3, 975, 800, 0.2, 1, 3)
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2, car3)

        ball_img = pygame.image.load('../logic/assets/images/objects/toy.png').convert_alpha()
        self.ball = Collectable("ball", ball_img, 1100, 320, 0.5)
        self.ball_group = pygame.sprite.Group()
        self.ball_group.add(self.ball)

        self.groups = {
            'car': self.car_group,
            'dog': self.dog_group,
            'ball': self.ball_group
        }

        pygame.display.update()

    def has_internal(self, sprite):
        for group in self.groups.values():
            if sprite in group:
                return True
            return False

    def add_internal(self, sprite, group_name):
        if group_name in self.groups:
            self.groups[group_name].add(sprite)
        else:
            print(f"Group {group_name} not found!")

    def add_sprite(self, sprite):
        if hasattr(sprite, "_spritegroup"):
            for spr in sprite.sprites():
                if not self.has_internal(spr):
                    self.add_internal(spr, spr._spritegroup)
                    spr.add_internal(self)
                elif not self.has_internal(sprite):
                    self.add_internal(sprite, sprite._spritegroup)
                    sprite.add_internal(self)

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

