import pygame

class Kid():

    def __init__(self, screen):
        """初始化kid并设置其初始位置"""

        self.screen = screen

        #加载kid图像并获取其外接矩形

        self.initimage = pygame.image.load('images/kid.png')
        self.image = pygame.transform.scale(self.initimage,(30, 30))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将kid初始化位置放在屏幕左侧
        self.rect.x = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

    def bliteme(self):
        """在指定位置绘制kid"""
        self.screen.blit(self.image, self.rect)