import sys, pygame

pygame.init()


white = (255, 255, 255)

class Bricks(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
    	pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        pygame.draw.rect(self.image, color, [40, 40, width, height])
        self.rect = self.image.get_rect()
