# Final Game Project
## Thomas Morris
 
 EW200 Final Game Project. 

This game is a multiplayer 2D shooter game. The goal is to shoot as many birds out of the sky.


Multiplayer: Player 1: used the (w) and (d) keys to jump and shoot bullets respectively. (game_test.py 129:143) Player 2: use the (o) key to jump and the (k) button to shoot bullets. (game_test.py 129:143)

Physical: The game has a working jumping physics for when the characters fall. (chara.py, chara2.py, 37)

Tiler: The background is made with tiles. (map.py)

Sound Blaster: The bullets make sound when they are fired. (game_test.py line134-135, 141-142)

Level Up: The birds get faster over time as they die. (enemy.py line 31)

Looking Weak(modified): The characters image changes if the character is jumping or not. (chara.py and chara2.py, line 50)

Shooter: The Characters fire bullets. Each has a separate bullet group that gets updated independently (bullet.py game_test.py line 132,139)

Textual: The text is not static and changes based on which screen is shown. Seperate draw text function was made(menu.py, game_test.py line 190)

Shifting Screens: The screens change based on what you are doing. Main menu or game (menu.py)

Fancy Fonts: The font that is used is not native to pygame, it was downloaded and input when the text is drawn. (game_test.py 60)

Main Menu: The main screen has a few different sub menus that can be interacted with. (menu.py)

TO RUN THE GAME, RUN THE main.py FILE
