# This file houses all the enemy classes
import pygame
from pygame.sprite import Sprite
from random import randint


class Bird(Sprite):
    """Enemy Class of flying metal bird"""

    def __init__(self, g_game):
        super().__init__()
        # Init image and also find the rect and the image
        self.screen = g_game.screen
        self.image = pygame.image.load('images/Characters/metal_fly.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.image_x = self.image.get_width()
        self.image_y = self.image.get_height()

        # start position for each bird
        self.rect.x = 645
        self.rect.y = randint(32, 255)

        # position data x, and y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movment data
        self.bird_speed = 3

    def update(self, counter):
        """Update the position of the bird"""
        # update(self, counter)
        # Ryan S helped me get the birds to move and also helped with a level modification
        # counter loop
        if counter % 100 == 0:
            self.bird_speed += self.bird_speed * 0.5
        self.rect.x -= self.bird_speed

    def draw(self):
        """Draw the enemy on the screen"""
        self.screen.blit(self.image, self.rect)
