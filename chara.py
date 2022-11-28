import pygame


class Chara(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Characters/chara_1_stand.png')
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)

        self.rect = self.image.get_rect()


    def update(self, screen):
        screen.blit(self.image, self.rect)

    def _chara_run(self):
        self.image1 = pygame.image.load('images/Characters/chara_1_stand.png')
        self.image1 = pygame.transform.scale(self.image, (96, 96))
        self.image1 = pygame.transform.flip(self.image, flip_x=True, flip_y=False)