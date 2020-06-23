import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


# Inicializando o jogo e criando o objeto "tela"

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)

    # ----------

    pygame.mixer.init()
    pygame.mixer.music.load('music/memories.mp3')
    pygame.mixer.music.play()

    # ----------

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
