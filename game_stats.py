class GameStats():
    # Armazena dados estatísticos do Alien Invasion
    def __init__(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicia  o jogo em um estado inativo
        self.game_active = False

        # a pontuação não deve ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        # Inicializa os dados estatísticos que podem mudar durante o jogo
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0