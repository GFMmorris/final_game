import pygame.sprite
import sys
from ground import Ground, GROUND_SIZE, Fill
from chara import Chara

from menu import *
from map import draw_background, TILE_SIZE

playing = False

DISPLAY_W = 700
DISPLAY_H = 500

earth = pygame.sprite.Group()
core = pygame.sprite.Group()

for n in range(0, DISPLAY_W, GROUND_SIZE):
    earth.add(Ground(n, DISPLAY_H-200))

for r in range(DISPLAY_H-168, DISPLAY_H, GROUND_SIZE):
    for b in (0, DISPLAY_W, GROUND_SIZE):
        core.add(Fill(b, r))


class Game:
    def __init__(self):
        pygame.init()

        # Self.running when the game as a whole is running, self.playing will be for when the game is actually
        # being played
        self.running = True
        self.playing = False

        # Set key boolean values
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

        # set display size
        self.screen = pygame.display.set_mode((700, 500))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Window Information
        self.DISPLAY_W, self.DISPLAY_H = 700, 500
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        # Text information
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # BackGround stuff
        self.WINDOW_WIDTH = (self.DISPLAY_W / 18) * TILE_SIZE
        self.WINDOW_HEIGHT = (self.DISPLAY_H / 18) * TILE_SIZE
        self.bg = draw_background((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Initialize the other menus and sets curr_menu status
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while playing:
            chara = Chara()
            self.screen.blit(self.bg, self.bg.get_rect())
            self.check_events()
            earth.draw(self.screen)
            core.draw(self.screen)
            chara.update(self.screen)
            pygame.display.flip()
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

    # def create_earth(self):
    #     for x in range(0, self.WINDOW_WIDTH, TILE_SIZE):
    #         earth = self._create_ground(self,(x,)
    #         ground_group.add(earth)
    #
    # def _create_ground(self, pos):
    #     # create a normal ground element
    #     dirt = Ground(self, pos)
    #     dirt_width, dirt_height = dirt.rect.size
    #     dirt.rect.bottomleft = pos
