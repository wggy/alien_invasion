import sys
import pygame
from src.bullet import Bullet
from src.alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, sb)


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb):
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
    elif event.key == pygame.K_p:
        restart_game(ai_settings, screen, stats, aliens, bullets, ship, sb)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    # elif event.key == pygame.K_UP:
    #     ship.move_up = False
    # elif event.key == pygame.K_DOWN:
    #     ship.move_down = False


def update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if stats.game_over:
        play_button.draw_button()
    # 让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, bullets, aliens, ship, stats, sb):
    # 更新子弹的位置
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, aliens, bullets, ship, stats, sb)


def fire_bullets(bullets, ai_settings, screen, ship):
    if len(bullets) >= ai_settings.bullet_allowed:
        print('bullet is over 3.')
    else:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for alien_number in range(number_aliens_x):
        for alien_row in range(number_rows):
            aliens.add(create_alien(ai_settings, screen, alien_number, alien_row))


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def create_alien(ai_settings, screen, alien_number, alien_row):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien_height = alien.rect.height
    alien.y = alien_height + 2 * alien_row * alien_height
    alien.rect.y = alien.y
    return alien


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - ship_height - alien_height * 4
    available_rows = int(available_space_y / (2 * alien_height))
    return available_rows


def update_aliens(ai_settings, screen, aliens, bullets, ship, stats):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, aliens, bullets, ship, stats)
    check_aliens_bottom(ai_settings, screen, aliens, bullets, ship, stats)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(ai_settings, aliens)
            break


def change_alien_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_bullet_alien_collisions(ai_settings, screen, aliens, bullets, ship, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        print(collisions)
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
    if len(aliens) == 0:
        ai_settings.increase_speed()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


def ship_hit(ai_settings, screen, aliens, bullets, ship, stats):
    stats.left_stats()
    if not stats.game_over:
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        sleep(1)
    else:
        pygame.mouse.set_visible(True)
        print('game over!!!')


def check_aliens_bottom(ai_settings, screen, aliens, bullets, ship, stats):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, aliens, bullets, ship, stats)
            break


def check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        restart_game(ai_settings, screen, stats, aliens, bullets, ship, sb)


def restart_game(ai_settings, screen, stats, aliens, bullets, ship, sb):
    if stats.game_over:
        ai_settings.init_dynamic_setting()
        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        stats.reset_stats()
        sb.show_score()
