import pygame

GROUND_SIZE = 32


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        # img attr must be a string to the file location for the ground tile
        # Init each ground sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)
