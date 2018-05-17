class Settings:

    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        self.bullet_height = 15
        self.bullet_width = 100
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 3
        self.bullet_allowed = 3

        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 50
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1
