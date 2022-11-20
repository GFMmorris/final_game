from game_test import Game

g = Game()

while g.running:
    g.playing = True
    g.game_loop()