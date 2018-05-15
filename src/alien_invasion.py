import pygame
from src.settings import Settings
from src.ship import Ship
import src.game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()

    pygame.display.set_caption('Alien Invasion')

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
