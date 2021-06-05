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
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from aerolite import Aerolite
import game_functions as gf
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))   
    pygame.display.set_caption("Aerolite Hit Airship")
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group();# pygame.sprite中的Group类
    # 创建一个用于存储陨石的编组
    aerolites = Group();# pygame.sprite中的Group类
    # 创建陨石群
    gf.create_fleet(ai_settings,screen,ship,aerolites)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aerolites,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aerolites,bullets)
            gf.update_aerolites(ai_settings,stats,screen,ship,aerolites,bullets)
            #每次循环时都重新绘制屏幕 让最近的屏幕绘制可见
        gf.update_screen(ai_settings,screen,stats,ship,aerolites,bullets,play_button)
run_game()
