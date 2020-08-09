import sys

import pygame

from source.componets.bullet import Bullet
from source.componets.thorn import Thorn
from time import sleep


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



def get_number_thorns_x(iwan_settings, thorn_width):
    """计算每行可容纳哦多少个尖刺"""
    available_space_x = iwan_settings.screen_width - 2 * thorn_width
    number_thorns_x = int(available_space_x / (2 * thorn_width))
    return number_thorns_x

def create_thorn(iwan_settings, screen, thorns, thorn_number):
    """创建一个尖刺，并将其放在当前行"""
    thorn = Thorn(iwan_settings, screen)
    thorn_width = thorn.rect.width
    thorn.x = thorn_width + 2.15 * thorn_width * thorn_number
    thorn.rect.x = thorn.x
    thorns.add(thorn)

def create_thorngroup(iwan_settings, screen, thorns):
    """创建尖刺群"""
    # 创建一个尖刺，并计算一行可以容纳多少尖刺
    # 尖刺间的间距为尖刺的宽度
    thorn = Thorn(iwan_settings, screen)
    number_thorns_x = get_number_thorns_x(iwan_settings, thorn.rect.width)
    # 创建第一行尖刺
    for thorn_number in range(number_thorns_x):
        create_thorn(iwan_settings, screen, thorns, thorn_number)

def update_thorns(iwan_settings, stats, screen, kid, thorns, bullets):
    # 检测kid和尖刺之间的碰撞
    if pygame.sprite.spritecollideany(kid, thorns):
        kid_hit(iwan_settings, stats, screen, kid, thorns, bullets)
        print("kid is die!!!!")

def kid_hit(iwan_settings, stats, screen, kid, thorns, bullets):
    """响应被尖刺碰到的kid"""
    #将dienum加1
    stats.kid_die += 1

    #清空尖刺列表和子弹列表
    thorns.empty()
    bullets.empty()

    #创建一群新的尖刺，并让kid回到初始位置
    create_thorngroup(iwan_settings, screen, thorns)
    kid.org_kid()

    #暂停
    sleep(0.5)