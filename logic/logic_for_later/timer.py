import pygame

def Timer():
    global gameOn
    if gameOn:
        start_ticks = pygame.time.get_ticks()
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # timer for the game

    pygame.display.flip()