import pygame
import game_test


class Chara2(pygame.sprite.Sprite):
    def __init__(self, g_game, image, pos):
        pygame.sprite.Sprite.__init__(self)
        # Allow for access to the screen rect and position arguments
        self.screen = g_game.screen
        self.screen_rect = self.screen.get_rect()

        # Sets the charaters image and transforms it to look right
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (54, 54))
        self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)

        # gets the rect for the image
        self.rect = self.image.get_rect()

        # Sets position for character
        self.pos = pos
        self.rect.midbottom = self.pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # jumping flags
        self.moving_up = False
        self.moving_down = False

        # physics variables using an arbitrary 'gravity' value to
        # simulate the increase/decrease in acceleration away/towards the ground.
        self.jump_height = 20
        self.gravity = 1
        self.up_speed = self.jump_height
        self.falling = True

    def jump(self):
        # Function to  make the character jump. This is run when jumping is set to true.
        if game_test.jumping_2:
            self.y -= self.up_speed
            self.up_speed -= self.gravity
            if self.up_speed < - self.jump_height:
                game_test.jumping_2 = False
                self.up_speed = self.jump_height
            self.rect.midbottom = self.pos

    def update(self):
        """Update the characters rect position"""
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
