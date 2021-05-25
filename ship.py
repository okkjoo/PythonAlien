"""
    包含Ship类，其中包含方法__init__(),
                update()管理飞船位置
                blitme()在屏幕上绘制飞船的方法
                表示飞船的图像存储在images的ship.bmp中
"""
import pygame
class Ship():
    def __init__(self,ai_settings,screen) :#第三个参数指定要将飞船绘制到什么地方
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外界矩形
        #为加载图像，我们调用了pygame.image.load()这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        #更新飞船的center值，而不是rect
        #修改self.center的值之前检查飞船位置，确保飞船在屏幕内
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor 
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor 
        #根据self.center更新rect对象
        self.rect.centerx = self.center#self.rect.centerx将只存储self.center的整数部分，但对显示飞船而言，这问题不大0
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)