import pygame

class Health:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current = max_health

    def decrease_health(self, amount):
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def increase_health(self, amount):
        self.current += amount
        if self.current > self.max_health:
            self.current = self.max_health

class Timer:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return elapsed_seconds

class Score:
    def __init__(self, timer, character):
        self.timer = timer
        self.character = character
        self.points = 0

    def update_score(self):
        elapsed_time = self.timer.update()
        health_points = self.character.health.current  # Access the health from the Character instance
        self.points = elapsed_time * 10 + health_points * 5
        return self.points

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def game_on(timer, character, score):
    pygame.display.flip()
    return score.update_score()

# Example of how to use these classes
timer = Timer()
character = Character(name="Dogtective", health=Health(max_health=5))  # Create Character with Health instance
score = Score(timer, character)
game_running = True

while game_running:
    # Update game state here
    character.health.decrease_health(1)  # Example of health decrease
    score_value = game_on(timer, character, score)
    print(f"Score: {score_value}")

    if character.health.current == 0:
        game_running = False
        print("Game Over!")
