import sys

import pygame.sprite

from menu import *
from map import draw_background, TILE_SIZE
from ground import Ground, GROUND_SIZE


class Game:
    def __init__(self):
        pygame.init()
        # Self.running when the game as a whole is running, self.playing will be for when the game is actually
        # being played
        self.running, self.playing = True, False
        # Set key boolean values
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
        # set display size
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # BG stuff
        self.WINDOW_WIDTH = (self.screen_width / 18) * TILE_SIZE
        self.WINDOW_HEIGHT = (self.screen_height / 18) * TILE_SIZE
        self.bg = draw_background((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Ground stuff
        self.ground_group = pygame.sprite.Group()

        self.DISPLAY_W, self.DISPLAY_H = self.screen.get_rect().width, self.screen.get_rect().height
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # Initialize the other menus and sets curr_menu status
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.screen.blit(self.bg, self.bg.get_rect())
            pygame.sprite.Group.draw(self.ground_group, self.screen)
            self.check_events()
            # TODO Remove start_key mapping feature by end game, could produce issues downstream
            if self.START_KEY:
                self.playing = False
            # self.draw_text('Thanks for playing', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            # self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                # force quite function to stop the game and close the program
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
