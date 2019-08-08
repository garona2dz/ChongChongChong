import pygame
import sys
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")
pos_x = 250
pos_y = 250  # 矩形左上角初始位置
v_x = random.randint(5, 10)
v_y = random.randint(3, 5)  # 移动速度
color = 255, 255, 0
width = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0, 100, 200))  # 填充背景颜色

    pos_x += v_x
    pos_y += v_y  # 矩形移动起来
    position = pos_x, pos_y, 200, 100  # 绘制矩形的左上角顶点位置和两边长参数
    # color = 255, 255, 0
    # color = random.choice([0, 0, 255]), random.choice([0, 0, 255]), random.choice([0, 0, 255])
    """
    牛逼的七彩亮瞎眼颜色哈哈哈哈哈哈
    """
    if pos_x >= 400 or pos_x <= 0:
        v_x = -v_x
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        # color = random.choice([0, 120,255,]), 0, 0
    if pos_y >= 400 or pos_y <= 0:  # 判断是否触碰到边界
        v_y = -v_y  # 触碰边界后反向移动
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    pygame.draw.rect(screen, color, position, width)
    pygame.display.update()

    tp=clock.tick(1000)  # 最快帧数，但是电脑运行跟不上
    print(tp)


