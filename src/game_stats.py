class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.game_over = True

    def left_stats(self):
        if self.ships_left > 0:
            self.ships_left -= 1
        else:
            self.game_over = True

    def reset_stats(self):
        self.game_over = False
        self.ships_left = self.ai_settings.ship_limit
