import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞机图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery

        self.move_right = False
        self.move_left = False
        # self.move_up = False
        # self.move_down = False

        self.centerx = float(self.rect.centerx)
        # self.centery = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.move_left and self.screen_rect.left < self.rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        # if self.move_up and self.rect.top > self.screen_rect.top:
        #     self.centery -= self.ai_settings.ship_speed_factor
        # if self.move_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        # self.rect.centery = self.centery

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
