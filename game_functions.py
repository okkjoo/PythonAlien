"""
    包含完成游戏的大部分工作的函数
    check_events()检测相关事件如按键和松开
        其中有辅助函数check_keydown_events 和 check_keyup_events
        来处理这些事件
    update_screen()用于在每次执行主循环时重绘屏幕
"""
import sys
from time import sleep
import pygame
from bullet import  Bullet
from aerolite import  Aerolite
from random import randint
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
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
def check_events(ai_settings,screen,stats,sb,play_button,ship,aerolites,bullets):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aerolites,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aerolites,bullets,mouse_x,mouse_y):
    """在玩家单击play按钮的时候开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not  stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #清空陨石列表和子弹列表
        aerolites.empty()
        bullets.empty()
        #创建新的一群陨石，并让飞船居中
        create_fleet(ai_settings,screen,ship,aerolites)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aerolites,bullets,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在所有飞船和陨石后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet();
    ship.blitme()
    aerolites.draw(screen)
    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()
def update_bullets(ai_settings,screen,stats,sb,ship,aerolites,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():  # 遍历编组的副本，这样才能在循环中修改bullets
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_aerolite_colloisions(ai_settings,screen,stats,sb,ship,aerolites,bullets)

def check_bullets_aerolite_colloisions(ai_settings,screen,stats,sb,ship,aerolites,bullets):
    """响应子弹和陨石的碰撞"""
    #删除发生碰撞的子弹与陨石
    collisions = pygame.sprite.groupcollide(bullets,aerolites,True,True)
    if collisions:
        for aerolites in collisions.values():
            stats.score += ai_settings.aerolite_points*len(aerolites)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aerolites) == 0: #检查陨石群是否已被消灭完，如果被消灭完了：
        #提高等级
        stats.level += 1
        sb.prep_level()
        #删除现有的子弹并重新创建陨石群
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aerolites)

def get_number_aerolite_x(ai_settings,aerolite_width):
    """计算每行可容纳多少陨石"""
    available_space_x = ai_settings.screen_width - ( 2 * aerolite_width )
    number_aerolite_x = int(available_space_x / (2*aerolite_width))
    return number_aerolite_x
def get_number_rows(ai_settings,ship_height,aerolite_height):
    """计算屏幕可容纳多少行陨石"""
    available_space_y = (ai_settings.screen_height - (3*aerolite_height)-ship_height)
    number_rows = int(available_space_y / (2*aerolite_height))
    return number_rows
def create_aerolite(ai_settings,screen,aerolites,aerolite_number,row_number):
    """ 创建一行陨石并将其放在当前行 """
    aerolite = Aerolite(ai_settings,screen)
    aerolite_width = aerolite.rect.width
    #陨石间距为陨石宽度
    aerolite.x = aerolite_width + 2*aerolite_width*aerolite_number
    aerolite.rect.x = aerolite.x
    aerolite.rect.y = 0.5*aerolite.rect.height + 1.5*aerolite.rect.height * row_number
    aerolites.add(aerolite)
def create_fleet(ai_settings,screen,ship,aerolites):
    """创建陨石群"""
    #创建一个陨石，用来计算一行可容纳多少陨石
    aerolite = Aerolite(ai_settings,screen)
    number_aerolite_x = get_number_aerolite_x(ai_settings,aerolite.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,aerolite.rect.height)
    #创建陨石群
    for row_number in range(number_rows):
        # for aerolite_number in range(number_aerolite_x):
        random_number = randint(3,number_aerolite_x)
        for aerolite_number in range(random_number):
            #创建一个陨石并将其加入当前行
            create_aerolite(ai_settings,screen,aerolites,aerolite_number,row_number)
def check_fleet_edges(ai_settings,aerolites):
    """有外星人到达边缘时采取相应的措施"""
    for aerolite in aerolites.sprites():
        if aerolite.check_edges():
            change_fleet_direction(ai_settings,aerolites)
            break
def change_fleet_direction(ai_settings,aerolites):
    """将陨石群向下移动并且 改变他们的方向"""
    for aerolite in aerolites.sprites():
        aerolite.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,screen,stats,sb,ship,aerolites,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #ship_left-1
        stats.ships_left -= 1
        #更新记分牌
        sb.prep_ships()
        #清空陨石列表和子弹列表
        aerolites.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings, screen, ship, aerolites)
        ship.center_ship()
        #暂停
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aerolites_bottom(ai_settings,screen,stats,sb,ship,aerolites,bullets):
    """检查是否有陨石到达了屏幕底部"""
    screen_rect = screen.get_rect()
    for aerolite in aerolites.sprites():
        if aerolite.rect.bottom > screen_rect.bottom:
            #像飞船被撞到了一个处理
            ship_hit(ai_settings,screen,stats,sb,ship,aerolites,bullets)
            break
def update_aerolites(ai_settings,screen,stats,sb,ship,aerolites,bullets):
    """检查是否有陨石位于屏幕边缘，并更新陨石群的位置"""
    check_fleet_edges(ai_settings,aerolites)
    aerolites.update()
    #检测陨石与飞机的碰撞
    if pygame.sprite.spritecollideany(ship,aerolites):
        ship_hit(ai_settings,screen,stats,sb,ship,aerolites,bullets)
    # 检查陨石是否有到达屏幕底部
    check_aerolites_bottom(ai_settings,screen,stats,sb,ship,aerolites,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了新的最高分"""
    if  stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()