import pygame
from user_interface.game_config import WIDTH, HEIGHT

class EndScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load('Scene.png') # Update with scenery images
        self.img2 = pygame.image.load('You Win.png') # Shows when a player has won, update png once image has been confirmed
        self.img3 = pygame.image.load('You lose.png') # Shows when a player has lost, update png once image has been confirmed

        self.img1 = pygame.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = pygame.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = pygame.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update(self, n):
        if n == 0:
            self.image = self.img3 # you lose background image
        elif n == 1:
            self.image = self.img2 # you win background image

def scoreDisplay():
    start_ticks = pygame.time.get_ticks()

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    bg = EndScreen()
    screen_group = pygame.sprite.Group(bg)

    gameOn = True
    while gameOn:
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000 # Timer for the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        screen_group.update(1) # Change 1 to 0 if the player loses
        screen_group.draw(win)
        pygame.display.flip()

    pygame.quit()
