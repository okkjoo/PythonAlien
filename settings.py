"""
    包含Settings类 类中包含__init__()，负责初始化游戏外观和飞船速度属性
    
"""
class Settings():
    """
    存储外星人游戏的所有设置的类
    """
    def __init__(self) :
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        #创建宽3像素，高15像素的深灰色子弹，速递比飞船稍低,限制未消失的子弹为3颗
        self.bullet_speed_factor=1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #陨石设置
        self.aerolite_speed_factor = 1
        self.fleet_drop_speed = 15
        self.fleet_direction=1  #1表示向右，-1表示向左