import pygame  # Import the Pygame library
from saving_score_onto_db import DbClass  # Import the DbClass for handling the database

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # Create a game window with a size of 800x600 pixels

class Health:
    def __init__(self, max_health):
        # Initialize the Health class with maximum health value
        self.max_health = max_health
        self.current = max_health

    def decrease_health(self, amount):
        # Decrease the current health by a given amount, ensuring it doesn't drop below zero
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def increase_health(self, amount):
        # Increase the current health by a given amount, ensuring it doesn't exceed the maximum health
        self.current += amount
        if self.current > self.max_health:
            self.current = self.max_health

class Timer:
    def __init__(self):
        # Initialize the Timer class and record the start time
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        # Calculate the elapsed time in seconds since the start time
        elapsed_seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        return elapsed_seconds

class Score:
    def __init__(self, timer, character):
        # Initialize the Score class with references to the Timer and Character instances
        self.timer = timer
        self.character = character
        self.points = 0

    def update_score(self):
        # Update the score based on elapsed time and character's current health
        elapsed_time = self.timer.update()
        health_points = self.character.health.current  # Access the health from the Character instance
        self.points = elapsed_time * 10 + health_points * 5
        return self.points

class Character:
    def __init__(self, name, health):
        # Initialize the Character class with a name and a Health instance
        self.name = name
        self.health = health

def game_on(timer, character, score):
    # Refresh the display and update the score
    pygame.display.flip()
    return score.update_score()

# Create instances of Timer, Character (with Health), and Score
timer = Timer()
character = Character(name="Dogtective", health=Health(max_health=5))
score = Score(timer, character)
db = DbClass()  # Instantiate the DbClass for database operations

game_running = True  # Flag to keep the game loop running

while game_running:
    # Update the game state (e.g., decrease health)
    character.health.decrease_health(1)  # Example of health decrease
    score_value = game_on(timer, character, score)
    print(f"Score: {score_value}")

    if character.health.current == 0:
        # End the game if health reaches zero and save the score
        game_running = False
        nickname = input("Enter your nickname: ")
        db.add_new_score(nickname, score_value)
        print("Game Over! Your score has been saved.")

# Retrieve and display the top ten scores
print("Top Ten Scores:")
for row in db.get_top_ten():
    print(row)

# Quit Pygame properly
pygame.quit()
