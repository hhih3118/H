import pygame
import sys
import random
import time

pygame.init()
pygame.display.set_caption('fdzz')
myFont = pygame.font.Font('KCC-Chassam.ttf', 70)
smallFont = pygame.font.Font('KCC-Chassam.ttf', 50)
bgfont = pygame.font.Font('JalnanGothicTTF.ttf',70)
start = pygame.font.Font('JalnanGothicTTF.ttf',50)

#size = screen_width, screen_height = 1600, 600
#size = screen_width, screen_height = 800, 600
size = screen_width, screen_height = 1600, 900

screen = pygame.display.set_mode(size)

bg = pygame.image.load("ㄷ.png")
mo1 = pygame.image.load("ee.png")
mo2 = pygame.image.load("ㄹ.png")
sin = pygame.image.load("ㅁ.png")
gu = pygame.image.load("ㅂ.png")
gu = pygame.transform.scale(gu, (1200,800))

sin2 = pygame.image.load("신문.png")
plus = pygame.image.load("더하기.png")
plus2 = pygame.image.load("더하기.png")
minus = pygame.image.load("빼기.png")
bgg = pygame.image.load("fff.png")
money = 5000
gasu = 0
chgasu = 0
#263 520 228 320
def purchase():
    global money, gasu, chgasu
    screen.blit(bg,(0,0))
    screen.blit(gu,(200,50))
    don = smallFont.render("{0}".format(money), True,(100,255,255))
    screen.blit(don,(300,200))
    jusikgaesu = smallFont.render("{0}".format(gasu), True,(255,255,255))

    screen.blit(jusikgaesu,(300,600))
    screen.blit(plus,(400,400))
    screen.blit(plus2,(500,600))
    screen.blit(minus,(600,600))
    gasufont = smallFont.render("총 개수: {0}".format(chgasu),True,(255,255,255))

    screen.blit(gasufont,(350,600))
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a , b = pygame.mouse.get_pos()
                if 400< a < 500 and 400 < b < 500:
                    money += 100
                    purchase()
                elif 500 < a < 600 and 600 < b < 700:
                    gasu += 1
                    purchase()
                elif 600 < a < 700 and 600 < b < 700:
                    money = money - gasu * 100
                    chgasu = chgasu + gasu
                    gasu = 0
                    purchase()
                else:
                    second()
        
        pygame.display.update()



def ending():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                first()
        screen.fill((200,0,0))
        pygame.display.update()

def first():
    Text = bgfont.render("펀드매니저로 살아남기", True,(255,255,255))
    startfont = start.render("출근하기",True,(255,255,255))
    secondtext = start.render("인수인계 받기",True,(255,255,255))

    print("dddd")
    
    

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                return()
        screen.blit(bgg,(0,0))
        screen.blit(Text,(400,200))
        screen.blit(startfont,(900,600))
        screen.blit(secondtext,(900,800))

        pygame.display.update()
first()

def second():
    global mo1
    pygame.init()

    while True:
        a , b = pygame.mouse.get_pos()
        if 348 < a < 866 and 313 < b < 665:
            mo1 = pygame.transform.scale(mo1, (200,200))
        else: 
            mo1 = pygame.transform.scale(mo1, (100,100))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 348 < a < 866 and 313 < b < 665:
                    purchase()
                else:
                    ending()
        
        screen.blit(bg,(0,0))
        screen.blit(mo1,(0,0))
        screen.blit(mo2,(0,0))
        screen.blit(sin,(0,0))
        pygame.display.update()
second()

