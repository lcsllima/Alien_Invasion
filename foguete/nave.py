import pygame

class Nave():

    def __init__(self, ai_config, screen):
        self.screen = screen
        self.ai_config = ai_config
        self.image = pygame.image.load('Rnave_maneira.png')
        # reconhecendo como um retangulo
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):



        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.centerx += self.ai_config.velocidade_nave
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_config.velocidade_nave
        # Tentando subir a nave
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_config.velocidade_nave
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_config.velocidade_nave

        # Atualiza o objeto rect de acordo com o self.center
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)

