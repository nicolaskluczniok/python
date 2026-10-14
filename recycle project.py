import pygame
import random

screen = pygame.display.set_mode((800,800))
background = pygame.image.load("C:/Users/nicol/OneDrive/python/images/background.png")
backgroundimage = pygame.transform.scale(background,(800,800))

class non(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprites.__init__(self)
        self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/bottle.png")
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0,800),random.randint(0,800)]

recycle1 = ["cardboard.png","pensil.png","straw.png"]


class recycle(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/"+random.choice(recycle1))
       self.image = pygame.transform.scale(self.image,(75,75))
       self.rect = self.image.get_rect()
       self.rect.center = [random.randint(0,800),random.randint(0,800)]

score = 0

class bin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/bin.png")
        self.image = pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]
    def update(self):
        global score
        key = pygame.key.get_pressed()
        if key [pygame.K_RIGHT]:
            self.rect.x  += 10
        if key [pygame.K_LEFT]:
            self.rect.x -= 10
        if key [pygame.K_UP]:
            self.rect.y -= 10
        if key [pygame.K_DOWN]:
            self.rect.y += 10
        if pygame.sprite.spritecollide(self,recyclegroup,True):
            score += 1


bin1 = bin()
bingroup = pygame.sprite.Group()
bingroup.add(bin1)
recyclegroup = pygame.sprite.Group()

for i in range(30):
    recycle2 = recycle()
    recyclegroup.add(recycle2)


while True:
    screen.blit(backgroundimage,(0,0))
    recyclegroup.draw(screen)
    bingroup.draw(screen)
    bingroup.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    