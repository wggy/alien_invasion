import sys
import pygame
from src.bullet import Bullet
from src.alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    # elif event.key == pygame.K_UP:
    #     ship.move_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    # elif event.key == pygame.K_UP:
    #     ship.move_up = False
    # elif event.key == pygame.K_DOWN:
    #     ship.move_down = False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹的位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(bullets, ai_settings, screen, ship):
    if len(bullets) >= ai_settings.bullet_allowed:
        print('bullet is over 3.')
    else:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    for alien_number in range(number_aliens_x):
        aliens.add(create_alien(ai_settings, screen, alien_number))


def get_number_aliens_x(ai_settings, alien_width):
    availabel_space_x = ai_settings.screen_width - 2 * alien_width
    return int(availabel_space_x / (2 * alien_width))


def create_alien(ai_settings, screen, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    return alien
