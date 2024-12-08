# Dogtective

The main character, a determined dog detective, is on a mission to recover a lost toy.
The toy has gone missing and Dogtective must dodge the moving cars to find it.

## Gameplay Mechanics:

Navigate the main menu with mouse clicks.
Use the keyboard arrow keys (up, down, left and right) to move Dogtective around the screen.

## Game demo - MC TO SORT URL OR MP4

Click below to see the game in action!

[Dogtective demo](URL GOES HERE)

## Game screenshots - LEADERBOARD SCREENSHOTS WILL BE UPDATED WHEN CODING IS FINISHED

**Main menu**

<img src="logic/assets/images/readme/main_menu.png" alt="Dogtective main menu" width="300" height="200">

**Gameplay**

<img src="logic/assets/images/readme/game_play.png" alt="Game play" width="300" height="200">

**Game Over**

<img src="logic/assets/images/readme/game_over.png" alt="Game over" width="300" height="200">

**Leaderboard**

<img src="logic/assets/images/readme/leaderboard.png" alt="Leaderboard" width="300" height="200">

**Credits**

<img src="logic/assets/images/readme/credits.png" alt="Credits" width="300" height="200">

## Set-up

To ensure the game runs smoothly, please follow the configuration steps below:

### 1. Config

Within your IDE, go to `logic/score_db_connection/config.py`.

Add your database username and password into the appropriate fields in order to connect to the database.

### 2. SQL script

Within your IDE, go to `logic/score_db_connection/dogtective_scores_db.sql`.

Run the `dogtective_scores_db.sql` script _(i.e. in SQLWorkbench or similar programme)_ to create the database.

### 3. Requirements/Dependencies

Please refer to `requirements.txt` for all dependencies that need to be installed for the game to run successfully.

**Note**: If you experience issues connecting to the database, consider the following troubleshooting steps:

- Conflicts may occur if both mysql-connector and mysql-connector-python packages are installed.
    - It may be advisable to check only mysql-connector-python is installed for this project


- Should you encounter further issues, please try uninstalling and reinstalling mysql-connector-python:

```
pip uninstall mysql-connector-python
pip install mysql-connector-python
```

### 4. Run

Run the `game-runner` python file to start the game. Dogtective needs your help! 😄

## Technologies used

- Python
- Pygame
- mySQL

## Credits
- [Road background](https://www.freepik.com/free-vector/aerial-scene-intersection_5361164.htm#fromView=search&page=1&position=6&uuid=a2915187-2a0e-49fe-b8a5-0a10b6afb006)
- [Dogtective game play sprites](https://free-game-assets.itch.io/free-street-animal-pixel-art-asset-pack)
- [City background](https://lucky-loops.itch.io/parallax-city-background)


## Testing - TBC - MC TO UPDATE

Unit testing
Gherkin testing and googledoc links

## Contributors

- [Abbeygayle Potts](https://github.com/AbbeygayleP)
- [Estelle Walford](https://github.com/esterwalf)
- [Iman Abdelgani](https://github.com/AversionToDeepWater)
- [Melanie Clark](https://github.com/Melanie-Clark)
- [Sally Davies](https://github.com/baby-sal)
- [Zarrin Rahman](https://github.com/z-for-zarrin)