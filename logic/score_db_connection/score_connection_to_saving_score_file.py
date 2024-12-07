# import pygame  # Import the Pygame library
# from logic.components.character import Character
# from logic.components.health import Health
# from logic.score_db_connection.db_utils_score import DbClass
# # from logic.components.score import Health, Character, Score, Timer
# from logic.components.score import Score
# # from user_interface.game_runner import runner
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the display
# screen = pygame.display.set_mode((800, 600))  # Create a game window with a size of 800x600 pixels commented out this
#
# # health = Health(5)
# # timer = runner()
# # score = Score.calculate_score()
#
#
# def update_score(self):  # will need name
#     # Update the score based on elapsed time and character's current health
#     self.db = DbClass()
#     elapsed_time = self.timer.update()
#     health_points = self.character.health.current  # Access the health from the Character instance
#     self.points = elapsed_time * 10 + health_points * 5
#     db.add_new_score("REPLACE WITH USER INPUT", 40)
#     # return self.points - not sure if this is needed atm?
#
#
# def game_on(timer, character, score):
#     # Refresh the display and update the score
#     pygame.display.flip()
#     return score.update_score()
#
#
# timer = Timer()
# character = Character(name="Dogtective", health=Health(max_health=5))
# score = Score(timer, character)
# db = DbClass()  # Instantiate the DbClass for database operations
#
# game_running = True  # Flag to keep the game loop running
#
# while game_running:
#     # Update the game state (e.g., decrease health)
#     character.health.decrease_health(1)  # Example of health decrease
#     score_value = game_on(timer, character, score)
#     print(f"Score: {score_value}")
#
#     if character.health.current == 0:
#         # End the game if health reaches zero and save the score
#         game_running = False
#         nickname = input(
#             "Enter your nickname: ")  # will this be replaced with pygame user input, as the user won't be interacting with the terminal?
#         db.add_new_score(nickname, score_value)
#         print("Game Over! Your score has been saved.")
#
# # Retrieve and display the top ten scores
# print("Top Ten Scores:")
# for row in db.get_top_ten():
#     print(row)
#
# # Quit Pygame properly
# pygame.quit()
