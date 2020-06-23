import pygame

class Config():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.sprit_image = pygame.image.load("imagem.jpg")
        # self.bg_color = (230, 230, 230)
        self.velocidade_nave = 25
