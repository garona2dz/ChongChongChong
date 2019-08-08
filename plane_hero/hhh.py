from pygame.locals import *
import pygame
import sys
import time
pygame.init()

bg = pygame.image.load("./images/background.png")
screen = pygame.display.set_mode((480,700))
clock = pygame.time.Clock()

def bomb():
    flash = []
    # names = locals()
    down1 = pygame.image.load("./images/enemy1_down1.png")
    down2 = pygame.image.load("./images/enemy1_down2.png")
    down3 = pygame.image.load("./images/enemy1_down3.png")
    down4 = pygame.image.load("./images/enemy1_down4.png")
    image_down = [down1, down2, down3, down4]
    for i in image_down:
        flash.append(i)
    #for enemies in self.enemies_down_group:
    #    enemies.speed = 0
     #   rect_x = enemies.rect.x
     #   rect_y = enemies.rect.y
        # while True:
    for i in range(0, 3):
        # time.sleep(0.1)
        j = 0
        while True:
            # clock.tick(100)
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                        sys.exit()

            screen.blit(flash[i], (100, 200))
            # pygame.display.update()
            j += 1
            if j == 100:
                break
            #time.sleep(0.05)
            print("jjjjj")
            pygame.display.update()
    #self.enemies_down_group.remove(enemies)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.blit(bg,(0, 0))
    #screen.blit(bg, (0, 0))
    bomb()
    print("hhhhh")
    # pygame.display.update()