"""
    包含Settings类 类中包含__init__()，负责初始化游戏外观和飞船速度属性
    
"""
class Settings():
    """
    存储外星人游戏的所有设置的类
    """
    def __init__(self) :
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #飞船设置
        self.ship_limit = 3

        #子弹设置
        #创建宽3像素，高15像素的深灰色子弹，速递比飞船稍低,限制未消失的子弹为3颗
        self.bullet_width = 30000
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #陨石设置
        self.fleet_drop_speed = 15

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2
        #陨石分数的提高速度
        self.score_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor=3
        self.aerolite_speed_factor = 1
        self.fleet_direction=1  #1表示向右，-1表示向左
        
        #计分
        self.aerolite_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.aerolite_speed_factor *= self.speedup_scale
        self.aerolite_points = int(self.aerolite_points * self.score_scale)
        # print(self.aerolite_points)#测试