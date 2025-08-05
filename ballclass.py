import pygame

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1200

class ball(pygame.sprite.Sprite):
    def __init__(self):
        self.image=pygame.image.load("lesson1/download__1_-removebg-preview (1).png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.centerx=WINDOW_WIDTH//2
        self.rect.centery=WINDOW_HEIGHT//2
        self.speed_x=10
        self.speed_y=10
    def update(self):
        self.rect.x=self.speed_x
        self.rect.y=self.speed_y
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1