import sys, pygame
from paddle import Paddle

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
GREEN = (20, 255, 140)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ball = pygame.transform.scale(ball, (25, 25))
ballrect = ball.get_rect(center=(320,240))


all_sprites_list = pygame.sprite.Group()
paddle = Paddle(GREEN, 40, 10)
all_sprites_list.add(paddle)
print all_sprites_list

while 1:
    all_sprites_list.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    all_sprites_list.draw(screen)
    screen.blit(ball, ballrect)
    pygame.display.flip()