import pygame

class Kid():

    def __init__(self, screen, iwan_settings):
        """初始化kid并设置其初始位置"""

        self.screen = screen
        self.iwan_settings=iwan_settings
        #加载kid图像并获取其外接矩形

        self.initimage = pygame.image.load('./../images/kid.png')
        self.image = pygame.transform.scale(self.initimage,(30, 30))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将kid初始化位置放在屏幕左侧
        self.rect.x = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom


        #在kid属性x中存入最小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = True

    def update(self):
        """根据移动标志调整kid位置"""
        #更新飞船的x值，而不是rect
        if self.moving_right:
            self.x += self.iwan_settings.kid_speed_factor
        if self.moving_left:
            self.x -= self.iwan_settings.kid_speed_factor
        if self.moving_up:
            self.y -= self.iwan_settings.kid_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.iwan_settings.kid_speed_factor


        #根据self.x更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def bliteme(self):
        """在指定位置绘制kid"""
        self.screen.blit(self.image, self.rect)

    def org_kid(self):
        """让kid回到初始位置"""
        self.x = self.screen_rect.left
        self.bottom = self.screen_rect.bottom