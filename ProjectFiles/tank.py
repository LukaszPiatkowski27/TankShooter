import pygame


class Tank:
    def __init__(self):
        self.tank_base_img = pygame.image.load('graphics/tank-base.png').convert()
        self.tank_barrel_img = pygame.image.load('graphics/tank-barrel.png').convert()
        self.tank_base_img.set_colorkey(pygame.Color(236, 64, 122))
