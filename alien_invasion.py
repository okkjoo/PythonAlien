"""
    创建一系列整个游戏都要用到的对象：
        存储在ai_settings中的设置
        存储在screen中的主显示surface
        一个飞船实例
    包含游戏的主循环while：
        在其中调用了 check_events()
                    ship.update()
                    update_screen()
    要启动该游戏 只需运行该文件，其他文件包含的代码被直接或间接地导入这个文件中
    
"""    
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))   
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #设置背景色
    # bg_color =(230,230,230)#浅灰
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #每次循环时都重新绘制屏幕 让最近的屏幕绘制可见
        gf.update_screen(ai_settings,screen,ship)
run_game()
