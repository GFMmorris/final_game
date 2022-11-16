# File that runs the video game loop
# imports 
import sys
from time import sleep

import pygame


class EscapeSpace:
    """General class for the entire game. this will run all important methods and functions for the game."""
    def __init(self):
        """initialize pygame for the game space"""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key-presses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()


