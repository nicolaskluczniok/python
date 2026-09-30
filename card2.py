import pygame
pygame .init()

screen = pygame.display.set_mode((500,500))
card = pygame.image.load("C:/Users/nicol/OneDrive/python/images/card2.jpg")
flower = pygame.image.load("C:/Users/nicol/OneDrive/python/images/flower.png")
cardimage = pygame.transform.scale(card,(500,500))
flowerimage = pygame.transform.scale(flower,(100,100))
font = pygame.font.SysFont("ariel",75)
text = font.render("hi card",True,"yellow") 
y = 50 

while True:
    y += 0.001
    screen.blit(cardimage,(0,0))
    screen.blit(flowerimage,(50,y))
    screen.blit(text,(120,150))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
            