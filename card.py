import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
card = pygame.image.load("images/card.jpg")
cardimage = pygame.transform.scale(card,(500,500))
birthday = pygame.image.load("images/birthday.png")
birthday = pygame.transform.scale(birthday,(250,250))
birthdaypin = pygame.image.load("images/birthdaypin.png")
birthdaypin = pygame.transform.scale(birthdaypin,(40,40))
font = pygame.font.SysFont("ariel",35)
font1 = pygame.font.SysFont("ariel",60)
text = font.render("Happy birthday",True,"yellow")
text1 = font1.render("Sam",True,"yellow")
while True:
    screen.blit(cardimage,(0,0))
    screen.blit(birthday,(300,300))
    screen.blit(birthdaypin,(430,420))
    screen.blit(text,(160,150))
    screen.blit(text1,(180,180))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
