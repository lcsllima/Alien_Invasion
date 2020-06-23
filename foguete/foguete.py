import pygame

from config import Config
from nave import Nave
import game_functions as gf

def run_game():
    pygame.init()
    ai_config = Config()

    screen = pygame.display.set_mode((ai_config.screen_width, ai_config.screen_height))
    image = ai_config.sprit_image

    pygame.display.set_caption('Foguete')
    nave = Nave(ai_config, screen)

    while True:
        gf.check_events(nave)
        nave.update()
        gf.update_screen(image, screen, nave)

run_game()