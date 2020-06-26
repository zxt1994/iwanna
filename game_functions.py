import sys

import pygame

def check_events(kid):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动人物
                kid.rect.x += 1

def update_screen(iwan_settings, screen, kid):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(iwan_settings.bg_color)
    kid.bliteme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()