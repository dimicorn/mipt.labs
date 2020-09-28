import pygame
from pygame.draw import *
import numpy as np
pygame.init()

screen = pygame.display.set_mode((600, 650))

#цвета
moongray = (240, 240, 240)
screengray = (130, 130, 130)
cloudgray1 = (100, 100, 100)
cloudgray2 = (75, 75, 75)
cloudgray3 = (105, 105, 105)
cloudgray4 = (30, 30, 30)
balconygray = (35, 35, 35)
ghostgray = (200, 200, 200)
brown = (40, 20, 0)
yellow = (255, 204, 0)
pink = (91, 82, 75)
housecolor = (42,36, 2)
lightblue = (173, 216, 230)
white = (255, 255, 255)
black = (0, 0, 0)

def background():
    #фон
    rect(screen, screengray, (0, 0, 600, 300))
def clouds_n_stuff():
    #луна
    circle(screen, moongray, (525, 75), 50)
    #облака
    ellipse(screen, cloudgray4, (200, 175, 600, 50))
    ellipse(screen, cloudgray2, (50, 82, 450, 55))
    ellipse(screen, cloudgray1, (300, 62, 325, 50))
    ellipse(screen, cloudgray3, (350, 120, 600, 50))
def house(x, y, i, s):
    #крыша
    polygon(s, black, [(x-int(25*i),y),(x+int(25*i), y-int(abs(30*i))),(x+int(275*i), y-int(abs(30*i))),(x+int(325*i), y)])
    #дом
    rect(s, housecolor, (x, y, int(abs(300*i)), int(abs(350*i))))
    #трубы
    rect(s, balconygray, (x+int(42*i), y-int(abs(70*i)), int(abs(8*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(150*i), y-int(abs(70*i)), int(abs(8*i)), int(abs(40*i))))
    rect(s, balconygray, (x+int(55*i), y-int(abs(95*i)), int(abs(20*i)), int(abs(80*i))))
    rect(s, balconygray, (x+int(257*i), y-int(abs(65*i)), int(abs(8*i)), int(abs(55*i))))
    #окна
    rect(s, brown, (x+int(37*i), y+int(abs(215*i)), int(abs(50*i)), int(abs(80*i))))
    rect(s, brown, (x+int(125*i), y+int(abs(215*i)), int(abs(50*i)), int(abs(80*i))))
    rect(s, yellow, (x+int(213*i), y+int(abs(215*i)), int(abs(50*i)), int(abs(80*i))))
    #бежевые штуки
    rect(s, pink, (x+int(15*i), y, int(abs(35*i)), int(abs(125*i))))
    rect(s, pink, (x+int(90*i), y, int(abs(35*i)), int(abs(125*i))))
    rect(s, pink, (x+int(165*i), y, int(abs(35*i)), int(abs(125*i))))
    rect(s, pink, (x+int(240*i), y, int(abs(35*i)), int(abs(125*i))))
    #балкон
    rect(s, balconygray, (x-int(30*i), y+int(abs(130*i)), int(abs(360*i)), int(abs(30*i))))
    rect(s, balconygray, (x-int(13*i), y+int(abs(80*i)), int(abs(324*i)), int(abs(15*i))))
    #крайние по бокам
    rect(s, balconygray, (x-int(21*i), y+int(abs(95*i)), int(abs(8*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(311*i), y+int(abs(95*i)), int(abs(8*i)), int(abs(50*i))))
    #остальные
    rect(s, balconygray, (x+int(15*i), y+int(abs(95*i)), int(abs(20*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(77*i), y+int(abs(95*i)), int(abs(20*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(139*i), y+int(abs(95*i)), int(abs(20*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(201*i), y+int(abs(95*i)), int(abs(20*i)), int(abs(50*i))))
    rect(s, balconygray, (x+int(263*i), y+int(abs(95*i)), int(abs(20*i)), int(abs(50*i))))
def ghost(x, y, i, s):
    #привидение
    #тело
    ghostbody = [(x-int(19*np.sin(45*np.pi/180)*i),y+int(abs(19*np.sin(45*np.pi/180)*i))),
                 (x-int(45*i),y+int(abs(80*i))),(x-int(20*i),y+int(abs(70*i))),(x, y+int(abs(90*i))),
                 (x+int(20*i), y+int(abs(75*i))),(x+int(50*i), y+int(abs(95*i))),
                 (x+int(60*i),y+int(abs(80*i))),(x+int(70*i),y+int(abs(65*i))),(x+int(85*i), y+int(abs(55*i))),
                 (x+int(80*i), y+int(abs(50*i))),(x+int(19*i), y)]
    polygon(s, ghostgray, ghostbody)
    #голова, глаза, зрачки
    circle(s, ghostgray, (x, y), int(abs(20*i)))
    circle(s, lightblue, (x-int(7*i), y), int(abs(6*i)))
    circle(s, lightblue, (x+int(7*i), y-int(abs(2*i))), int(abs(6*i)))
    circle(s, black, (x-int(8*i), y), int(abs(2*i)))
    circle(s, black, (x+int(6*i), y-int(abs(2*i))), int(abs(2*i)))
    ellipse(s, white, (x-int(7*i),y-int(abs(2*i)), int(abs(5*i)), int(abs(3*i))))
    ellipse(s, white, (x+int(7*i),y-int(abs(4*i)), int(abs(5*i)), int(abs(3*i))))
background()
clouds_n_stuff()
house(50, 300, 0.5, screen)
house(245, 275, 0.5, screen)
ghost(475, 520, 1, screen)
ghost(500, 400, 0.5, screen)
ghost(50, 550, -0.5, screen)
#поверхность с градиентом
screen2 = pygame.Surface((600,650))
#закраска поверхности
rect(screen2, (1,1,1),(0,0,600,650))
#дома, привидения и облака с градиентом
ellipse(screen2, cloudgray4, (100, 250, 600, 65))
ellipse(screen2, cloudgray1, (150, 325, 600, 50))
ellipse(screen2, cloudgray2, (0, 350, 500, 50))
house(425, 170, 0.5, screen2)
ghost(400, 500, 0.5, screen2)
ghost(550, 425, 0.5, screen2)
ghost(75, 575, -0.5, screen2)
#параметры градиента
screen2.set_alpha(200)
screen2.set_colorkey((1,1,1))
screen.blit(screen2, (0,0))

pygame.display.update()
FPS = 30
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
