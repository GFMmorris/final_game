# Final Game Project
## Thomas Morris
 
 EW200 Final Game Project. 

This will be a two level game with a functional main menu and scoreboard system.

The file will include several class files (.py) each contain one class of the entire game. One file will be the actual game file that will run the entire game.

Assets for the game are located in the images folder in this directory.

The scoreboard will work as a continuously updated .txt file that stores the information as plain text. The information will be accessible via json pull requests in game.

Each level will have the same map and enemies. Goal is to earn the most points during your play-through.

Level 1: This a 2D platformer side crawler. There will be several types of enemies and functional gravity/ environment settings. Use  the WASD and space bar for controls. This level will be scored based on time to completion with a count up timer. 3 lives, if die, game over.

Level 2: This level is a flight level with obstacle asteroids and small alien fleets that can be destroyed. The player earns more points depending on the number of aliens/asteriods they get rid of during their playthrough. 3 lives, if die, game over.

Score: Score is determined by the sum of th two scores form Lvl 1 and Lvl 2. The player is first asked to input their name. Once accepted and checked, the file will then either:

1. Show their score if it is their first time and store the value in a .txt file.

2. if the player is returning (i.e. their name is already in the system) The score is checked and the higher score is saved. Then the system displays the best score. OPT. if the score is an improvment the screen displys special graphics.


TO RUN THE SYSTEM THUS FAR, RUN THE main.py FILE
