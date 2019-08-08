"""
绘制椭圆，就是绘制弧形，矩形的长和宽是长轴和短轴
"""
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
    position = 200, 150, 300, 200
    star_angle = math.radians(0)
    end_angle = math.radians(360)
    width = 10
    pygame.draw.arc(screen, color, position, star_angle, end_angle, width)
    pygame.display.update()