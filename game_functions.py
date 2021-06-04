"""
    包含完成游戏的大部分工作的函数
    check_events()检测相关事件如按键和松开
        其中有辅助函数check_keydown_events 和 check_keyup_events
        来处理这些事件
    update_screen()用于在每次执行主循环时重绘屏幕
"""
import sys
import pygame
from bullet import  Bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有到达限制就继续添加子弹"""
    #创建一颗子弹，并将其 加入到编组中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    """"响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings,screen,ship,bullets):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在所有飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet();
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():  # 遍历编组的副本，这样才能在循环中修改bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))   # 测试