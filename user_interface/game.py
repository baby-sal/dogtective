# game render and loop

import pygame
import sys
from enum import Enum
from logic.components.environmental import Obstacle
from logic.components.character import Character
from logic.components.health import Health
import user_interface.game_config as config
from logic.assets.scrolling_background import ScrollBackground
from menu_display import MenuDisplay

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    NEXT_LEVEL = 4

class GameRunner:
    # Game window set-up

    def __init__(self):
        # Initialise pygame
        pygame.init()

        self.dis_width = config.WIDTH
        self.dis_height = config.HEIGHT
        self.FPS = config.FPS

        self.game_display = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("Dogtective")
        self.clock = pygame.time.Clock()

        self.background_image = self.load_background_image()
        self.scroll_background = ScrollBackground()
        self.current_state = GameState.MENU #sets the current state to menu

        health = Health(5)
        self.health_group = pygame.sprite.Group()
        self.health_group.add(health)

        self.dog = Character("dog", health)
        self.dog_group = pygame.sprite.Group()
        self.dog_group.add(self.dog)

        car_img1 = pygame.image.load('../logic/assets/images/obstacles/blue_car.png').convert_alpha()
        car_img2 = pygame.image.load('../logic/assets/images/obstacles/green_car.png').convert_alpha()
        car_img3 = pygame.image.load('../logic/assets/images/obstacles/pink_car.png').convert_alpha()
        car1 = Obstacle("car1", car_img1, 140, 0, 0.2, 1, 3)
        car2 = Obstacle("car2", car_img2, 490, 600, 0.2, 2, -5)
        car3 = Obstacle("car1", car_img3, 915, 800, 0.2, 1, 3)
        self.car_group = pygame.sprite.Group()
        self.car_group.add(car1, car2, car3)

        pygame.display.update()

        self.menu_display = MenuDisplay()

    def load_background_image(self):
        return pygame.image.load('../logic/assets/images/background/Background2_freepik_draft1.png').convert_alpha()

    def render_background_image(self):
        self.game_display.blit(self.background_image, (0, 0))

    def render_menu(self):
        self.game_display.fill((50, 150, 50))  # Background color for menu
        font = pygame.font.Font(None, 74)
        text = font.render("Dogtective", True, (255, 255, 255))
        self.game_display.blit(text, (
            self.dis_width // 2 - text.get_width() // 2, self.dis_height // 2 - text.get_height() // 2))
        # Use the MenuDisplay instance to render the menu
        self.menu_display.menu()

    def render_game_over(self):
        self.game_display.fill((0, 0, 0))  # Background color for game over screen
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        self.game_display.blit(text, (
        self.dis_width // 2 - text.get_width() // 2, self.dis_height // 2 - text.get_height() // 2))

        sub_text = pygame.font.Font(None, 36).render("Press Enter to Retry", True, (255, 255, 255))
        self.game_display.blit(sub_text, (self.dis_width // 2 - sub_text.get_width() // 2, self.dis_height // 2 + 50))

    def render_next_level(self):
        self.game_display.fill((0, 0, 0))  # Background color for next level screen
        font = pygame.font.Font(None, 74)
        text = font.render("Next Level", True, (0, 255, 0))
        self.game_display.blit(text, (
        self.dis_width // 2 - text.get_width() // 2, self.dis_height // 2 - text.get_height() // 2))

        sub_text = pygame.font.Font(None, 36).render("Press Enter to Continue", True, (255, 255, 255))
        self.game_display.blit(sub_text, (self.dis_width // 2 - sub_text.get_width() // 2, self.dis_height // 2 + 50))

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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.current_state == GameState.MENU:
                            self.current_state = GameState.PLAYING  # Switch to playing state
                        elif self.current_state == GameState.GAME_OVER:
                            self.current_state = GameState.PLAYING  # Restart the game after game over
                            self.dog.health.current = 5  # Reset dog health
                            # Reset other game parameters as needed
                        elif self.current_state == GameState.NEXT_LEVEL:
                            self.current_state = GameState.PLAYING  # Continue to next level
                            # Set up the next level parameters here

            if self.current_state == GameState.MENU:
                self.render_menu()
            elif self.current_state == GameState.PLAYING:
                if self.dog.health.current > 0:
                    self.scroll_background.endless_scroll(self.game_display)  # Render the scrolling background
                    self.render_all(self.car_group, self.health_group)
                    self.render_dog(self.car_group)
                else:
                    self.current_state = GameState.GAME_OVER  # Switch to game over state
            elif self.current_state == GameState.GAME_OVER:
                self.render_game_over()
            elif self.current_state == GameState.NEXT_LEVEL:
                self.render_next_level()

            pygame.display.update()
            self.clock.tick(self.FPS)


def run():
    game = GameRunner()
    game.game_loop()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    run()
