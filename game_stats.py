class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settintgs):
        """初始化统计信息"""
        self.ai_settintgs = ai_settintgs
        self.reset_stats()
        #游戏刚启动时处于非活跃状态
        self.game_active = False

        #最高分
        self.high_score = 0
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settintgs.ship_limit #剩余的ship
        self.score = 0
        self.level = 1
