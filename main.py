import game_test
from game_test import Game
from menu import MainMenu

g = Game()
mm = MainMenu(g)

while g.running:
    g.curr_menu.display_menu()
    if game_test.playing:
        g.game_loop()
