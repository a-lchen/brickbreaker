import sys, pygame

pygame.init()


white = (255, 255, 255)

class Bricks(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
    	pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, [40, 40, width, height])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def bounce(self, ballrect):
    	if ballrect.colliderect(self.rect):
    		return True
    	return False



