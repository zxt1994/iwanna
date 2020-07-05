import sys

import pygame

from source.componets.bullet import Bullet
from source.componets.thorn import Thorn



def check_keydown_events(event, iwan_settings, screen, kid, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动人物
        kid.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动人物
        kid.moving_left = True
        # 跳跃
    elif event.key == pygame.K_LSHIFT:
        kid.moving_up = True
        kid.moving_down = False

    elif event.key == pygame.K_z:
        # 创建一颗子弹，并将其加入到编组bullets中
        #new_bullet = Bullet(iwan_settings, screen, kid)
        #bullets.add(new_bullet)
        fire_bullet(iwan_settings, screen, kid, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(iwan_settings, screen, kid, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    new_bullet = Bullet(iwan_settings, screen, kid)
    bullets.add(new_bullet)

def check_keyup_event(event, iwan_settings, screen, kid, bullets):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        kid.moving_right = False
    elif event.key == pygame.K_LEFT:
        kid.moving_left = False

    elif event.key == pygame.K_LSHIFT:
        kid.moving_up = False
        kid.moving_down = True

def check_events(iwan_settings, screen, kid, bullets):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, iwan_settings, screen, kid, bullets)


        elif event.type == pygame.KEYUP:
           check_keyup_event(event, iwan_settings, screen, kid, bullets)


def update_screen(iwan_settings, screen, kid, thorns, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(iwan_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    kid.bliteme()

    thorns.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets, rect):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.x >= rect.right:
            bullets.remove(bullet)
    print(len(bullets))

def create_thorngroup(iwan_settings, screen, thorns):
    """创建尖刺群"""
    #创建一个尖刺，并计算一行可以容纳多少尖刺
    #尖刺间的间距为尖刺的宽度
    thorn = Thorn(iwan_settings, screen)
    thorn_width = thorn.rect.width
    available_space_x = iwan_settings.screen_width - 2 * thorn_width
    number_thorns_x = int(available_space_x / (2 * thorn_width))

    #创建第一行尖刺
    for thorn_number in range(number_thorns_x):
        #创建一个尖刺并将其加入当前行
        thorn = Thorn(iwan_settings, screen)
        thorn.x = thorn_width + 2 * thorn_width * thorn_number
        thorn.rect.x = thorn.x
        thorns.add(thorn)