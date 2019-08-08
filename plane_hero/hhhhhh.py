import pygame
from pygame.locals import *
pygame.init()


a = pygame.image.load("./images/background.png")
screen = pygame.display.set_mode((580, 700))

j = 0
while True:
    screen = pygame.display.set_mode((480, 700))
    #screen.blit(a,(0,0))
    screen.blit(a,(0, 0))
    j += 1
    if j >= 10:
        break
    pygame.display.update()
#pygame.time.wait(1000)
