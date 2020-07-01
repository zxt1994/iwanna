import sys

import pygame

from source.componets.bullet import Bullet




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


def update_screen(iwan_settings, screen, kid, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(iwan_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    kid.bliteme()

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