import pygame

from source.settings import Settings
from source.componets.kid import Kid
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    iwan_settings = Settings()
    screen = pygame.display.set_mode((iwan_settings.screen_width, iwan_settings.screen_height))

    pygame.display.set_caption("I Wanna")

    kid=Kid(screen, iwan_settings)

    bullets = Group()
    rect = screen.get_rect()

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(iwan_settings, screen, kid, bullets)
        kid.update()
        gf.update_bullets(bullets, rect)
        gf.update_screen(iwan_settings, screen, kid, bullets)

run_game()