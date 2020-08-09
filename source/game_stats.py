class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, iwan_settings):
        """初始化统计信息"""
        self.iwann_settings = iwan_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.kid_die = self.iwann_settings.kid_dienum