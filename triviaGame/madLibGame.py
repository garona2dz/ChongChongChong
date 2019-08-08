import sys
import pygame
# import datetime
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("MaD Lib")
# print(datetime.datetime.now())
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.fill((0, 20, 200))
    pygame.display.update()
