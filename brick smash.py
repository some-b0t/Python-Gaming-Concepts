import pygame
from paddleclass import paddle

pygame.init()

WIDTH=1200
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Brick Smash")

gameloop=True
FPS=20
clock=pygame.time.Clock()

gamepaddle=paddle(WIDTH,HEIGHT)

while gameloop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False
        
    gamepaddle.update(event)

    screen.fill("black")
    gamepaddle.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()