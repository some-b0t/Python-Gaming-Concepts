#importing module
import pygame
import random
#initializing module
pygame.init()

#setting up display window
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Tron Light Cycle")

#creating gameloop
gameloop=True

#creating bike
headx=300
heady=300
bikeposition=(headx,heady,15,15)
bike=pygame.draw.rect(screen,"darkblue",bikeposition)

bike_dx=0
bike_dy=0

speed=8
FPS=20
clock=pygame.time.Clock()

body=[]

score=0

f=pygame.font.SysFont("Times New Roman MS",30)
f1=pygame.font.SysFont("Times New Roman MS",50)

go=f1.render("Game Over",True,"black")
gr=go.get_rect()
gr.center=(300,300)

gameover=False

#events in gameloop
while gameloop:

    #allowing window to close on input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            bike_dx=0
            bike_dy=-1*speed
        if event.key == pygame.K_DOWN:
            bike_dx=0
            bike_dy=1*speed
        if event.key == pygame.K_LEFT:
            bike_dx=-1*speed
            bike_dy=0
        if event.key == pygame.K_RIGHT:
            bike_dx=1*speed
            bike_dy=0

    score=score+1

    headx=headx+bike_dx
    heady=heady+bike_dy
    bikeposition=(headx,heady,15,15)
    body.append(bikeposition)
        


    if gameover:
        screen.fill("lightblue")
        screen.blit(go,gr)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False

    #coloring screen
    st=f.render("Score ="+str(score),True,"darkgrey")
    sr=st.get_rect()
    sr.topleft=(30,30)
    screen.blit(st,sr)
    screen.fill("lightblue")

    for parts in body:
        pygame.draw.rect(screen,"blue",parts)

    #creating bike
    bike=pygame.draw.rect(screen,"darkblue",bikeposition)
    
    pygame.display.flip()
    clock.tick(FPS)

#closing the game window
pygame.quit()