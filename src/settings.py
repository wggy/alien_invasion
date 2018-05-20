class Settings:

    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1
        self.ship_limit = 3

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 3
        self.bullet_allowed = 100

        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 50
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.alien_points = 50
        self.points_scale = 1.5

    def init_dynamic_setting(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 0.5
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.points_scale * self.alien_points)
