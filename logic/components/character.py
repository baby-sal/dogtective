import pygame as p
import pygame.time
# import sys may be needed when dog collides with ball and game ends?

from user_interface.game_config import HEIGHT, WIDTH
from logic.assets.get_sprite_image import SpriteSheet


# class for player character
class Character(p.sprite.Sprite):

    def __init__(self, name, health):
        super().__init__()
        self.name = name
        self.health = health
        self.x = 50
        self.y = HEIGHT / 2
        self.speed = 4
        self.width = 100
        self.height = 50
        self.collision_immune = False
        self.collision_time = 0

        self.idle = SpriteSheet('../logic/assets/images/characters/dogtective_sprite/Idle.png', 1.5, 4)
        self.walk = SpriteSheet('../logic/assets/images/characters/dogtective_sprite/Walk.png', 1.5, 6)
        self.hurt = SpriteSheet('../logic/assets/images/characters/dogtective_sprite/Hurt.png', 1.5, 2)

        self.move = False
        self.direction = "right"

        self.image = self.idle.frame
        self.mask = p.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()

    def update(self, car_group): # do we need ball_group here?
        if pygame.time.get_ticks() - self.collision_time > 1500:  # The time is in ms.
            self.collision_immune = False
        self.move = False
        if self.health.current >= 0:
            self.movement()
        self.update_animation()
        self.correction()
        self.check_collision(car_group) # do we need ball_group here?
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()

        if keys[p.K_LEFT]:
            self.x -= self.speed  # left key pressed negative velocity
            self.direction = "left"
            self.move = True

        elif keys[p.K_RIGHT]:
            self.x += self.speed  # right key pressed positive velocity
            self.direction = "right"
            self.move = True

        if keys[p.K_UP]:
            self.y -= self.speed  # left key up negative velocity
            self.move = True

        elif keys[p.K_DOWN]:
            self.y += self.speed  # right key down positive velocity
            self.move = True

    def update_animation(self):
        if self.move:
            self.walk.cycle_animation()
            self.image = self.walk.frame
        elif self.collision_immune:
            self.hurt.cycle_animation()
            self.image = self.hurt.frame
        else:
            self.idle.cycle_animation()
            self.image = self.idle.frame

        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False).convert_alpha()

    def correction(self):
        """Prevents character going off the side of the screen"""
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.width / 2 > HEIGHT:
            self.y = HEIGHT - self.width / 2

    def check_collision(self, car_group): # add ball_group
        car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)
        # ball_check = p.sprite.spritecollide(self, ball_group, False, p.sprite.collide_mask)
        if car_check and not self.collision_immune:
            self.health.current -= car_check[0].damage
            # print(self.health.current)    # uncomment for testing
            self.collision_immune = True
            self.collision_time = pygame.time.get_ticks()

        # if ball_check and not self.collision_immune:
        #     self.collision_immune = True
        #     sys.exit()

    def __str__(self):
        return f"{self.name}: Health ({self.health})"