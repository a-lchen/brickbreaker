import sys, pygame

pygame.init()


white = (255, 255, 255)

class Bricks(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

brick1 = Bricks(white, 30, 15)