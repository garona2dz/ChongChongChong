import math
import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Welcome to Pie Game")
my_font = pygame.font.Font(None, 60)
color = 200, 80, 80
width = 5
x = 300
y = 250
radius = 200
arc_position = x - radius, y - radius, radius * 2, radius * 2
piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    screen.fill((255, 255, 255))

    text1 = my_font.render("1", True, color)
    screen.blit(text1, (x + radius / 2, y - radius / 2))
    text2 = my_font.render("2", True, color)
    screen.blit(text2, (x - radius / 2, y - radius / 2))
    text3 = my_font.render("3", True, color)
    screen.blit(text3, (x - radius / 2, y + radius / 2))
    text4 = my_font.render("4", True, color)
    screen.blit(text4, (x + radius / 2, y + radius / 2))

    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(91)
        pygame.draw.arc(screen, color, arc_position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(181)
        pygame.draw.arc(screen, color, arc_position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(271)
        pygame.draw.arc(screen, color, arc_position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(361)
        pygame.draw.arc(screen, color, arc_position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)

    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0

    pygame.display.update()



