class Settings():
    """存储iwanna的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #kid的设置
        self.kid_speed_factor = 0.25

        #子弹设置
        self.bullet_speed_factor = 0.7
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60