import sys

import pygame


def check_keydown_events(event, kid):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动人物
        kid.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动人物
        kid.moving_left = True
    elif event.key == pygame.K_LSHIFT:
        kid.moving_up = True
        kid.moving_down = False




def check_keyup_event(event, kid):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        kid.moving_right = False
    elif event.key == pygame.K_LEFT:
        kid.moving_left = False

    elif event.key == pygame.K_LSHIFT:
        kid.moving_up = False
        kid.moving_down = True

def check_events(kid):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, kid)


        elif event.type == pygame.KEYUP:
           check_keyup_event(event, kid)


def update_screen(iwan_settings, screen, kid):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(iwan_settings.bg_color)
    kid.bliteme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()