import random
import pygame


SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 50
CREATE_ENEMY1_EVENT = pygame.USEREVENT
CREATE_ENEMY2_EVENT = pygame.USEREVENT + 1
HERO_FIRE_EVENT = pygame.USEREVENT + 2 # 用户常量直接加1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=0):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(image_name)
        self.speed = speed
        self.rect = self.image.get_rect()
        # self.mask = pygame.mask.from_surface(self.image)  # 指定蒙版

    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png", 21)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(14, 35)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = 0
        self.down_index = 0

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

        if (self.down_index >= 1) & (self.down_index <= 2):
            self.image = pygame.image.load("./images/enemy1_down1.png")
            return

        if (self.down_index >= 3) & (self.down_index <= 4):
            self.image = pygame.image.load("./images/enemy1_down1.png")
            return

        if (self.down_index >= 5) & (self.down_index <= 6):
            self.image = pygame.image.load("./images/enemy1_down3.png")
            return

        if (self.down_index >= 7) & (self.down_index <= 8):
            # self.speed = 0
            self.image = pygame.image.load("./images/enemy1_down4.png")
            return

        if self.down_index >= 9:
            # print(self.down_index)
            self.kill()
            return

class Enemy_big(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/enemy2.png")
        self.speed = 5
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = 0
        self.count = 0
        self.down_index = 0

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

        if (self.count >= 10) and (self.count <= 20):
            self.image = pygame.image.load("./images/enemy2_hit.png")
            return
        if (self.count >= 20):
            if (self.down_index >= 1) & (self.down_index <= 2):
                self.image = pygame.image.load("./images/enemy2_down1.png")
                return

            if (self.down_index >= 3) & (self.down_index <= 4):
                self.image = pygame.image.load("./images/enemy2_down1.png")
                return

            if (self.down_index >= 5) & (self.down_index <= 6):
                self.image = pygame.image.load("./images/enemy2_down3.png")
                return

            if (self.down_index >= 7) & (self.down_index <= 8):
                # self.speed = 0
                self.image = pygame.image.load("./images/enemy2_down4.png")
                return

        if self.down_index >= 9:
            # print(self.down_index)
            self.kill()
            return

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        #  self.rect.x = (SCREEN_RECT.width - self.rect.width)/2
        self.rect.centerx = SCREEN_RECT.centerx  # 矩形位置中心centerx
        self.rect.bottom = SCREEN_RECT.bottom - 60
        self.bullets = pygame.sprite.Group()
        self.change_index = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if (self.change_index >= 0) & (self.change_index <= 2):
            self.image = pygame.image.load("./images/me1.png")
            return

        if (self.change_index >= 3) & (self.change_index <= 6):
            self.image = pygame.image.load("./images/me2.png")
            # self.change_index = 0
            return

    def fire(self):
        for i in (-1, 1):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y
            bullet.rect.centerx = self.rect.centerx + i * 10
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -9)

    def update(self):
        super().update()
        if self.rect.bottom < 100:
            self.kill()
