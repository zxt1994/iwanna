import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, iwan_setting, screen, kid):
        """在kid所处位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        #在（0,0）出创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, iwan_setting.bullet_width, iwan_setting.bullet_height)
        self.rect.centery = kid.rect.centery
        self.rect.right = kid.rect.right

        #存储小数表示子弹位置
        
        self.x = float(self.rect.x)

        self.color = iwan_setting.bullet_color
        self.speed_factor = iwan_setting.bullet_speed_factor


    def update(self):
        """向右移动子弹"""
        #更新表示子弹位置的小数值
        self.x += self.speed_factor
        #更新表示子弹的rect位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)