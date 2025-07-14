import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("The Great Escape")

gameloop=True

speed=5
FPS=20
clock=pygame.time.Clock()

a=pygame.draw.rect(screen,"red",(0,0,20,600))
b=pygame.draw.rect(screen,"red",(0,0,800,20))
c=pygame.draw.rect(screen,"red",(0,580,800,20))
d=pygame.draw.rect(screen,"red",(780,0,20,600))
e=pygame.draw.rect(screen,"red",(30,0,20,200))
f=pygame.draw.rect(screen,"red",(80,0,20,400))
g=pygame.draw.rect(screen,"red",(400,20,20,350))
h=pygame.draw.rect(screen,"red",(200,0,400,20))
i=pygame.draw.rect(screen,"red",(200,0,20,350))
j=pygame.draw.rect(screen,"red",(0,400,430,20))
k=pygame.draw.rect(screen,"red",(0,400,350,20))
l=pygame.draw.rect(screen,"red",(0,500,20,100))
m=pygame.draw.rect(screen,"red",(0,200,20,50))
n=pygame.draw.rect(screen,"red",(0,200,200,20))
o=pygame.draw.rect(screen,"red",(0,580,20,400))
p=pygame.draw.rect(screen,"red",(700,0,200,20))
q=pygame.draw.rect(screen,"red",(450,0,400,20))
r=pygame.draw.rect(screen,"red",(0,520,20,250))
s=pygame.draw.rect(screen,"red",(0,100,20,100))
t=pygame.draw.rect(screen,"red",(500,0,300,20))
u=pygame.draw.rect(screen,"red",(0,500,300,20))
v=pygame.draw.rect(screen,"red",(700,0,300,20))
w=pygame.draw.rect(screen,"red",(500,0,250,20))
x=pygame.draw.rect(screen,"red",(500,0,400,0))
x=pygame.draw.rect(screen,"red",(600,0,20,400))
y=pygame.draw.rect(screen,"red",(700,0,20,500))
z=pygame.draw.rect(screen,"green",(150,250,25,25))

character_x=760
character_y=40

character=pygame.draw.rect(screen,"white",(character_x,character_y,10,10))

character_dx=0
character_dy=0

gameover=False

gamewon=False

f=pygame.font.SysFont("Times New Roman MS",50)
f1=pygame.font.SysFont("TImes New Roman MS",50)

wo=f1.render("You Win!",True,"green")
wr=wo.get_rect()
wr.center=(400,300)

go=f.render("Game Over!",True,"white")
gr=go.get_rect()
gr.center=(400,300)

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                character_dx=-25
                character_dy=0
            if event.key==pygame.K_RIGHT:
                character_dx=25
                character_dy=0
            if event.key==pygame.K_UP:
                character_dx=0
                character_dy=-25
            if event.key==pygame.K_DOWN:
                character_dx=0
                character_dy=25
                
    if character.colliderect(a):
        gameover=True
    if character.colliderect(b):
        gameover=True
    if character.colliderect(c):
        gameover=True
    if character.colliderect(d):
        gameover=True
    if character.colliderect(e):
        gameover=True
    if character.colliderect(g):
        gameover=True
    if character.colliderect(h):
        gameover=True
    if character.colliderect(i):
        gameover=True
    if character.colliderect(j):
        gameover=True
    if character.colliderect(k):
        gameover=True
    if character.colliderect(l):
        gameover=True
    if character.colliderect(m):
        gameover=True
    if character.colliderect(n):
        gameover=True
    if character.colliderect(o):
        gameover=True
    if character.colliderect(p):
        gameover=True
    if character.colliderect(q):
        gameover=True
    if character.colliderect(r):
        gameover=True
    if character.colliderect(s):
        gameover=True
    if character.colliderect(t):
        gameover=True
    if character.colliderect(u):
        gameover=True
    if character.colliderect(v):
        gameover=True
    if character.colliderect(w):
        gameover=True
    if character.colliderect(x):
        gameover=True
    if character.colliderect(y):
        gameover=True
    if character.colliderect(z):
        gamewon=True

    if gameover:
        screen.fill("black")
        screen.blit(go,gr)
        pygame.display.update()
        pygame.time.delay(2500)
        gameloop=False
        
    if gamewon:
        screen.blit(wo,wr)
        pygame.display.update()
        pygame.time.delay(4000)
        gameloop=False

    character_x=character_x+character_dx
    character_y=character_y+character_dy

    a=pygame.draw.rect(screen,"red",(0,0,20,600))
    b=pygame.draw.rect(screen,"red",(0,0,800,20))
    c=pygame.draw.rect(screen,"red",(0,580,800,20))
    d=pygame.draw.rect(screen,"red",(780,0,20,600))
    e=pygame.draw.rect(screen,"red",(30,0,20,200))
    f=pygame.draw.rect(screen,"red",(80,0,20,400))
    g=pygame.draw.rect(screen,"red",(400,20,20,350))
    h=pygame.draw.rect(screen,"red",(200,0,400,20))
    i=pygame.draw.rect(screen,"red",(200,0,20,350))
    j=pygame.draw.rect(screen,"red",(0,400,430,20))
    k=pygame.draw.rect(screen,"red",(0,400,350,20))
    l=pygame.draw.rect(screen,"red",(0,500,20,100))
    m=pygame.draw.rect(screen,"red",(0,200,20,50))
    n=pygame.draw.rect(screen,"red",(0,200,200,20))
    o=pygame.draw.rect(screen,"red",(0,580,20,400))
    p=pygame.draw.rect(screen,"red",(700,0,200,20))
    q=pygame.draw.rect(screen,"red",(450,0,400,20))
    r=pygame.draw.rect(screen,"red",(0,520,20,250))
    s=pygame.draw.rect(screen,"red",(0,100,20,100))
    t=pygame.draw.rect(screen,"red",(500,0,300,20))
    u=pygame.draw.rect(screen,"red",(0,500,300,20))
    v=pygame.draw.rect(screen,"red",(700,0,300,20))
    w=pygame.draw.rect(screen,"red",(500,0,250,20))
    x=pygame.draw.rect(screen,"red",(500,0,400,0))
    x=pygame.draw.rect(screen,"red",(600,0,20,400))
    y=pygame.draw.rect(screen,"red",(700,0,20,500))
    z=pygame.draw.rect(screen,"green",(150,250,25,25))
    character=pygame.draw.rect(screen,"white",(character_x,character_y,10,10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()