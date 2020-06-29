import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem e define seu atributo rect
        self.image = pygame.image.load('naves/alien.bmp')
        self.rect = self.image.get_rect()

        # Posiciona inicialmente à parte superior esquerda da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena em sua posição atual
        self.x = float(self.rect.x)

    def blitme(self): # Desenha o alien (no local atual)
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
