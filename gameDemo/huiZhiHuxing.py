import math
import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 80, 200))
    color = 255, 255, 0
    position = 200, 150, 300, 300  # 矩形内画弧形，左上角位置参数和两边长
    star_angle = math.radians(0)
    end_angle = math.radians(160)  # 起始角度，0-360就是画圆、椭圆（最好到361，以免出现缝隙）
    width = 10
    pygame.draw.arc(screen, color, position, star_angle, end_angle, width)
    pygame.display.update()