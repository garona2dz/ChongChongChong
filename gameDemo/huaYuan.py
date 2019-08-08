import pygame, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))  # 界面大小
pygame.display.set_caption("Drawing Circles")  # 标题内容
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 100, 200))  # 填充的背景颜色
    color = 255, 255, 0  # 定义颜色
    position = 300, 300  # 圆心位置
    radius = 100  # 圆的半径
    width = 10  # 线条粗细
    pygame.draw.circle(screen, color, position, radius, width)  # 画圆函数
    pygame.display.update()  # 刷新界面显示
