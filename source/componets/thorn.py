import pygame
from pygame.sprite import Sprite

class Thorn(Sprite):
    """表示单个尖刺的类"""
    def __init__(self, iwan_settings, screen):
        super(Thorn, self).__init__()
        self.screen = screen
        self.iwan_settings = iwan_settings

        #加载尖刺图像，设置其rect属性
        self.initimage = pygame.image.load('D:/iwanna/images/thorn.png')
        self.image = pygame.transform.scale(self.initimage,(30, 30))
        self.rect = self.image.get_rect()

        #尖刺在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储尖刺的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制尖刺"""
        self.screen.blit(self.image, self.rect)