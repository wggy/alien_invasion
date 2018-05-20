class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.game_over = True
        self.score = 0
        self.high_score = 0

    def left_stats(self):
        if self.ships_left > 1:
            self.ships_left -= 1
        else:
            self.game_over = True

    def reset_stats(self):
        self.score = 0
        self.game_over = False
        self.ships_left = self.ai_settings.ship_limit
