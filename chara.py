import pygame


class Chara(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Characters/chara_1_stand.png')
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200

    def draw(self, screen):
        screen.blit(self.image, (700, 750))
