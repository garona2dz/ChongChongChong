import pygame
import  sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((480,700))
bg = pygame.image.load("./images/background.png")
me1 = pygame.image.load("./images/me1.png")
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.blit(bg, (0, 0))  # 对齐的坐标
    screen.blit(me1, (189, 400))
    pygame.display.update()  # 显示内容



pygame.quit()
