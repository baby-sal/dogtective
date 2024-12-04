# Dogtective

Dogtective is an arcade game centered around the main pet character who must dodge obstacles to find their lost toy.

## Game demo
Click below to see the game in action!

[Dogtective demo](URL GOES HERE)

## Game screenshots - NEED TO ADD ONCE GAME IS COMPLETE
**Welcome menu**

![Dogtective menu screen](filepath i.e. Assets/menu.png)

**Gameplay screenshot**

![Dogtective gameplay screenshot](filepath i.e. Assets/menu.png)

**Game Over**

![Dogtective game over](filepath i.e. Assets/menu.png)

**Leaderboard**

![Dogtective leaderboard](filepath i.e. Assets/menu.png)

## Set-up

In order for the game to run, please follow the following configuration steps:

### 1. Config
Filepath: logic/score_db_connection/config.py

Add your username and password into the relevant fields in order to connect to the database.

### 2. SQL script - IS THIS NEEDED OR IS IT BEING RAN DIRECTLY FROM PYTHON?
Filepath: logic/score_db_connection/dogtective_scores_db.sql

Run the `dogtective_scores_db.sql` script _(i.e. in SQLWorkbench or similar programme)_ to create the database

### 3. requirements.txt
Please refer to this document for all dependencies that need to be installed for the game to run successfully

Note: If you encounter issues connecting to the database, you may wish to consider the following:

- Conflicts may occur if both mysql-connector and mysql-connector-python packages are installed.
  - It may be advisable to check only mysql-connector-python is installed for this project
- Should you encounter further issues, please try uninstalling and reinstalling mysql-connector-python:
```
pip uninstall mysql-connector-python
pip install mysql-connector-python
```

### 4. run
NEED TO CHECK WHICH FILE WILL BE RUN
Run this file to start the game

## Technologies
- Python
- Pygame
- mySQL

## Contributors
* [Abbeygayle Potts](https://github.com/AbbeygayleP)
* [Estelle Walford](https://github.com/esterwalf)
* [Iman Abdelgani](https://github.com/AversionToDeepWater)
* [Melanie Clark](https://github.com/Melanie-Clark)
* [Sally Davies](https://github.com/baby-sal)
* [Zarrin Rahman](https://github.com/z-for-zarrin)


 
