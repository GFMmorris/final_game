import pygame
import game_test


class Chara(pygame.sprite.Sprite):
    def __init__(self, g_game):
        pygame.sprite.Sprite.__init__(self)
        # Allow for access to the screen rect and position arguments
        self.screen = g_game.screen
        self.screen_rect = self.screen.get_rect()

        # Sets the charaters image and transforms it to look right
        self.image = pygame.image.load('images/Characters/chara_1_stand.png')
        self.image = pygame.transform.scale(self.image, (54, 54))
        self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)

        # gets the rect for the image
        self.rect = self.image.get_rect()

        # Sets position for character
        self.rect.midbottom = (100, 300)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # jumping flags
        self.moving_up = False
        self.moving_down = False

        # physics variables
        self.jump_height = 20
        self.gravity = 1
        self.up_speed = self.jump_height

    def jump(self):
        start_position = self.rect.midbottom
        if game_test.jumping:
            self.y -= self.up_speed
            self.up_speed -= self.gravity
            if self.y == start_position:
                game_test.jumping = False

    def update(self):
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def _chara_run(self):
        self.image1 = pygame.image.load('images/Characters/chara_1_stand.png')
        self.image1 = pygame.transform.scale(self.image, (96, 96))
        self.image1 = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
