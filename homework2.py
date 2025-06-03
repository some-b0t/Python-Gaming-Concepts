import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("initials")
gameloop=True
while gameloop:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    d=pygame.draw.rect(screen,"blue",(200,50,50,500))
    a=pygame.draw.rect(screen,"red",(200,50,300,50))
    b=pygame.draw.rect(screen,"green",(200,300,300,50))
    c=pygame.draw.rect(screen,"yellow",(200,550,300,50))
    pygame.display.flip()
pygame.quit()
