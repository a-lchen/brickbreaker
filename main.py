import sys, pygame
from paddle import Paddle
from bricks import Bricks

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
GREEN = (20, 255, 140)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ball = pygame.transform.scale(ball, (25, 25))
ballrect = ball.get_rect(center=(320,240))

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

all_sprites_list = pygame.sprite.Group()
paddle = Paddle(GREEN, 40, 10, 0, 470)
all_sprites_list.add(paddle)

brick_list = []
for i in range(16):
    x = i*40
    y = 0
    brick = Bricks(RED, 39, 9, x, y)
    brick_list.append(brick)
    all_sprites_list.add(brick)

while 1:
    all_sprites_list.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if (paddle.bounce(ballrect)):
        speed[1] = -speed[1]

    paddle.handle_keys()
    screen.fill(black)
    all_sprites_list.draw(screen)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    for i in range(len(brick_list)):
        if brick_list[i].bounce(ballrect):
            speed[1] = -speed[1]
            all_sprites_list.remove(brick_list.pop(i))
            break


