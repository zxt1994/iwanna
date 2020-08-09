import pygame

from source.settings import Settings
from source.componets.kid import Kid
import game_functions as gf
from pygame.sprite import Group
from source.game_stats import GameStats
from source.componets.thorn import Thorn

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    iwan_settings = Settings()
    screen = pygame.display.set_mode((iwan_settings.screen_width, iwan_settings.screen_height))

    pygame.display.set_caption("I Wanna")

    kid=Kid(screen, iwan_settings)
    #创建一个角色、一个子弹编组和一个尖刺编组

    thorns = Group()
    bullets = Group()
    rect = screen.get_rect()

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(iwan_settings)

    #创建一个尖刺群
    gf.create_thorngroup(iwan_settings, screen, thorns)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(iwan_settings, screen, kid, bullets)
        kid.update()
        gf.update_bullets(bullets, rect)
        gf.update_screen(iwan_settings, screen, kid, thorns, bullets)
        gf.update_thorns(iwan_settings, stats, screen, kid, thorns, bullets)

run_game()