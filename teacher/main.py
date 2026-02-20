#물건 날아옴

import pygame
import random
import time

size = width, height = 1400,800
win = pygame.display.set_mode(size)
bg = pygame.image.load("도트 배경 팅경.png")
bg2 = pygame.image.load("바닥.png")
char1 = pygame.image.load('과학.png')
char2 = pygame.image.load('과학왼.png')
ob = pygame.image.load('담배.png')
ob2 = pygame.image.load("휴지.png")
firstbg = pygame.image.load("시작배경.png")
firstbutton = pygame.image.load("버튼.png")
againbutton = pygame.image.load("다시하기.png")
lastbg = pygame.image.load("끝.png")
choice_sc = pygame.image.load("캐릭터 선택 과학.png")
choice_mu = pygame.image.load("캐릭터 선택 쌤.png")
choice = pygame.image.load("준비.png")
vitual1 = pygame.image.load("가상현실1.png")
vitual2 = pygame.image.load("가상현실2.png")
uchar1 = pygame.image.load("평범.png")
uchar2 = pygame.image.load("음악왼.png")
p=0
o=0
i=0
l=0
stage_count = 0
obsp = -1
ctime = 0
kbutton = 0
#win.fill((255,255,255))

win.blit(firstbg,(0,0))
pygame.display.update()

pygame.init()
clock = pygame.time.Clock()
start = pygame.time.get_ticks()

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (글씨체, 크기)
font = pygame.font.Font(None, 100)
# 시작 시간
start = pygame.time.get_ticks()

# Load an image
weapon = pygame.image.load("무기이이.png")
vweapon = pygame.image.load("건물오.png")
vlweapon = pygame.image.load("건물왼.png")
pp = pygame.image.load("하트0개빈.png")
walkRight =[pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷1.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷2.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷3.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png"),
            pygame.image.load("걷4.png")]
walkLeft = [pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷1.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷2.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷3.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png"),
            pygame.image.load("과학왼걷4.png")]
eneM = [pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),
        pygame.image.load("학생1.png"),

        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),
        pygame.image.load("학생2.png"),

        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png"),
        pygame.image.load("학생3.png")]

eneL = [pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        pygame.image.load("학생왼1.png"),
        
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),
        pygame.image.load("학생왼2.png"),

        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png"),
        pygame.image.load("학생왼3.png")]

sitR_ = pygame.image.load("과학앉.png")
sitL_ = pygame.image.load("과학앉왼.png")

# 유진쌤 모션

virtual = [pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),
           pygame.image.load("가상현실1.png"),

           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           pygame.image.load("가상현실2.png"),
           
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),
           pygame.image.load("가상현실3.png"),]

wing = [pygame.image.load("이동 옆1.png"),
        pygame.image.load("이동 옆1.png"),
        pygame.image.load("이동 옆1.png"),
        pygame.image.load("이동 옆1.png"),
        pygame.image.load("이동 옆1.png"),

        pygame.image.load("이동 옆2.png"), 
        pygame.image.load("이동 옆2.png"),
        pygame.image.load("이동 옆2.png"),
        pygame.image.load("이동 옆2.png"),
        pygame.image.load("이동 옆2.png"),
        
        pygame.image.load("이동 옆3.png"),
        pygame.image.load("이동 옆3.png"),
        pygame.image.load("이동 옆3.png"),
        pygame.image.load("이동 옆3.png"),
        pygame.image.load("이동 옆3.png")]

wingL = [pygame.image.load("이동 옆왼1.png"),
        pygame.image.load("이동 옆왼1.png"),
        pygame.image.load("이동 옆왼1.png"),
        pygame.image.load("이동 옆왼1.png"),
        pygame.image.load("이동 옆왼1.png"),

        pygame.image.load("이동 옆왼2.png"), 
        pygame.image.load("이동 옆왼2.png"),
        pygame.image.load("이동 옆왼2.png"),
        pygame.image.load("이동 옆왼2.png"),
        pygame.image.load("이동 옆왼2.png"),
        
        pygame.image.load("이동 옆왼3.png"),
        pygame.image.load("이동 옆왼3.png"),
        pygame.image.load("이동 옆왼3.png"),
        pygame.image.load("이동 옆왼3.png"),
        pygame.image.load("이동 옆왼3.png")]

throw = [pygame.image.load("과학던1.png"),
         pygame.image.load("과학던1.png"),
         pygame.image.load("과학던1.png"),
         pygame.image.load("과학던1.png"),
         pygame.image.load("과학던1.png"),

         pygame.image.load("과학던2.png"),
         pygame.image.load("과학던2.png"),
         pygame.image.load("과학던2.png"),
         pygame.image.load("과학던2.png"),
         pygame.image.load("과학던2.png"),
         
         pygame.image.load("과학던3.png"),
         pygame.image.load("과학던3.png"),
         pygame.image.load("과학던3.png"),
         pygame.image.load("과학던3.png"),
         pygame.image.load("과학던3.png")]

throwl = [pygame.image.load("과학왼던1.png"),
         pygame.image.load("과학왼던1.png"),
         pygame.image.load("과학왼던1.png"),
         pygame.image.load("과학왼던1.png"),
         pygame.image.load("과학왼던1.png"),

         pygame.image.load("과학왼던2.png"),
         pygame.image.load("과학왼던2.png"),
         pygame.image.load("과학왼던2.png"),
         pygame.image.load("과학왼던2.png"),
         pygame.image.load("과학왼던2.png"),
         
         pygame.image.load("과학왼던3.png"),
         pygame.image.load("과학왼던3.png"),
         pygame.image.load("과학왼던3.png"),
         pygame.image.load("과학왼던3.png"),
         pygame.image.load("과학왼던3.png")]

vsit_image = [pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),

         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         pygame.image.load("평범.png"),
         
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),
         pygame.image.load("올리기 3.png"),

         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         pygame.image.load("올리기 2.png"),
         
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png"),
         pygame.image.load("올리기 1.png")]


vsit_number = 0

# 무기 여러발 가능
weapons = []
wea_speed = 60

vweapons = []
vwea_speed = 30

vlweapons = []

#적 스피드
ene_speed = 3
obs = 0

# 팔 올리는 거 모션
throw_number = 0

vel = 10 # 329
x = 800
y = 399
left = False
right = False
walkcount = 0
walkCe = 0
stopd = True
stopL = False
sitR = False
sitL = False
eneW = False
ctimedef = False
ctimek = False
throww = False
throwwl = False

ene = pygame.image.load("적.png")
ene_X_pos = 1600 # 화면 중간에 위치
eneL_X = -70
obx= 1600
ene_Y_pos = 600 # 화면 맨 아래 위치
limitedtime = 0

stage0_r=[1500, 1900, 2000, 1600, 1900, 2100, 1740]
stage0_l= [-100, -1700, -1000, -1000, -100, -300, -3000]
speed = [5 , 7, 10]
speedob = [15 , 20, 30]
thr=[1800, 3000, 1600, 1900, 1500, 1700, 3000]

bombmove = 0
gg = pygame.image.load("하트1개빈.png")
def redrawG():
    global walkcount, ctimedef, ctime, kbutton, ctimek, throw_number, throww, stopd, stopL, throwwl, vel
    win.blit(bg, (0, 0))
    win.blit(bg2,(0, 700))
    #win.fill((255, 255, 255))

    if walkcount >= 32:
        walkcount = 0

    #
    

    # walk right
    if right:
        win.blit(walkRight[walkcount],(x,y))
        walkcount += 1
        vel= 10
    
    elif throww:
        win.blit(throw[throw_number],(x,y))
        throw_number += 1
        vel = 0
        if throw_number >= 15:
           throw_number = 0
           throww = False
           stopd = True

    elif throwwl:
        win.blit(throwl[throw_number],(x,y))
        throw_number += 1
        vel = 0
        stopd = False
        if throw_number >= 15:
           throw_number = 0
           throwwl = False
           stopL = True

    #walk left
    elif left:
        win.blit(walkLeft[walkcount],(x,y))
        walkcount += 1
        vel = 10
    
    elif sitR:
        win.blit(sitR_, (x, y + 121))

    elif sitL:
        win.blit(sitL_, (x, y + 121))

    elif stopd :
        win.blit(char1, (x, y))
        vel = 10

    elif stopL:
        win.blit(char2, (x,y))
        vel =10

    if ctimedef:
       ctime += 1
       if ctime >= 20:
           print("j 쿨타임 끝!")
           ctime = 0
           ctimedef = False

    if ctimek:
        kbutton +=1
        if kbutton >=200:
            print("k 쿨타임 끝!")
            kbutton = 0
            ctimek = False

vright = False
vleft = False
vsit = False
vsit2 = False
vup = False
vup_number = 0
limited = False
down = False
vctime = False
kvbutton = 0
move_number = 0
def 가상현실():
    global walkcount, ctimedef,move_number,wing, ctime, vctime, vright, left, kvbutton, ctimek, vsit, vsit_image, vsit_number,down, vsit2, vitual1, vup,uchar1, stopd, vup_number, vel
    win.blit(bg, (0, 0))
    win.blit(bg2,(0, 700))
    #win.fill((255, 255, 255))

    if walkcount >= 32:
        walkcount = 0
    
    if move_number >= 15:
        move_number = 0
    
    # walk right
    if vright:
        win.blit(wing[move_number],(x,y - 70))
        move_number += 1

    #walk left
    elif left:
        win.blit(wingL[move_number],(x,y - 70))
        move_number += 1
        
    
    elif stopd :
        win.blit(virtual[walkcount],(x,y - 70))
        walkcount += 1

    elif down:
        vel = 0
        vsit_number += 1
        win.blit(vsit_image[vsit_number],(x , y-70))
        stopd = False
        if vsit_number >= 55:
            vsit_number = 0
            down = False
            stopd = True    



    if ctimedef:
       ctime += 1
       if ctime >= 20:
           ctime = 0
           print ("j 쿨타임 끝!")
           ctimedef = False

    if vctime:
        kvbutton +=1
        if kvbutton >=150:
            kvbutton = 0
            print ("space 쿨타임 끝!")
            vctime = False
    
    

urun = False
run = False
first = True
second = False
third = False
while first:
    win.blit(firstbg,(0,0))
    win.blit(firstbutton,(950,530))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            first = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            a , b = pygame.mouse.get_pos()
            if 800 < a < 1095 and 550 < b < 727:
                first = False
                second = True

while second:
    win.blit(choice,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            second = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            a , b = pygame.mouse.get_pos()
            if 417 < a < 731 and 234 < b < 654:
                second = False
                run = True
            elif 704 < a < 973 and 219 < b < 747:
                urun = True
                second = False

tlqkf = 500


def shotr(z):
    d = stage0_r [z]
    
    return d

def shootl(x):
    g = stage0_l [x]

    return g

def speedf(u):
    e = speed [u]

    return e

def obspeed(t):
    r = speedob [t]

    return r

def tqobx(i):
    t = thr [i]

    return t

while run:
    clock.tick(48)
    walkCe +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if right:
                right = False
                stopd = True
            elif left:
                left = False
                stopd = False
                stopL = True
                right = False
            if sitR:
                sitR = False
                stopd = True
            if sitL:
                sitL = False
                stopd = False
                stopL = True
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if stopd == True:
                    if ctimedef == False:
                       weaX = x + 211
                       weaY = 500
                       weapons.append([weaX, weaY])
                       ctimedef = True
                       throww = True
                       throwwl = False
                       stopd = False
                       

                elif right == True:
                     if ctimedef == False:
                       weaX = x + 211
                       weaY = 500
                       weapons.append([weaX, weaY])
                       ctimedef = True
                       throww = True
                       throwwl = False
                       right = False
                
                elif stopL == True:
                    if ctimedef == False:
                       weaX = x - 80
                       weaY = 500
                       weapons.append([weaX, weaY])
                       ctimedef = True
                       throwwl = True
                       throww = False
                       stopL = False

                elif left == True:
                    if ctimedef == False:
                       weaX = x - 80
                       weaY = 500
                       weapons.append([weaX, weaY])
                       ctimedef = True
                       throwwl = True
                       throww = False
                       left = False
            if event.key == pygame.K_k:
                if ctimek == False:
                    p+=1
                    o+=1
                    if p == 7:
                       p=0
                    if o == 7:
                       o=0
                    ene_X_pos = shootl(p)
                    eneL_X = shotr(o)
                    ctimek = True
                
                
                
               
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if keys[pygame.K_d]:
            vel = 0
            sitL =False
            right = False
            left = False
            sitR = True

        if keys[pygame.K_a]:
            right = False
            left = False
            vel=0
            sitR = False
            sitL = True
        
        if stopd:
            stopd = False
            stopL = False
            sitL = False
            sitR = True
        if stopL:
            stopL = False
            sitR = False
            sitL = True
            sitR = False

    elif keys[pygame.K_d]:
        if throww == False and throwwl == False:
            if x > width - 100:
                x = width - 100
            if throww == False:
                right = True
                x += vel
            left = False
            sitR = False
            sitL = False
    elif keys[pygame.K_a]:
        if throwwl == False and throww == False:
            right = False
            stopd = False
            if x < 30:
                x = 30
            if throwwl == False:
                left = True
                x -= vel
            right = False
            stopL = True
        

    #충돌처
    
    ene_X_pos -= ene_speed
    eneL_X += ene_speed
    obx -= obs
    
    if ene_X_pos < 0:
        ene_X_pos = random.randint(1200, 3000)
    if eneL_X > 1200:
        eneL_X = random.randint(-1570, -70)
    if obx < 0:
        obx = random.randint(1200, 2000)
    walkCe +=1
    if walkCe >= 30:
        walkCe = 0
    
    redrawG()
    

    weapons = [ [w[0], w[1] - wea_speed] for w in weapons]
    # 천장에 닿은 무기 없애기
    
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    for weaX, weaY in weapons:
        win.blit(weapon, (weaX, weaY))
        
        if ene_X_pos < weaX < ene_X_pos + 70 or ene_X_pos < weaX + 30 < ene_X_pos + 70:
           p +=1
           if p == 7:
               p=0
               stage_count += 1
               ene_X_pos = shotr(p)
               if stage_count <= 5:
                   text = font.render("stage %d" %stage_count,True,(255,255,255))
                   win.blit(text,(500,250))
                   pygame.display.update()
                   time.sleep(3)
                   if stage_count >= 3: 
                       obsp += 1
                       obs = obspeed(obsp) 
               if l == 2:
                   l = 2
               else: 
                   l += 1
               ene_speed = speedf(l)
               
           else:
               ene_X_pos = shotr(p)
        elif eneL_X < weaX < eneL_X + 70 or eneL_X < weaX + 30 < eneL_X + 70:
           o +=1
           if o == 7:
               o=0
               eneL_X = shootl(o)
           else:
               eneL_X = shootl(o)
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    score = ((pygame.time.get_ticks() - start) / 1000)
    timer = game_font.render(str(int(score)), True, (255, 255, 255))
    win.blit(timer, (10,10))
    
    if ene_X_pos < x + 100:
        run = False
    if eneL_X + 70 > x + 30:
        run = False
    if x < obx < x+70:
        if sitL == False and sitR == False:
            run = False
    win.blit(eneM[walkCe], (ene_X_pos, 399))
    win.blit(eneL[walkCe], (eneL_X, 399))
    if stage_count % 2 == 1:
        win.blit(ob, (obx, 400))
    elif stage_count % 2 == 0:
        win.blit(ob2, (obx, 400))
    
    win.blit(bg2,(0,700))
    win.blit(gg,(0,0))
    pygame.display.update()



while urun:

    y = 400
    vel = 10
    clock.tick(48)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            urun = False

        if event.type == pygame.KEYUP:
            if vright == True:
                stopd = True
                vright = False
            
            if left == True:
                stopd = True
                left = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if ctimedef == False:
                    if stopd == True or vright == True:
                        ctimedef = True
                        weaX = x + 200
                        weaY = 700
                        vweapons.append([weaX, weaY])
                    elif left == True:
                        ctimedef = True
                        weaX = x - 100
                        weaY = 700
                        vlweapons.append([weaX, weaY])


            
               
                
             
                
                
               
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
       if vctime == False:
           vctime = True
           vright = False
           left = False
           down =True
           stopd = False

    elif keys[pygame.K_d]:
        if x > width - 100:
             x = width - 100
        if down == False:
            x += vel
            vright = True
            left = False
            stopd = False

        
        
    elif keys[pygame.K_a]:
        if x < 30:
            x = 30
        if down == False:
            x -= vel
            vright = False
            left = True
            stopd = False

    
    

        
            

    

    
    #충돌처
    
    ene_X_pos -= ene_speed
    eneL_X += ene_speed
    obx -= obs
    
    if ene_X_pos < 0:
        ene_X_pos = random.randint(1200, 3000)
    if eneL_X > 1200:
        eneL_X = random.randint(-1570, -70)
    if obx < 0:
        obx = random.randint(1200, 2000)
    walkCe += 1
    if walkCe >= 30:
        walkCe = 0
    
    가상현실()
    

    vweapons = [ [w[0], w[1] - 10] for w in vweapons]
    vlweapons =[ [w[0], w[1] - 10] for w in vlweapons]
    # 천장에 닿은 무기 없애기
    
    vweapons = [[w[0], w[1]] for w in vweapons if w[1] > 558]
    vlweapons = [[w[0], w[1]] for w in vlweapons if w[1] > 558]
    
    

    for weaX, weaY in vweapons or vlweapons:
        if stopd == True or walkRight == True:
            win.blit(vweapon, (weaX, weaY))
            
        else:
            win.blit(vlweapon, (weaX, weaY))
            

        if ene_X_pos < weaX < ene_X_pos + 123 or ene_X_pos < weaX + 98 < ene_X_pos + 123:
            p +=1
            if p == 7:
               p=0
               stage_count += 1
               ene_X_pos = shotr(p)
               if stage_count <= 5:
                   text = font.render("stage %d" %stage_count,True,(255,255,255))
                   win.blit(text,(500,250))
                   pygame.display.update()
                   time.sleep(3)
                   if stage_count >=3: 
                       obsp += 1
                       obs = obspeed(obsp) 
               if l == 2:
                   l = 2
               else: 
                   l += 1
               ene_speed = speedf(l)
               
            else:
               ene_X_pos = shotr(p)
        elif eneL_X < weaX < eneL_X + 123 or eneL_X < weaX + 98 < eneL_X + 123:
           o +=1
           if o == 7:
               o=0
               eneL_X = shootl(o)
           else:
               eneL_X = shootl(o)
    score = ((pygame.time.get_ticks() - start) / 1000)
    timer = game_font.render(str(int(score)), True, (255, 255, 255))
    win.blit(timer, (10,10))
    
    if ene_X_pos < x + 190:
        if down == False:
            urun = False
    if eneL_X + 70 > x + 30:
        if down == False:
            urun = False
    if x + 30 < obx < x + 190:
        if down == False:
            urun = False
    win.blit(eneM[walkCe], (ene_X_pos, 399))
    win.blit(eneL[walkCe], (eneL_X, 399))
    if walkcount % 2 == 1:
        win.blit(ob, (obx, 600))
    elif walkcount % 2 == 0:
        win.blit(ob2, (obx, 600))
    win.blit(bg2,(0,700))
    pygame.display.update() 
    

    
    

    

