import pygame
import time
from plane_sprite import *


pygame.init()
pygame.display.set_caption('Python打飞机大战')
my_font = pygame.font.Font(None, 44)


class PlaneGame(object):
    def __init__(self):

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.__create_sprites()

        pygame.time.set_timer(CREATE_ENEMY1_EVENT, 200)  # 定时器产生敌机1
        # pygame.time.set_timer(CREATE_ENEMY2_EVENT, 1000)

        pygame.time.set_timer(HERO_FIRE_EVENT, 200)  # 定时器发射子弹

    def __create_sprites(self):

        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)  # 新建背景组

        self.enemy1 = Enemy()
        self.enemy2 = Enemy_big()
        self.enemy1_group = pygame.sprite.Group()  # 新建敌机组
        self.enemy2_group = pygame.sprite.Group()
        self.enemy2_hit_group = pygame.sprite.Group()
        self.enemies_down_group = pygame.sprite.Group()  # 击毁敌机组

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)   # 新建英雄组

    def start_game(self):
        print("kai shi")
        while True:
            # 1 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2 事件监听
            self.__event_handler()
            # 3 碰撞检测
            self.__check_collide()
            # 4 更新精灵
            self.__update_sprites()
            # 5 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY1_EVENT:
                self.enemy1 = Enemy()
                self.enemy1_group.add(self.enemy1)  # 定时产生敌机1
            elif event.type == CREATE_ENEMY2_EVENT:
                self.enemy2 = Enemy_big()
                self.enemy2_group.add(self.enemy2)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # 一直按下键不能一直输入
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.__pause()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:  # 返回按键元组，如果被按下，对应数值为1
            self.hero.speed = 16
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -16
        else:
            self.hero.speed = 0

    def __check_collide(self):
        enemies1 = pygame.sprite.groupcollide(self.enemy1_group, self.hero.bullets, True, True)
        enemies2 = pygame.sprite.groupcollide(self.enemy2_group, self.hero.bullets, False, True)

        self.score += len(enemies1)   # 增加得分

        self.enemies_down_group.add(enemies1)
        self.enemy1_group.remove(enemies1)  # 敌机1的处理

        self.enemy2_hit_group.add(enemies2)
        for enemies2 in self.enemy2_group:
            enemies2.count += 1
            if enemies2.count >= 20:
                self.enemy2_group.remove(enemies2)

        # print(enemies)
        hero_hit = pygame.sprite.spritecollide(self.hero, self.enemy1_group, True,
                                               pygame.sprite.collide_circle_ratio(0.75))   # 精灵和精灵组的碰撞检测
        if len(hero_hit) > 0:
            # self.hero.kill()
            self.__over_again()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy1_group.update()
        self.enemy1_group.draw(self.screen)
        self.enemy2_group.update()
        self.enemy2_group.draw(self.screen)

        self.enemies_down_group.update()
        self.enemies_down_group.draw(self.screen)
        for enemies in self.enemies_down_group:
            enemies.down_index += 1

        self.enemy2_hit_group.update()
        self.enemy2_hit_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.change_index += 1
        if self.hero.change_index >= 7:
            self.hero.change_index = 0

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        text_score = my_font.render("SCORE : %d" % self.score, True, (0, 0, 0))
        self.screen.blit(text_score, (0, 670))

    def __pause(self):
        pit1 = pygame.image.load("./images/resume_nor.png")
        pit2 = pygame.image.load("./images/resume_pressed.png")
        while True:
            self.screen.blit(pit1, (210, 300))
            # pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_over()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # self.screen.blit(pit2, (210, 300))
                    # pygame.display.update()
                    j = 0
                    while True:
                        # self.screen = pygame.display.set_mode(SCREEN_RECT.size)
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                self.__game_over()
                        self.screen.blit(pit2, (210, 300))
                        pygame.display.update()
                        j += 1
                        if j >= 5:
                            break
                    # pygame.display.update()
                    self.start_game()
            pygame.display.update()

    def __over_again(self):
        self.score = 0
        ag = pygame.image.load("./images/again.png")
        be = pygame.image.load("./images/gameover.png")
        while True:
            self.screen.blit(ag, (90, 290))
            self.screen.blit(be, (90, 351))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_over()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (90 < x < 390) & (300 < y < 341):
                        self.start_game()
                    if (90 < x < 390) & (361 < y < 402):
                        self.__game_over()

    @staticmethod
    def __game_over():
        print("game over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
