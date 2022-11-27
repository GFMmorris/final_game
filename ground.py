import pygame

GROUND_SIZE = 64


class Ground(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        super().__init__()

        self.image = pygame.image.load('images/Tiles/dirt_top_middle.png')
        self.image = pygame.transform.scale(self.image, (GROUND_SIZE,GROUND_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = [startx, starty]
        # img attr must be a string to the file location for the ground tile
        # Init each ground sprite

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
