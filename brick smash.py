import pygame
from paddleclass import paddle
from ballclass import ball

pygame.init()

WIDTH=1200
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

gameloop=True
FPS=20
clock=pygame.time.Clock()

ball_group=pygame.sprite.Group()

paddle_group=pygame.sprite.Group()

gamepaddle=paddle(WIDTH,HEIGHT)
gameball=ball()

ball_group.add(gameball)
paddle_group.add(gamepaddle)

while gameloop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

    ball_group.update()
    paddle_group.update(event)

    screen.fill("black")
    paddle_group.draw(screen)
    ball_group.draw(screen)
    pygame.display.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()