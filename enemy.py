# This file houses all the enemy classes
import pygame
import game_test
from pygame.sprite import Sprite


class Bird(Sprite):
    """Enemy Class of flying metal bird"""

    def __init__(self, g_game):
        super().__init__()
        # Init image and also find the rect and the image
        self.screen = g_game.screen
        self.image = pygame.image.load('images/Characters/metal_fly.png')
        self.rect = self.image.get_rect()
        self.image_x = self.image.get_width()
        self.image_y = self.image.get_height()

        # start position for each bird
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # position data x, and y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movment data
        self.bird_speed = 3

    def update(self):
        """Update the position of the bird"""
        self.x -= self.bird_speed
