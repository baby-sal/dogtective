import pygame as p
import pygame.time

from user_interface.game_config import HEIGHT, WIDTH

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

        self.dog1 = p.image.load('../logic/assets/images/characters/dogtective_sprite/Idle.png').convert_alpha()
        # set width and height for dog image 1
        self.dog1 = p.transform.scale(self.dog1, (self.width, self.height))
        # set width and height for dog image 2
        self.dog2 = p.transform.flip(self.dog1, True, False)  # flips dog image 1 to face the other direction

        self.image = self.dog1
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self, car_group):
        if pygame.time.get_ticks() - self.collision_time > 3000:  # The time is in ms.
            self.collision_immune = False
        self.movement()
        self.correction()
        self.check_collision(car_group)
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()

        if keys[p.K_LEFT]:
            self.x -= self.speed  # left key pressed negative velocity
            self.image = self.dog2  # switch to dog image 2

        elif keys[p.K_RIGHT]:
            self.x += self.speed  # right key pressed positive velocity
            self.image = self.dog1   # switch to dog image 1

        if keys[p.K_UP]:
            self.y -= self.speed  # left key up negative velocity

        elif keys[p.K_DOWN]:
            self.y += self.speed  # right key down positive velocity

    def correction(self):
        """Prevents character going off the side of the screen"""
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.width / 2 < 0:
            self.y = self.width / 2

        elif self.y + self.width / 2 > WIDTH:
            self.y = WIDTH - self.width / 2

    def check_collision(self, car_group):
        car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)
        if car_check and not self.collision_immune:
            self.health.current -= car_check[0].damage
            print("Health: ", self.health)
            self.collision_immune = True
            self.collision_time = pygame.time.get_ticks()
            print(self.collision_time)

    def __str__(self):
        return f"{self.name}: Health ({self.health})"
