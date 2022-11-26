import pygame
import game_test


# Base class for all menu types. Main, options, credits.
class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 75

    # draw cursor with function for writing text in game class.
    def draw_cursor(self):
        self.game.draw_text('*', 30, self.cursor_rect.x, self.cursor_rect.y + 7)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


# subclass main menu, starts at the start
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.options_x, self.options_y = self.mid_w, self.mid_h + 50
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 70
        self.quit_x, self.quit_y = self.mid_w, self.mid_h + 110
        self.playing = False

        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Game Title', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Start Game', 20, self.start_x, self.start_y)
            self.game.draw_text('Options', 20, self.options_x, self.options_y)
            self.game.draw_text('Credits', 20, self.credits_x, self.credits_y)
            self.game.draw_text('Quit', 20, self.quit_x, self.quit_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        """Checks for logic direction for cursor based on starting position"""
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                # start game loop
                print('Check_input check')
                self.playing = True
                game_test.playing = True
                return True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit':
                self.game.running = False

        # Tells start menu class to stop running because of input to a different menu
        self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.vol_x, self.vol_y = self.mid_w, self.mid_h + 20
        self.controls_x, self.controls_y = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Volume', 15, self.vol_x, self.vol_y)
            self.game.draw_text('Controls', 15, self.controls_x, self.controls_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

        # TODO: Create a Volume Menu from here. Follow same pattern as before for creating a menu
        elif self.game.START_KEY:
            pass


class CreditsMenu(Menu):
    """Credits menu for showing the sources for assets and my name"""

    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by MIDN 3/C Morris', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
