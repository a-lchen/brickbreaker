import pygame
WHITE = (255, 255, 255)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height,x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        pygame.draw.rect(self.image, color, [0,0,width, height])
        # self.rect.x = 200
        
        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-dist, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(dist, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -dist)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, dist)

    def bounce(self, r):
        if (r.colliderect(self.rect)):
            return True
        return False