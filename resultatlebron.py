import pygame
from pygame.locals import *
pygame.init()
fen = pygame.display.set_mode((1180,670))
fon = pygame.image.load("background.png").convert()
fen.blit(fon,(0,0))
replay=pygame.image.load("replay.png").convert_alpha()
resultat = pygame.font.SysFont(None, 60)
res = resultat.render("the winner is Lebron", True, BLEND_ADD)
fen.blit(res,(450,100))
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
replay_button=Button(390,450,replay)
continuer = True
while continuer:
    if replay_button.draw():
        if replay_button.clicked==True :
            import start
            start
    for evennement in pygame.event.get():
        if evennement.type == QUIT:
            continuer = False
    pygame.display.update()
pygame.quit()