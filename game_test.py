import pygame.sprite
import sys

from random import randint

from ground import Ground, GROUND_SIZE, Fill
from chara import Chara
from chara2 import Chara2
from bullet import Bullet
from bullet2 import Bullet2
from enemy import Bird

from menu import *
from map import draw_background, TILE_SIZE

# Variable for running game loop among all files
playing = False

# jumping variable for global use for both characters
jumping = False
jumping_2 = False

# Standard screen size variables among all files
DISPLAY_W = 700
DISPLAY_H = 500

CLOCK = pygame.time.Clock()

# Ground Groups for game part 1
earth = pygame.sprite.Group()
core = pygame.sprite.Group()

for n in range(0, DISPLAY_W, GROUND_SIZE):
    earth.add(Ground(n, DISPLAY_H - 200))

for b in (0, DISPLAY_W, GROUND_SIZE):
    for r in range(332, 500, GROUND_SIZE):
        core.add(Fill(b, r))


class Game:
    """Game class that holds the main class and game loop that runs the menu and the other classes"""

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

        # Text information, uses an imported font from 1001freefonts.com
        self.font_name = "fonts/8-bit-operator/8bitOperatorPlus8-Regular.ttf"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # BackGround stuff
        self.WINDOW_WIDTH = (self.DISPLAY_W / 18) * TILE_SIZE
        self.WINDOW_HEIGHT = (self.DISPLAY_H / 18) * TILE_SIZE
        self.bg = draw_background((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # Sound inits for the game
        self.chara_gun_sound = 'sounds/lazer7.mp3'
        self.chara_2_gun_sound = 'sounds/lazer15.mp3'

        # Initialize the other menus and sets curr_menu status
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        # init character
        self.chara = Chara(self, 'images/Characters/chara_1_stand.png', (100, 300))
        self.chara_2 = Chara2(self, 'images/Characters/chara_2_stand.png', (150, 300))
        self.bullets = pygame.sprite.Group()
        self.bullets_2 = pygame.sprite.Group()
        self.bullets_allowed = 3
        self.bullets_allowed_2 = 3

        # enemy init data
        self.birds = pygame.sprite.Group()
        self.bird_number = 5

        # level counter
        self.level_counter = 1

    # Molly Tressler Helped to make CHara jump
    def game_loop(self):
        while playing:
            self.check_events()
            self._update_bullets()
            self._update_chara()
            self._update_birds()
            self.reset_keys()
            self.update_screen()
            self.level_counter += 1

    def check_events(self):
        """Key Press event information. Gets events from pygame. Event, checks the kind of event."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                sys.exit()
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
                if event.key == pygame.K_w:
                    game_test.jumping = True
                    self.chara.jump()
                if event.key == pygame.K_d:
                    self._chara_fire_bullet()
                    pygame.mixer.music.load(self.chara_gun_sound, "pew")
                    pygame.mixer.music.play()
                if event.key == pygame.K_o:
                    game_test.jumping_2 = True
                    self.chara_2.jump()
                if event.key == pygame.K_k:
                    self._chara_2_fire_bullet()
                    pygame.mixer.music.load(self.chara_2_gun_sound, "pew2")
                    pygame.mixer.music.play()

    def reset_keys(self):
        # Function to reset all keys after a game loop
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

    def _chara_fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < self.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _chara_2_fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets_2) < self.bullets_allowed_2:
            new_bullet = Bullet2(self)
            self.bullets_2.add(new_bullet)

    def _update_chara(self):
        """Update the position of the chara"""
        if jumping:
            self.chara.jump()
        if jumping_2:
            self.chara_2.jump()
        self.chara.update(jumping)
        self.chara_2.update(jumping_2)

    def _update_bullets(self):
        """Update the position of the bullets and then get rid of old bullets"""
        # update bullet position
        self.bullets.update(self.birds)
        self.bullets_2.update(self.birds)
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= DISPLAY_W:
                self.bullets.remove(bullet)
        for bullet in self.bullets_2.copy():
            if bullet.rect.left >= DISPLAY_W:
                self.bullets_2.remove(bullet)

    def _create_bird(self):
        """create a bird enemy at some position"""
        bird = Bird(self)
        bird.x = 700
        bird.rect.x = bird.x
        bird.rect.y = randint(0, 500)
        self.birds.add()

    def draw_text(self, text, size, x, y):
        # Function to draw text on menus
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def _update_birds(self):
        """Birds now update position and keep a constant numebr of birds on the screen"""
        self.birds.update(self.level_counter)
        if len(self.birds) < self.bird_number:
            new_bird = Bird(self)
            self.birds.add(new_bird)
        for bird in self.birds:
            if bird.rect.x < 0:
                pygame.sprite.Sprite.kill(bird)

    def add_bird(self):
        if len(self.birds) < self.bird_number:
            new_bird = Bird(self)
            self.birds.add(new_bird)

    def update_screen(self):
        """Update the screen with all information about the chara and all enemies and projectiles"""
        # Background and ground building
        self.screen.blit(self.bg, self.bg.get_rect())
        earth.draw(self.screen)
        core.draw(self.screen)

        # blit bullet for chara 1
        for bullet in self.bullets.sprites():
            bullet.make_bullet()

        # blit bullet for chara 2
        for bullet in self.bullets_2.sprites():
            bullet.make_bullet()

        self.birds.draw(self.screen)

        # Draw the character
        self.chara.blitme()
        self.chara_2.blitme()

        # Flip the final Screen
        pygame.display.flip()
        CLOCK.tick(60)
