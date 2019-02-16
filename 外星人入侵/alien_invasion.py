import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
#from bullet import Bullet
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    sb = Scoreboard(ai_settings, screen, stats)
    #创建一个子弹组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets, sb)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)
run_game()