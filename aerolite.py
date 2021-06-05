import pygame
from pygame.sprite import  Sprite
class  Aerolite(Sprite):
    """表示陨石"""
    def __init__(self,ai_settings,screen):
        """初始化陨石并设置其初始位置"""
        super(Aerolite,self).__init__()
        self.screen =  screen
        self.ai_settings = ai_settings
        #加载陨石图像，并设置其rect属性
        self.image = pygame.image.load('images/aerolite.bmp')
        self.rect = self.image.get_rect()
        #在每个陨石都在最初的屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储陨石在屏幕上的位置
        self.x = float(self.rect.x)
    def blitme(self):
        """在指定位置绘制陨石"""
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        """如果外星人处于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left<=0: 
            return True

    def update(self):
        """向右或向左移动外星人"""
        self.x += (self.ai_settings.aerolite_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x