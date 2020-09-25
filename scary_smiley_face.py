import pygame
from pygame.draw import *

pygame.init()


screen = pygame.display.set_mode((400, 400))
gray = (200, 200, 200)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
rect(screen, gray, (0, 0, 400, 400))
circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)
rect(screen, black, (162, 250, 75, 17))
circle(screen, red, (150, 175), 23)
circle(screen, black, (150, 175), 10)
circle(screen, red, (250, 175), 20)
circle(screen, black, (250, 175), 7)
polygon(screen, black, [(150,125),(190, 190),(180, 180),(145, 130)])
polygon(screen, black, [(220,190),(250,125),(255,120),(225,195)])
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
