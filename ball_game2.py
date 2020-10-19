import pygame
import numpy as np
import random
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1000, 600))
table = pygame.display.set_mode((1000, 600))
point = 0
#цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (40, 0, 0))
screen.blit(textsurface,(0, 0))
#массивы
#шарики
A=[]
X1=[]
Y1=[]
R1=[]
Color1=[]
V1=[]
U1=[]
#квадраты
L2=[]
R2=[]
X2=[]
Y2=[]
XC2=[]
YC2=[]
Color2=[]
#количество шариков и квадратов на экране
num = 3

def new_ball():
    #функция по созданию нового шарика
    x = randint(100, 900)
    y = randint(100, 500)
    r = randint(30, 80)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    v = random.randint(-5, 5)
    u = random.randint(-5, 5)

    return x, y, r, color, v, u

def new_square():
    #функция по созданию нового квадрата
    x = randint(100, 900)
    y = randint(100, 500)
    l = randint(30, 50)
    color2 = COLORS[randint(0, 5)]
    rect(screen, color2, (x, y, l, l))
    xc = int(x + l/2)
    yc = int(y - l/2)
    r = l / (2)**0.5
    return x, y, xc, yc, r, color2, l

def draw_ball(x, y, r, color):
    #функция рисует шарик
    circle(screen, color, (x, y), r)

def draw_square(x, y, l, color):
    #функция рисует квадрат
    rect(screen, color, (x, y, l, l))
    


def balls_in_one_place(num):
    #проверка находяться ли шарики друг в друге
    for i in range(num):
        for j in range(i + 1, num):
            if (X1[i] - X1[j])**2 + (Y1[i] - Y1[j])**2 <= (R1[i] + R1[j] + 5)**2:
                while (X1[i] - X1[j])**2 + (Y1[i] - Y1[j])**2 <= (R1[i] + R1[j] + 5)**2:
                    X1[j], Y1[j], R1[j], Color1[j], V1[j], U1[j] = new_ball()
                    X1[i], Y1[i], R1[i], Color1[i], V1[i], U1[i] = new_ball()
                balls_in_one_place(num)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
#время жизни шариков, квадратов и их перерисовка
pygame.time.set_timer(pygame.USEREVENT + 1, 10)
pygame.time.set_timer(pygame.USEREVENT + 2, 5000)
pygame.time.set_timer(pygame.USEREVENT + 3, 1)
pygame.time.set_timer(pygame.USEREVENT + 4, 10)

#создаем первые шарики и квадраты
for i in range(num):
    x1, y1, r1, color1, v1, u1 = new_ball()
    X1.append(x1)
    Y1.append(y1)
    R1.append(r1)
    Color1.append(color1)
    V1.append(v1)
    U1.append(u1)
    
    x2, y2, xc2, yc2, r2, color2, l2 = new_square()
    X2.append(x2)
    Y2.append(y2)
    XC2.append(xc2)
    YC2.append(yc2)
    L2.append(l2)
    Color2.append(color2)
    R2.append(r2)
#проверям координаты шариков
balls_in_one_place(num)

while not finished:
    clock.tick(FPS)
    #текст с количеством очков
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score: ' + str(point), False, (255, 255, 255))
    screen.blit(textsurface,(0, 0))
    #рисуем шарики
    for i in range(num):
        draw_ball(X1[i], Y1[i], R1[i], Color1[i])
    #рисуем квадраты
    for i in range(num):
        draw_square(X2[i], Y2[i], L2[i], Color2[i])
        
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 2:
            #время жизни шариков истекло, создаем новые шарики и проверяем их координаты
            for i in range(num):
                X1[i], Y1[i], R1[i], Color1[i], V1[i], U1[i] = new_ball()
            balls_in_one_place(num)
        elif event.type == pygame.USEREVENT + 1:
            #проверка на столкновение шариков со стенкой
            for i in range(num):
                if X1[i] + R1[i]>1000 or X1[i] - R1[i]<0:
                    V1[i]=-V1[i]
                if Y1[i] + R1[i]>600 or Y1[i] - R1[i]<0:
                    U1[i]=-U1[i]
                X1[i], Y1[i] = X1[i] + V1[i], Y1[i] + U1[i]
        elif event.type == pygame.USEREVENT + 3:
            #проверка на столкновение шариков между собой
            for j in range(num):
                for k in range(j, num):
                    if np.sqrt((X1[k] - X1[j])**2 + (Y1[k] - Y1[j])**2) <= R1[k] + R1[j] and k!=j:
                        if V1[k]*V1[j]>0:
                            if abs(V1[k])>abs(V1[j]):
                                V1[k]=-V1[k]
                            else:
                                V1[j]=-V1[j]
                        else:
                            V1[k]=-V1[k]
                            V1[j]=-V1[j]
                        if U1[k]*U1[j]>0:
                            if abs(U1[k])>abs(U1[j]):
                                U1[k]=-U1[k]
                            else:
                                U1[j]=-U1[j]
                        else:
                            U1[k]=-U1[k]
                            U1[j]=-U1[j]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = event.pos
            for i in range(num):
                #добавление очков при попадании на шарик
                if abs(A[0] - X1[0+i])<R1[0+i] and abs(A[1] - Y1[0+i])<R1[0+i]:
                    point += int(200/R1[0+i])
                    R1[0+i]=0
                    V1[0+i]=0
                    U1[0+i]=0
                    X1[0+i]=0
                    Y1[0+i]=0
                #добавление очков при попадании или квадрат
                if abs(A[0] - XC2[0+i])<R2[0+i] and abs(A[1] - YC2[0+i])<R2[0+i]:
                    point += 200
                    L2[0+i]=0
                    XC2[0+i]=0
                    YC2[0+i]=0
                    R2[0+i]=0
        elif event.type == pygame.USEREVENT + 4:
            #время жизни квадратов истекло, создаем новые квадраты
            for i in range(num):
                X2[i], Y2[i], XC2[i], YC2[i], R2[i], Color2[i], L2[i] = new_square()
        elif event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
