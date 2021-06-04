import pygame
from pygame.sprite import  Sprite
class Bullet(Sprite):#继承了从模块pygame.sprite中导入的 Sprite 类，通过使用精灵可将游戏中的相关元素编组，从而操作编组中的元素
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()#调用super()继承Sprite
        self.screen = screen
        #在(0,0)出创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)#使用pygame.Rect创建子弹的属性rect
        #子弹从飞船顶部射出
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储用小数(为了能微调子弹的速度)表示的子弹位置
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    

    ##方法
    def update(self):
        """向上更新子弹模拟子弹射出"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect位置
        self.rect.y = self.y
    
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)