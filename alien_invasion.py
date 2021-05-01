import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # display.set_mode()返回的surface表示整个游戏窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
