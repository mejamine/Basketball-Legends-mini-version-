import pygame
from pygame.locals import *
pygame.init()
fen = pygame.display.set_mode((1180,670))
fon = pygame.image.load("background.png").convert()
fen.blit(fon,(0,0))
start = pygame.image.load("button.png").convert_alpha()
kobe = pygame.image.load("kobe_button.png").convert_alpha()
lebron = pygame.image.load("lebron_button.png").convert_alpha()
wade = pygame.image.load("wade_button.png").convert_alpha()
giannis = pygame.image.load("giannis_button.png").convert_alpha()
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked=False
    def draw(self):
        action = False
        fen.blit(self.image,(self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked==False:
                self.clicked=True
                action=True
        return(action)
kobe_button=Button(20,20,kobe)
lebron_button=Button(20,240,lebron)
wade_button=Button(760,20,wade)
giannis_button=Button(760,240,giannis)
start_button=Button(390,450,start)
continuer = True
while continuer:
    if start_button.draw():
        if lebron_button.clicked==True and giannis_button.clicked==True :
            import main1
            main1
        elif lebron_button.clicked==True and wade_button.clicked==True:
            import main2
            main2
        elif kobe_button.clicked==True and giannis_button.clicked==True:
            import main3
            main3
        elif kobe_button.clicked==True and wade_button.clicked==True:
            import main4
            main4
    lebron_button.draw()
    wade_button.draw()
    kobe_button.draw()
    giannis_button.draw()
    for evennement in pygame.event.get():
        if evennement.type == QUIT:
            continuer = False
    pygame.display.update()
pygame.quit()