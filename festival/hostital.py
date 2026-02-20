import pygame
import random
import sys
import time

pygame.init()
pygame.display.set_caption('fdzz')
bgfont = pygame.font.Font('JalnanGothicTTF.ttf',70)
start1 = pygame.font.Font('JalnanGothicTTF.ttf',50)
size = screen_width, screen_height = 1600, 900
tt = 0
screen = pygame.display.set_mode(size)
bg = pygame.image.load("폐 처리.png")
co1 = [pygame.image.load("코로나1.png"),pygame.image.load("코로나2.png")] # 120 120
co2 = [pygame.image.load("코로나1.png"),pygame.image.load("코로나2.png")]
co3 = [pygame.image.load("코로나1.png"),pygame.image.load("코로나2.png")]

me1 = pygame.image.load("메르스.png") # 200 150
me2 = pygame.image.load("메르스.png")
me3 = pygame.image.load("메르스.png")

gam1 = [pygame.image.load("감기1.png"),pygame.image.load("감기2.png")] # 70 70
gam2 = [pygame.image.load("감기1.png"),pygame.image.load("감기2.png")]
gam3 = [pygame.image.load("감기1.png"),pygame.image.load("감기2.png")]
gam4 = [pygame.image.load("감기1.png"),pygame.image.load("감기2.png")]

bin1 = pygame.image.load("빈대.png")
bin2 = pygame.image.load("빈대.png")
bin3 = pygame.image.load("빈대.png")
bin4 = pygame.image.load("빈대.png")

smallFont = pygame.font.Font('JalnanGothicTTF.ttf',60)
smallFont1 = pygame.font.Font('JalnanGothicTTF.ttf',30)

vP1 = pygame.image.load("폐1.png")
vP2 = pygame.image.load("폐2.png")
vP3 = pygame.image.load("폐3.png")
vP4 = pygame.image.load("폐4.png")
a1 = -100
b1 = -100
a2 = -100
b2 = -100
a3 = -100
b3 = -100
a4 = -100
b4 = -100
a5 = -100
b5 = -100
a6 = -100
b6 = -100
a7 = -100
b7 = -100
a8 = -100
b8 = -100
a9 = -100
b9 = -100
a10 = -100
b10 = -100
a11 = -100
b11 = -100
a12 = -100
b12 = -100
a13 = -100
b13 = -100
a14 = -100
b14 = -100

tty = pygame.image.load("감메코빈 게임 방법001.png")
tty = pygame.transform.scale(tty,(1600,900))
#15811감기 2612 메르스 41013 코로나 37914 빈대
def corona1():
    global a1, b1, tt
    a1 = random.randrange(0,1530)
    b1 = random.randrange(0,830)
def corona2():
    global a2, b2
    a2 = random.randrange(0,1400)
    b2 = random.randrange(0,750)
def corona3():
    global a3, b3
    a3 = random.randrange(0,1500)
    b3 = random.randrange(0,800)
def corona4():
    global a4, b4
    a4 = random.randrange(0,1480)
    b4 = random.randrange(0,780)
def corona5():
    global a5, b5
    a5 = random.randrange(0,1530)
    b5 = random.randrange(0,830)
#15811감기 2612 메르스 41013 코로나 37914 빈대
def corona6():
    global a6, b6
    a6 = random.randrange(0,1400)
    b6 = random.randrange(0,750)
def corona7():
    global a7, b7
    a7 = random.randrange(0,1500)
    b7 = random.randrange(0,800)
def corona8():
    global a8, b8
    a8 = random.randrange(0,1530)
    b8 = random.randrange(0,830)
def corona9():
    global a9, b9
    a9 = random.randrange(0,1500)
    b9 = random.randrange(0,800)
def corona10():
    global a10, b10
    a10 = random.randrange(0,1480)
    b10 = random.randrange(0,780)
def corona11():
    global a11, b11
    a11 = random.randrange(0,1530)
    b11 = random.randrange(0,830)
#15811감기 2612 메르스 41013 코로나 37914 빈대
def corona12():
    global a12, b12
    a12 = random.randrange(0,1400)
    b12 = random.randrange(0,750)
def corona13():
    global a13, b13
    a13 = random.randrange(0,1480)
    b13 = random.randrange(0,780)
def corona14():
    global a14, b14
    a14 = random.randrange(0,1500)
    b14 = random.randrange(0,800)

bbg = pygame.image.load("다운로드.png")
bbg2 = pygame.image.load("사망.png")
def ending():
    global cc1, cc2, cc3, tlqkf,a1, b1, a2, a3, a4, a5, a6, a7, b2, b3, b4, b5, b6, b7, k1, k2, k3, k4, k5, k6, k7, a8, a9, a10, b8, b9, b10, k8, k9, k10
    global g2, g4, g6, kk, hh, tt, ap, wjatn, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, k11, k12, k13, k14, a11, b11, a12, b12, a13, b13, a14, b14
    pygame.init()
    
    tlqkf = 0
    a1 = -100
    b1 = -100
    a2 = -100
    b2 = -100
    a3 = -100
    b3 = -100
    a4 = -100
    b4 = -100
    a5 = -100
    b5 = -100
    a6 = -100
    b6 = -100
    a7 = -100
    b7 = -100
    a8 = -100
    b8 = -100
    a9 = -100
    b9 = -100
    a10 = -100
    b10 = -100
    a11 = -100
    b11 = -100
    a12 = -100
    b12 = -100
    a13 = -100
    b13 = -100
    a14 = -100
    b14 = -100
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    k7 = 0
    k8 = 0
    k9 = 0
    k10 = 0
    k11 = 0
    k12 = 0
    k13 = 0
    k14 = 0
    
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    v7 = 0
    v8 = 0
    v9 = 0
    v10 = 0

    hg2 = 2
    g4 = 2
    g6 = 2

    kk = 0
    hh = 0
    ap = 1
    tlqkf = 0
    tt = 0
    ii = smallFont.render("점수: {}".format(wjatn),True,(0,0,0))
    wjatn = 0
    
    ff1 = smallFont1.render("코로나 바이러스에 감염되어 죽었습니다!",True,(0,0,0))
    ff2 = smallFont1.render("코로나 바이러스는 감염 속도가 빨라 빠르게 처리해야하니 유의하세요!", True,(0,0,0))
    ff1_size = ff1.get_rect().size
    ff1_width = ff1_size[0]
    ff1_height = ff1_size[1]
    ff2_size = ff2.get_rect().size
    ff2_width = ff2_size[0]
    ff2_height = ff2_size[1]
    ii_size = ii.get_rect().size
    ii_width = ii_size[0]
    
    ff3 = smallFont1.render("너무 많은 균에 감염되어 죽었습니다!",True,(0,0,0))
    ff3_size = ff3.get_rect().size
    ff3_width = ff3_size[0]
    ff3_height = ff3_size[1]
    while True:
        if cc1 >= 100 or cc2 >= 100 or cc3 >= 100:
            screen.blit(bbg,(0,0))
            screen.blit(ii,(800 - ii_width/2,300))
            screen.blit(ff1,(800 - ff1_width/2,580))
            screen.blit(ff2,(800 - ff2_width/2,680))
        else:
            screen.blit(bbg2,(0,0))
            screen.blit(ii,(800 - ii_width/2,300))
            screen.blit(ff3,(800 - ff3_width/2,450 - ff3_height/2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                cc1 = 0
                cc2 = 0
                cc3 = 0
                first()
                
        pygame.display.update()


k1 = 0
k2 = 0
k3 = 0
k4 = 0
k5 = 0
k6 = 0
k7 = 0
k8 = 0
k9 = 0
k10 = 0
k11 = 0
k12 = 0
k13 = 0
k14 = 0

g2 = 2
g4 = 2
g6 = 2

kk = 0
hh = 0
ap = 1
tlqkf = 0

wjatn = 0
cc1 = 0
cc2 = 0
cc3 = 0
vv1 = [20, 710, 1400, 1950, 2330, 2630, 2890]
vv2 = [90, 780, 1460, 1990, 2360, 2660, 2910]
vv3 = [160, 850, 1520, 2030, 2390, 2690, 2930]
vv4 = [230, 920, 1580, 2070, 2420, 2720, 2950]
vv5 = [300, 990, 1640, 2110, 2450, 2750, 2970]
vv6 = [370, 1060, 1700, 2150, 2480, 2780, 2990]
vv7 = [430, 1130, 1750, 2190, 2510, 2810, 3010]
vv8 = [500, 1200, 1800, 2230, 2540, 2830, 3030]
vv9 = [570, 1270, 1850, 2270, 2570, 2850, 3050]
vv10 = [640, 1340, 1900, 2300, 2600, 2870, 3070]
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0
v10 = 0
#15811감기 2612 메르스 41013 코로나 37914 빈대
start = pygame.time.get_ticks()
clock = pygame.time.Clock()
moving = 0

kk1 = 0
kk2 = 0
kk3 = 0
kk4 = 0
kk5 = 0
kk6 = 0
kk7 = 0
kk8 = 0
kk9 = 0 
kk10 = 0
kk11 = 0
kk12 = 0
kk13 = 0
kk14 = 0
def second():
    global a1, b1, a2, a3, a4, a5, a6, a7, b2, b3, b4, b5, b6, b7, k1, k2, k3, k4, k5, k6, k7, a8, a9, a10, b8, b9, b10, k8, k9, k10
    global g2, g4,g6, kk, hh, ap, tlqkf, tt, wjatn, cc1, cc2, cc3, v1, v2, v3, v4, v5, v6, v7, v8, vv1, vv2, vv3, vv4, vv5, vv6, vv7, vv8
    global moving, a11, b11, a12, b12, a13, b13, a14, b14, v9, v10, vv9, vv10, k11,k12,k13,k14,kk1,kk2,kk3,kk4,kk5,kk6,kk7,kk8,kk9,kk10,kk11,kk12,kk13,kk14
    pygame.init()
    yu = kk1+kk2+kk3+kk4+kk5+kk6+kk7+kk8+kk9+kk10+kk11+kk12+kk13+kk14
    if -50 <= yu < 3:
        screen.blit(vP1,(0,0))
    elif 3 <= yu < 6:
        screen.blit(vP2,(0,0))
    elif 6<= yu < 9:
        screen.blit(vP3,(0,0))
    else:
        screen.blit(vP4,(0,0))
    danger = smallFont.render("병균이 너무 많습니다! 빨리 처리하세요!",True,(255,255,255))
    gg = smallFont.render("점수: {}".format(wjatn),True,(255,255,255))
    
    danger_size = danger.get_rect().size
    danger_width = danger_size[0]
    danger_height = danger_size[1]
    
    if yu >= 6:
        screen.blit(danger,(800 - danger_width/2,450 - danger_height/2))
    if moving == 0:
        moving += 1
        print ("tt")
    else:
        moving = 0
        print ("gg")
    #15811감기 2612 메르스 41013 코로나 37914 빈대
    if k1 >= 1:
        screen.blit(gam1[moving],(a1,b1))
        kk1 = 1
    else:
        kk1 = 0
    if k2 >= 1:
        screen.blit(me1,(a2,b2))
        kk2 = 1
    else:
        kk2 = 0
    if k3 >= 1:
        screen.blit(bin1,(a3,b3))
        kk3 = 1
    else:
        kk3 = 0
    if k4 >= 1:
        screen.blit(co1[moving],(a4,b4))
        kk4 = 1
    else:
        kk4 = 0
    if k5 >= 1:
        screen.blit(gam2[moving],(a5,b5))
        kk5 = 1
    else:
        kk5 = 0
    if k6 >= 1:
        screen.blit(me2,(a6,b6))
        kk6 = 1
    else:
        kk6 = 0
    if k7 >= 1:
        screen.blit(bin2,(a7,b7))
        kk7 = 1
    else:
        kk7 = 0
    if k8 >= 1:
        screen.blit(gam3[moving],(a8,b8))
        kk8 = 1
    else:
        kk8 = 0
    if k9 >= 1:
        screen.blit(bin3,(a9,b9))
        kk9 = 1
    else:
        kk9 = 0
    if k10 >= 1:
        screen.blit(co2[moving],(a10,b10))
        kk10 = 1
    else:
        kk10 = 0
    if k11 >= 1:
        screen.blit(gam4[moving],(a11,b11))
        kk11 = 1
    else:
        kk11 = 0
    if k12 >= 1:
        screen.blit(me3,(a12,b12))
        kk12 = 1
    else:
        kk12 = 0
    if k13 >= 1:
        screen.blit(co3[moving],(a13,b13))
        kk13 = 1
    else:
        kk13 = 0
    if k14 >= 1:
        screen.blit(bin4,(a14,b14))
        kk14 = 1
    else:
        kk14 = 0
    screen.blit(gg,(50,50))
    while True:
        tlqkf += 1
        clock.tick(48)
        if k4 >= 1:
            cc1 += 1
        if k10 >= 1:
            cc2 += 1
        if k13 >= 1:
            cc3 += 1
        if cc1 == 100 or cc2 == 100 or cc3 == 100:
            ending()
            
        if yu >= 10:
            ending()
        #15811감기 2612 메르스 41013 코로나 37914 빈대
        if tlqkf == vv1[v1]:
           v1 += 1
           if a1 == -70 and b1 == -70:
                tt += 1
           k1 += 1
           corona1()
           second()
        
        if tlqkf == vv2[v2]:
            v2 += 1
            if a2 == -200 and b2 == -150:
                tt += 1
            if a3 == -100 and b3 == -100:
                tt += 1
            g2 = 2
            k2 += 1
            k3 += 1
            corona3()
            corona2()
            second()
        #15811감기 2612 메르스 41013 코로나 37914 빈대
        if tlqkf == vv3[v3]:
            
            v3 += 1
            if a4 == -120 and b4 == -120:
                tt += 1
            tt += 1
            k4 += 1
            corona4()
            second()

        if tlqkf == vv4[v4]:
            
            v4 += 1
            if a5 == -70 and b5 == -70:
                tt += 1
            k5 += 1
            corona5()
            second()
        if tlqkf == vv5[v5]:
            v5 += 1
            if a6 == -200 and b6 == -150:
                tt += 1
            g4 = 2
            k6 += 1
            corona6()
            second()
        if tlqkf == vv6[v6]:
            v6 += 1
            if a7 == -100 and b7 == -100:
                tt += 1
            k7 += 1
            corona7()
            second()
        if tlqkf == vv7[v7]:
            v7 += 1
            if a9 == -100 and b9 == -100:
                tt += 1
            if a8 == -70 and b8 == -70:
                tt += 1
            
            k8 += 1
            k9 += 1
            corona8()
            corona9()
            second()
        if tlqkf == vv8[v8]:
            v8 += 1
            if a10 == -120 and b10 == -120:
                tt += 1
            k10 += 1
            corona10()
            second()
        if tlqkf == vv9[v9]:
            v9 += 1
            g6 = 2
            if a12 == -200 and b12 == -150:
                tt += 1
            if a11 == -70 and b11 == -70:
                tt += 1
            k11 += 1
            k12 += 1
            corona11()
            corona12()
            second()
        if tlqkf == vv10[v10]:
            v10 += 1
            if a14 == -100 and b14 == -100:
                tt += 1
            if a13 == -120 and b13 == -120:
                tt += 1
            k13 += 1
            k14 += 1
            corona13()
            corona14()
            second()
        
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_f]:
            kk += 1
        if keys[pygame.K_d]:
            hh += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    kk = 0
                if event.key == pygame.K_d:
                    hh = 0
            #15811감기 2612 메르스 41013 코로나 37914 빈대
            if event.type == pygame.MOUSEBUTTONDOWN:
                a , b = pygame.mouse.get_pos()
                if a1 < a < a1 + 70 and b1 < b < b1 + 70:
                    if kk == 0 and hh == 0:    
                        wjatn += 100
                        tt -= 1
                        k1 = 0
                        a1 = -70
                        b1 = -70
                        second()
                if a2 < a < a2 + 200 and b2 < b < b2 + 150:
                    if hh == 0:
                        if kk > 0:
                            g2 -= 1
                            if g2 <= 0:
                                wjatn += 200
                                tt -= 1
                                k2 = 0
                                a2 = -200
                                b2 = -150
                                print("2")
                                second()
                if a3 < a < a3 + 100 and b3 < b < b3 + 100:
                    if kk > 0 and hh > 0:
                        wjatn += 200
                        tt -= 1
                        k3 = 0
                        a3 = -100
                        b3 = -100
                        second()
                #15811감기 2612 메르스 41013 코로나 37914 빈대
                if a4 < a < a4 + 120 and b4 < b < b4 + 120:
                    if kk == 0:    
                        if hh > 0:
                            tt -= 1
                            cc1 = 0
                            wjatn += 200
                            k4 = 0
                            a4 = -120
                            b4 = -120
                            second()
                if a5 < a < a5 + 70 and b5 < b < b5 + 70:
                    if kk == 0 and hh == 0:
                        wjatn += 100
                        tt -= 1
                        k5 = 0
                        a5 = -100
                        b5 = -100
                        second()
                #15811감기 2612 메르스 41013 코로나 37914 빈대
                if a6 < a < a6 + 200 and b6 < b < b6 + 150:
                    if hh == 0:    
                        if kk > 0:
                            g4 -= 1
                            if g4 <= 0: 
                                tt -= 1
                                wjatn += 200   
                                k6 = 0
                                a6 = -200
                                b6 = -150
                                print("6")
                                second()
                if a7 < a < a7 + 100 and b7 < b < b7 + 100:
                    if hh > 0 and kk > 0:
                        tt -= 1
                        wjatn += 200
                        k7 = 0
                        a7 = -100
                        b7 = -100
                        second()
                if a8 < a < a8 + 70 and b8 < b < b8 + 70:
                    if kk == 0 and hh == 0:
                        wjatn += 100
                        k8 = 0
                        a8 = -70
                        b8 = -70
                        second()
                #15811감기 2612 메르스 41013 코로나 37914 빈대
                if a9 < a < a9 + 100 and b9 < b < b9 + 100:
                       
                    if kk > 0 and hh > 0:
                        
                        wjatn += 200  
                        tt -= 1
                        
                        k9 = 0
                        a9 = -100
                        b9 = -100
                        second()
                if a10 < a < a10 + 120 and b10 < b < b10 + 120:
                    if kk == 0:    
                        if hh > 0:
                            tt -= 1
                            cc2 = 0
                            wjatn += 200
                            k10 = 0
                            a10 = -120
                            b10 = -120
                            second()
                if a11 < a < a11 + 70 and b11 < b < b11 + 70:
                    if kk == 0 and hh == 0:
                        wjatn += 100
                        tt -= 1
                        k11 = 0
                        a11 = -70
                        b11 = -70
                        second()
                if a12 < a < a12 + 200 and b12 < b < b12 + 150:
                    if hh == 0:    
                        if kk > 0:
                            g6 -= 1
                            if g6 <= 0: 
                                tt -= 1
                                wjatn += 200   
                                k12 = 0
                                print("12")
                                a12 = -200
                                b12 = -150
                                
                                second()
                if a13 < a < a13 + 120 and b13 < b < b13 + 120:
                    if kk == 0:    
                        if hh > 0:
                            tt -= 1
                            cc3 = 0
                            wjatn += 200
                            k13 = 0
                            a13 = -120
                            b13 = -120
                            second()
                if a14 < a < a14 + 100 and b14 < b < b14 + 100:
                       
                    if kk > 0 and hh > 0:
                        
                        wjatn += 200  
                        tt -= 1
                        
                        k14 = 0
                        a14 = -100
                        b14 = -100
                        second()
        pygame.display.update()
ttt = 0


def first():
    global ttt
    pygame.init()
    screen.blit(bg,(0,0))
    Text = bgfont.render("감메코빈 멸살하기", True,(255,255,255))
    
    startfont = start1.render("멸살하기",True,(255,255,255))
    secondtext = start1.render("설명 보기",True,(255,255,255))
    s_size = startfont.get_rect().size
    t_size = secondtext.get_rect().size
    s_width = s_size[0]
    t_width = t_size[0]
    
    screen.blit(Text,(100,400))
    screen.blit(startfont,(1100,500))
    screen.blit(secondtext,(1100,600))

    if ttt >= 1:
        
        screen.blit(tty,(0,0))
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                a , b = pygame.mouse.get_pos()
                if 1100 < a < 1100 + s_width and 500 < b < 550:
                    if ttt == 0:
                        print("Ggf")
                        second()
                    else:
                        ttt = 0
                        first()
                elif 1100 < a < 1100 + t_width and 600 < b < 650:
                    if ttt == 0:
                        ttt += 1
                        first()
                    else:
                        ttt = 0
                        first()
                else:
                    ttt = 0
                    first()
        pygame.display.update()
first()
