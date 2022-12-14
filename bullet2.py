# bullet class file

import pygame
from pygame.sprite import Sprite


class Bullet2(Sprite):
    """A Class to manage bullets from the chara"""

    def __init__(self, g_game):
        super().__init__()
        self.screen = g_game.screen
        self.image = pygame.image.load('images/TilesShips/single_bom.png')
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.image_x = self.image.get_width()
        self.image_y = self.image.get_height()

        # bullet settings
        self.bullet_speed = 8
        self.bullets_allowed = 3

        # bullet position data
        self.rect = pygame.Rect(50, 0, self.image_x, self.image_y)
        self.rect.midright = g_game.chara_2.rect.midright
        self.x = float(self.rect.x)

    def update(self, birds):
        """Move the bullet across the screen"""
        # Update the decimal position of the bullet
        collision = pygame.sprite.spritecollide(self, birds, True)
        self.x += self.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def make_bullet(self):
        self.screen.blit(self.image, self.rect)
