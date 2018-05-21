import pygame
from src.settings import Settings
from src.ship import Ship
import src.game_functions as gf
from pygame.sprite import Group
from src.game_stats import GameStats
from src.button import Button
from src.scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.display.set_caption('Alien Invasion')

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    play_button = Button(ai_settings, screen, 'Play')

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)
        if not stats.game_over:
            ship.update()
            gf.update_bullets(ai_settings, screen, bullets, aliens, ship, stats, sb)
            gf.update_aliens(ai_settings, screen, aliens, bullets, ship, stats, sb)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)


run_game()
