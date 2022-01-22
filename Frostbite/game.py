import pygame
from random import choice
from time import sleep

pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
pygame.display.set_caption("Frostbite Atari")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
timer = 2700

def dist2d(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return d

def distX(x1, x2):
    d = x1-x2
    return d

def distX2(x1,x2):
    d = ((x1-x2)**2)**(1/2)
    return d

#Player
playersprite = pygame.image.load("player.png")
playerX = 400
playerY = 150
playerX_change = 0
jump = pygame.mixer.Sound("jump.wav")

def player(x,y):
    screen.blit(playersprite, (x, y))
    
#Iglo
iglosprite = pygame.image.load("iglo1.png")
igloX = 500
igloY = 75

#Platform
platspritel1 = pygame.image.load("platform.png")
platspritel2 = pygame.image.load("platform.png")
platspritel3 = pygame.image.load("platform.png")
platspritel4 = pygame.image.load("platform.png")
plat1X = -300
plat2X = 320
plat3X = 160
plat4X = 700
plat5X = -240
plat6X = 400
plat7X = 120
plat8X = 700

platl1_change = choice([0.75,1,1.5,1]) * choice([-1,1])
platl2_change = choice([0.75,1,1.5,1]) * choice([-1,1])
platl3_change = choice([0.75,1,1.5,1]) * choice([-1,1])
platl4_change = choice([0.75,1,1.5,1]) * choice([-1,1])

def platl1(x,y):
    screen.blit(platspritel1, (x, y))
def platl2(x,y):
    screen.blit(platspritel2, (x, y))
def platl3(x,y):
    screen.blit(platspritel3, (x, y))
def platl4(x,y):
    screen.blit(platspritel4, (x, y))
    
#Bear
bearsprite = pygame.image.load("bear.png")
bearX = 0
bearY = 150
bearX_change = 3

def bear(x,y):
    screen.blit(bearsprite, (x, y))

#Clam
clamsprite = pygame.image.load("clam.png")
clamX = choice([0,800])
clamY = 330
clamX_change = 1

def clam(x,y):
    screen.blit(clamsprite, (x,y))
    
#Crab
crabsprite = pygame.image.load("crab.png")
crabX = choice([0,800])
crabY = 510
crabX_change = 1

def crab(x,y):
    screen.blit(crabsprite, (x,y))
    
#Fish
fishsprite = pygame.image.load("fish.png")
fishX = choice([0,800])
fishY = 420
fishX_change = 1

def fish(x,y):
    screen.blit(fishsprite, (x,y))
    
#Background
mainscreen = pygame.image.load("mainscreen.png")
blip = pygame.image.load("blip.png")
blipY = 248
blipX = 340
backg = pygame.image.load("background.png")

#Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10

font2 = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x,y):
    scorescreen = font.render(str(score), True, (147, 159, 255))
    screen.blit(scorescreen, (x,y))
    
def show_final_score(x,y):
    scorefinal = font2.render(str(score), True, (0, 0, 0))
    screen.blit(scorefinal, (x,y))

timerX = 10
timerY = 60
def show_timer(x,y):
    timerscreen = font.render(str(timer//60)+"ºC", True, (147,159,255))
    screen.blit(timerscreen, (x,y))
    
#MAIN MENU
move = pygame.mixer.Sound("moveup.flac")
confirm = pygame.mixer.Sound("confirm.wav")
gameover = pygame.mixer.Sound("gameover.wav")
pygame.mixer.init()
pygame.mixer.music.load("menumusic.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

font3 = pygame.font.Font("freesansbold.ttf", 16)


#RESULTS
loss_screen = pygame.image.load("gameover.png")
victory_screen = pygame.image.load("victory.png")
loss = pygame.mixer.Sound("loss.mp3")
wingame = pygame.mixer.Sound("win.mp3")

mains = True
while mains:
    screen.blit(mainscreen, (0,0))
    screen.blit(blip, (blipX, blipY))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN and blipY == 248:
                blipX = 340
                blipY = 300
                move.play()

            elif event.key == pygame.K_UP and blipY == 300:
                blipX = 340
                blipY = 248
                move.play()
            
            if event.key == pygame.K_RETURN and blipY == 248:
                confirm.play()
                sleep(1.25)
                mains = False
                
            elif event.key == pygame.K_RETURN and blipY == 300:
                confirm.play()
                sleep(1.25)
                pygame.quit()
                mains=False
    
    pygame.display.update()

iglo=0
l1press=False
l2press=False
l3press=False
l4press=False
win = False
running = True
while running:
    screen.blit(backg, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #Movement

        if event.type == pygame.KEYDOWN:
            
            #Horizontal movement
            if event.key == pygame.K_LEFT:
                playerX_change=-2.5
            if event.key == pygame.K_RIGHT:
                playerX_change=2.5
                
            #Vertical movement
            if event.key == pygame.K_UP and playerY != 150:
                playerY -= 90
                jump.play()

            elif event.key == pygame.K_DOWN and playerY != 510:
                playerY += 90
                jump.play()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
    
    playerX+=playerX_change

    if clamX>=840 or clamX<=-40:
        clamX_change*=-1
        clamsprite = pygame.transform.flip(clamsprite, True, False)
    clamX+=clamX_change
    
    if crabX>=840 or crabX<=-40:
        crabX_change*=-1
        crabsprite = pygame.transform.flip(crabsprite, True, False)
    crabX-=crabX_change
    
    if fishX>=840 or fishX<=-40:
        fishX_change*=-1
        fishsprite = pygame.transform.flip(fishsprite, True, False)
    fishX+=fishX_change
    
    #Collision
    if dist2d(bearX, bearY, playerX, playerY)<40:
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    if distX2(clamX, playerX)<10 and playerY==330:
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    if distX2(fishX, playerX)<10 and playerY==420:
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    if distX2(crabX, playerX)<10 and playerY==510:
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
        
    #Boundary Check
    if playerX <=0:
        playerX = 0
    elif playerX >=752:
        playerX = 752
    
    if bearX < 0 or bearX>714:
        bearX_change*=-1
        bearsprite = pygame.transform.flip(bearsprite, True, False)
    bearX+=bearX_change
    
 
    #PLATS
    platl1(plat1X, 270)
    platl1(plat2X, 270)
    platl2(plat3X, 360)
    platl2(plat4X, 360)
    platl3(plat5X, 450)
    platl3(plat6X, 450)
    platl4(plat7X, 540)
    platl4(plat8X, 540)
    
    plat1X+=platl1_change
    plat2X+=platl1_change
    plat3X+=platl2_change
    plat4X+=platl2_change
    plat5X+=platl3_change
    plat6X+=platl3_change
    plat7X+=platl4_change
    plat8X+=platl4_change
    
    if plat1X<=-320 or plat2X>=860:
        platl1_change*=-1
    if plat3X<=-320 or plat4X>=860:
        platl2_change*=-1
    if plat5X<=-320 or plat6X>=860:
        platl3_change*=-1
    if plat7X<=-320 or plat8X>=860:
        platl4_change*=-1
        
    #PRESSED
    if playerY==240 and iglo<14 and ((distX(playerX, plat1X)>=-10 and distX(playerX, plat1X)<=300) or (distX(playerX, plat2X)>=-10 and distX(playerX, plat2X)<=300)):
        if l1press == False:
            platspritel1 = pygame.image.load("jumped.png")
            l1press = True
            iglo+=1
            score+=100
    elif playerY==240 and not ((distX(playerX, plat1X)>=-10 and distX(playerX, plat1X)<=300) or (distX(playerX, plat2X)>=-10 and distX(playerX, plat2X)<=300)):
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    if playerY==330 and iglo<14 and ((distX(playerX, plat3X)>=-10 and distX(playerX, plat3X)<=300) or (distX(playerX, plat4X)>=-10 and distX(playerX, plat4X)<=300)):
        if l2press == False:
            platspritel2 = pygame.image.load("jumped.png")
            l2press = True
            iglo+=1
            score+=100
    elif playerY==330 and not ((distX(playerX, plat3X)>=-10 and distX(playerX, plat3X)<=300) or (distX(playerX, plat4X)>=-10 and distX(playerX, plat4X)<=300)):
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
        
    if playerY==420 and iglo<14 and ((distX(playerX, plat5X)>=-10 and distX(playerX, plat5X)<=300) or (distX(playerX, plat6X)>=-10 and distX(playerX, plat6X)<=300)):
        if l3press == False:
            platspritel3 = pygame.image.load("jumped.png")
            l3press = True
            iglo+=1
            score+=100
    elif playerY==420 and not ((distX(playerX, plat5X)>=-10 and distX(playerX, plat5X)<=300) or (distX(playerX, plat6X)>=-10 and distX(playerX, plat6X)<=300)):
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
        
    if playerY==510 and iglo<14 and ((distX(playerX, plat7X)>=-10 and distX(playerX, plat7X)<=300) or (distX(playerX, plat8X)>=-10 and distX(playerX, plat8X)<=300)):
        if l4press == False:
            platspritel4 = pygame.image.load("jumped.png")
            l4press = True
            iglo+=1
            score+=100
    elif playerY==510 and not ((distX(playerX, plat7X)>=-10 and distX(playerX, plat7X)<=300) or (distX(playerX, plat8X)>=-10 and distX(playerX, plat8X)<=300)):
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    if l1press==True and l2press==True and l3press==True and l4press==True:
        l1press=False
        l2press=False
        l3press=False
        l4press=False
        platspritel1 = pygame.image.load("platform.png")
        platspritel2 = pygame.image.load("platform.png")
        platspritel3 = pygame.image.load("platform.png")
        platspritel4 = pygame.image.load("platform.png")
    

    if iglo==2:
        iglosprite = pygame.image.load("iglo2.png")
    if iglo==3:
        iglosprite = pygame.image.load("iglo3.png")
    if iglo==4:
        iglosprite = pygame.image.load("iglo4.png")
    if iglo==5:
        iglosprite = pygame.image.load("iglo5.png")
    if iglo==6:
        iglosprite = pygame.image.load("iglo6.png")
    if iglo==7:
        iglosprite = pygame.image.load("iglo7.png")
    if iglo==8:
        iglosprite = pygame.image.load("iglo8.png")
    if iglo==9:
        iglosprite = pygame.image.load("iglo9.png")
    if iglo==10:
        iglosprite = pygame.image.load("iglo10.png")
    if iglo==11:
        iglosprite = pygame.image.load("iglo11.png")
    if iglo==12:
        iglosprite = pygame.image.load("iglo12.png")
    if iglo==13:
        iglosprite = pygame.image.load("iglo13.png")
    if iglo==14:
        iglosprite = pygame.image.load("iglo14.png")
    if iglo>=1:
        screen.blit(iglosprite, (igloX,igloY))
        
    if iglo==14 and playerY==150:
        win = True
        sleep(2)
        running=False
        
    if timer<=0:
        sleep(0.1)
        gameover.play()
        sleep(2)
        running=False
    
    #ENEMIES
    bear(bearX, bearY)
    clam(clamX, clamY)
    crab(crabX, crabY)
    fish(fishX, fishY)
    player(playerX, playerY)
    show_score(scoreX, scoreY)
    show_timer(timerX, timerY)
    timer-=1
    
    clock.tick(60)
    pygame.display.update()
    
results = True
if win == False:
    pygame.mixer.music.load("loss.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
else:
    score+=(timer//60)*20
    pygame.mixer.music.load("win.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
while results:
    if win == False:
        screen.blit(loss_screen, (0,0))
    else:
        screen.blit(victory_screen, (0,0))
    
    show_final_score(320,165)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                confirm.play()
                sleep(1)
                pygame.quit()
                results=False
    
    pygame.display.update()