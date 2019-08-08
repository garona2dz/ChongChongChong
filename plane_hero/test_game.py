import pygame
import  sys
from pygame.locals import *
from plane_sprite import *
pygame.init()

running = True
screen = pygame.display.set_mode((480,700))
clock1 = pygame.time.Clock()

bg = pygame.image.load("./images/background.png")
me = pygame.image.load("./images/me1.png")
screen.blit(bg, (0, 0))
screen.blit(me,(189,300))


me_position = Rect(189,300,102,126)

enemy = GameSprite("./images/enemy1.png", 4)
enemy1 = GameSprite("./images/enemy1.png", 8)

enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    me_position.y -= 10

    if me_position.y + me_position.height < 0:
        me_position.y = (me_position.y + me_position.height) % 700 # 取余使能够循环

    screen.blit(bg, (0, 0))
    screen.blit(me, me_position)

    enemy_group.update() # 让组中所有精灵更新
    enemy_group.draw(screen)  # 精灵组调用方法来实现来绘制界面

    pygame.display.update()
    clock1.tick(60)



