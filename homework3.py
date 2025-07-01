import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Midas Touch")
screen.fill("white")
gameloop=True

midasx=300
midasy=300
midasposition=(midasx,midasy,20,20)
box1position=(550,550,50,50)
box2position=(0,550,50,50)
box3position=(550,0,50,50)
box4position=(0,0,50,50)

b1c="red"
b2c="blue"
b3c="yellow"
b4c="purple"

m=pygame.draw.rect(screen,"green",midasposition)
b1=pygame.draw.rect(screen,b1c,box1position)
b2=pygame.draw.rect(screen,b2c,box2position)
b3=pygame.draw.rect(screen,b3c,box3position)
b4=pygame.draw.rect(screen,b4c,box4position)


midas_dx=0
midas_dy=0

speed=10
FPS=20
clock=pygame.time.Clock()

sound=pygame.mixer.Sound("lesson1/magical-twinkle-242245.mp3")

while gameloop:
    screen.fill("#FFFFFF")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            midas_dx=0
            midas_dy=-1*speed
        if event.key == pygame.K_DOWN:
            midas_dx=0
            midas_dy=1*speed
        if event.key == pygame.K_LEFT:
            midas_dx=-1*speed
            midas_dy=0
        if event.key == pygame.K_RIGHT:
            midas_dx=1*speed
            midas_dy=0

    midasx=midasx+midas_dx
    midasy=midasy+midas_dy
    midasposition=(midasx,midasy,20,20)

    m=pygame.draw.rect(screen,"green",midasposition)
    b1=pygame.draw.rect(screen,b1c,box1position)
    b2=pygame.draw.rect(screen,b2c,box2position)
    b3=pygame.draw.rect(screen,b3c,box3position)
    b4=pygame.draw.rect(screen,b4c,box4position)

    if m.colliderect(b1):
        b1c="gold"
        sound.play()
    if m.colliderect(b2):
        b2c="gold"
        sound.play()
    if m.colliderect(b3):
        b3c="gold"
        sound.play()
    if m.colliderect(b4):
        b4c="gold"
        sound.play()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()