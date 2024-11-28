import pygame
from user_interface.game_config import WIDTH, HEIGHT

class Screen(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = pygame.image.load('Scene.png')#Update with scenery images
        self.img2 = pygame.image.load('You Win.png')#shows when a player has won, update png once image has been confirmed
        self.img3 = pygame.image.load('You lose.png')# shows when a player has lost, update png once image has been confirmed

        self.img1 = pygame.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = pygame.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = pygame.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)

def EndScreen(n):
    global gameOn

    gameOn = False
    """if n == 0:
        bg.image = bg.img3 #you loose background image, need to update based on images saved

    elif n == 1:
        bg.image = bg.img2 #you win background image, need to update based on images saved"""

def scoreDisplay():
    global gameOn
    if gameOn:
        start_ticks = pygame.time.get_ticks()
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000#timer for the game
    
    pygame.display.flip()
    
win = p.display.set_mode((WIDTH, HEIGHT))
bg = Screen()
screen_group = pygame.sprite.Group()
screen_group.add(bg)
screen_group.draw(win)
screen_group.update()


