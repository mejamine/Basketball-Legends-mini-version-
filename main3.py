import pygame
from pygame.locals import *
import player
import random
pygame.init()
pygame.key.set_repeat(400, 30)
fen = pygame.display.set_mode((1180,670))
fon = pygame.image.load("background.png").convert()
fen.blit(fon,(0,0))
bute1=0
bute2=0
score1 = pygame.font.SysFont(None,60)
img1= score1.render('KOBE', True,BLEND_ADD)
score2 = pygame.font.SysFont(None,60)
img2= score2.render('GIANNIS', True,BLEND_ADD)
rim1 = pygame.image.load("rim1.png").convert_alpha()
rim2 = pygame.image.load("rim2.png").convert_alpha()
b1 = pygame.image.load("ball.png").convert_alpha()
b1recto=b1.get_rect()
b1recto.topleft=(560,510)
player1 = pygame.image.load("giannis.png").convert_alpha()
player2 = pygame.image.load("kobe.png").convert_alpha()
p1=player.Player(620,370,player1)
p2=player.Player(460,370,player2)
player1recto=player1.get_rect()
player1recto.topleft=(p1.x,p1.y)
player2recto=player2.get_rect()
player2recto.topleft=(p2.x,p2.y)
continuer = True
x=random.randrange(2)
if x==1:
    p1.ballholder=0
    p2.ballholder=1
elif x==0:
    p1.ballholder=1
    p2.ballholder=0
t=True
y=0
shooter=-1
score=0
while continuer:
    score11 = pygame.font.SysFont(None, 60)
    img3 = score11.render(str(bute2), True, BLEND_ADD)
    score12 = pygame.font.SysFont(None, 60)
    img4 = score12.render(str(bute1), True, BLEND_ADD)
    if p1.ballholder==1:
        b1recto.left=(player1recto.left-60)
    if p2.ballholder==1:
        b1recto.left=(player2recto.left+100)

    y=y+1
    if y%2==0 and t==True:
        b1recto.top=b1recto.top+80
    elif y%2==1 and t==True:
        b1recto.top=b1recto.top-80
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_f:
                if player2recto.left<=1075 and (player1recto.left-player2recto.left>=120 or player2recto.left-player1recto.left>=110):
                    player2recto=player2recto.move(10,0)
            if event.key==K_s:
                if player2recto.left>=15 and (player2recto.left-player1recto.left>=120 or player1recto.left-player2recto.left>=110) :
                    player2recto=player2recto.move(-10,0)
            if event.key == K_d:
                if p2.ballholder==0 and player1recto.left-player2recto.left<=140:
                    p2.ballholder=1
                    p1.ballholder=0
            if event.key == K_e:
                if p2.ballholder==1:
                    pp2=b1recto.left
                    p2.ballholder=0
                    t=False
                    shooter=2
            if event.key ==K_DOWN:
                if p1.ballholder==0 and player1recto.left-player2recto.left<=140:
                    p2.ballholder=0
                    p1.ballholder=1
            if event.key == K_LEFT:
                if player1recto.left>=15  and (player1recto.left-player2recto.left>=120 or player2recto.left-player1recto.left>=110):
                    player1recto=player1recto.move(-10,0)
            if event.key ==K_RIGHT:
                if player1recto.left<=1075 and (player2recto.left-player1recto.left>=120 or player1recto.left-player2recto.left>=110):
                    player1recto = player1recto.move(10, 0)
            if event.key == K_UP:
                if p1.ballholder==1:
                    shooter=1
                    p1.ballholder=0
                    pp1=b1recto.left
                    t=False
    score = max(bute1, bute2)
    if shooter==1:
        xintervalle1=b1recto.left-60
        yintervalle1=b1recto.top-180
        targety1=180
        targetx1=150
        x1=xintervalle1/15
        y1=yintervalle1/10
        if b1recto.left >= 100:
            if b1recto.top>=80:
                b1recto.top=b1recto.top-y1
                b1recto.left=b1recto.left-x1
            elif b1recto.top<80:
                b1recto.left=b1recto.left-x1
                b1recto.top=b1recto.top+y1
        elif b1recto.left<100 and b1recto.top<=600:
            b1recto.top=b1recto.top+10
        else:
            bute1=bute1+1
            b1recto.topleft = (560,510)
            p1.ballholder = 0
            p2.ballholder = 1
            player1recto.topleft = (p1.x, p1.y)
            player2recto.topleft = (p2.x, p2.y)
            shooter=0
            t=True
    elif shooter==2:
        xintervalle2 = 1000-b1recto.left+45
        yintervalle2 = b1recto.top - 180
        targety2 = 180
        targetx2 = 1020
        x2=xintervalle2/15
        y2=yintervalle2/10
        if b1recto.left <=1025:
            if b1recto.top >= 80:
                b1recto.top=b1recto.top-y2
                b1recto.left=b1recto.left+x2
            elif b1recto.top<80:
                b1recto.left=b1recto.left+x2
                b1recto.top=b1recto.top+y2
        elif b1recto.left>1025 and b1recto.top<=600:
            b1recto.top=b1recto.top+10
        else:
            bute2=bute2+1
            b1recto.topleft = (560, 510)
            p1.ballholder=1
            p2.ballholder=0
            player1recto.topleft = (p1.x, p1.y)
            player2recto.topleft = (p2.x, p2.y)
            shooter=0
            t=True
    if score==2:
        if bute1==2:
            winner='giannis'
            import resultatgiannis
            resultatgiannis
        elif bute2==2:
            import resultatkobe
            resultatkobe
            winner='kobe'



    fen.blit(fon, (0, 0))
    fen.blit(img1, (400, 10))
    fen.blit(img2,(600,10))
    fen.blit(img3,(480,60))
    fen.blit(img4,(670,60))
    fen.blit(rim1, (0, 120))
    fen.blit(rim2, (1000, 120))
    fen.blit(player1,player1recto)
    fen.blit(player2,player2recto)
    fen.blit(b1,b1recto)
    pygame.display.update()
pygame.quit()