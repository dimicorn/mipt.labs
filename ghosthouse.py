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
house = (42,36, 2)
lightblue = (173, 216, 230)
white = (255, 255, 255)
black = (0, 0, 0)
def background():
    #фон
    rect(screen, screengray, (0, 0, 600, 300))
def first_layer():
    #луна
    circle(screen, moongray, (525, 75), 50)
    #облако за домом
    ellipse(screen, cloudgray4, (200, 175, 600, 50))
    #облако за домом
    ellipse(screen, cloudgray4, (200, 175, 600, 50))
    #дом
    rect(screen, house, (50, 170, 300, 350))
    #крыша
    polygon(screen, black, [(25,170),(75, 140),(325, 140),(375, 170)])
    #трубы за облаками
    rect(screen, balconygray, (92, 100, 8, 50))
    rect(screen, balconygray, (200, 100, 8, 40))
def second_layer():
    #все остальные облака
    ellipse(screen, cloudgray2, (50, 82, 450, 55))
    ellipse(screen, cloudgray1, (300, 62, 325, 50))
    ellipse(screen, cloudgray3, (350, 120, 600, 50))
    #трубы перед облаками
    rect(screen, balconygray, (105, 75, 20, 80))
    rect(screen, balconygray, (307, 105, 8, 55))
    #окна
    rect(screen, brown, (87, 385, 50, 80))
    rect(screen, brown, (175, 385, 50, 80))
    rect(screen, yellow, (263, 385, 50, 80))
    #бежевые штуки
    rect(screen, pink, (65, 170, 35, 125))
    rect(screen, pink, (140, 170, 35, 125))
    rect(screen, pink, (215, 170, 35, 125))
    rect(screen, pink, (290, 170, 35, 125))
    #балкон
    rect(screen, balconygray, (20, 300, 360, 30))
    rect(screen, balconygray, (37, 250, 324, 15))
    #крайние по бокам
    rect(screen, balconygray, (29, 265, 8, 50))
    rect(screen, balconygray, (361, 265, 8, 50))
    #остальные
    rect(screen, balconygray, (65, 265, 20, 50))
    rect(screen, balconygray, (127, 265, 20, 50))
    rect(screen, balconygray, (189, 265, 20, 50))
    rect(screen, balconygray, (251, 265, 20, 50))
    rect(screen, balconygray, (313, 265, 20, 50))
def ghost():
    #привидение
    #голова, глаза, зрачки
    circle(screen, ghostgray, (475, 520), 20)
    circle(screen, lightblue, (468, 520), 6)
    circle(screen, lightblue, (482, 518), 6)
    circle(screen, black, (467, 520), 2)
    circle(screen, black, (481, 518), 2)
    ellipse(screen, white, (468,518,5, 3))
    ellipse(screen, white, (482,516,5, 3))
    #тело
    ghostbody = [(475-19*np.sin(45*np.pi/180),520+19*np.sin(45*np.pi/180)),(430,600),(455,590),(475, 610),(495, 595),(525, 615),(535,600),(545,585),(560, 575),(555, 570),(475+19, 520)]
    polygon(screen, ghostgray, ghostbody)
background()
first_layer()
second_layer()
ghost()

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
