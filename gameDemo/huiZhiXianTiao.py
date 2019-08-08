import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 80, 0))
    color = 255, 255, 0
    width = 50
    pygame.draw.line(screen, color, (100,100), (500, 400), width)
    pygame.display.update()