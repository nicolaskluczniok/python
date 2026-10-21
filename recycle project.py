import pygame
import random
pygame .init()
import time

screen = pygame.display.set_mode((800,800))
background = pygame.image.load("C:/Users/nicol/OneDrive/python/images/background.png")
backgroundimage = pygame.transform.scale(background,(800,800))
gameover = pygame.image.load("C:/Users/nicol/OneDrive/python/images/gameover.png")
gameoverimage = pygame.transform.scale(gameover,(800,800))

class non(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/bottle.png")
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0,700),random.randint(0,700)]

recycle1 = ["cardboard.png","pensil.png","straw.png"]


class recycle(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/"+random.choice(recycle1))
       self.image = pygame.transform.scale(self.image,(75,75))
       self.rect = self.image.get_rect()
       self.rect.center = [random.randint(0,600),random.randint(0,600)]

score = 0
Lives = 3

class bin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:/Users/nicol/OneDrive/python/images/bin.png")
        self.image = pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]
    def update(self):
        global score
        global Lives
        key = pygame.key.get_pressed()
        if key [pygame.K_RIGHT]:
            self.rect.x  += 10
        if key [pygame.K_LEFT]:
            self.rect.x -= 10
        if key [pygame.K_UP]:
            self.rect.y -= 10
        if key [pygame.K_DOWN]:
            self.rect.y += 10
        collide = pygame.sprite.spritecollide(self,recyclegroup,True)
        for i in collide:
            score += 1
        if pygame.sprite.spritecollide(self,nongroup,True):
            Lives -= 1
        


bin1 = bin()
bingroup = pygame.sprite.Group()
bingroup.add(bin1)
recyclegroup = pygame.sprite.Group()
nongroup = pygame.sprite.Group()

for i in range(30):
    recycle2 = recycle()
    recyclegroup.add(recycle2)
for i in range(5):
    non2 = non()
    nongroup.add(non2)
    
    
while True:
    font = pygame.font.SysFont("ariel",75)
    text = font.render(str(score),True,"Purple")
    text1 = font.render("lives",True,"Black")
    text2 = font.render(str(Lives),True,"Red")
    text3 = font.render("score",True,"Black")
    
    screen.blit(backgroundimage,(0,0))
    screen.blit(text,(750,0))
    screen.blit(text1,(0,0))
    screen.blit(text2,(130,0))
    screen.blit(text3,(600,0))
    recyclegroup.draw(screen)
    nongroup.draw(screen)
    bingroup.draw(screen)
    bingroup.update()
    if Lives == 0:
        screen.fill("black")
        screen.blit(gameoverimage,(0,0))
        pygame.display.update()
        time.sleep(2.5)
        pygame.quit()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()