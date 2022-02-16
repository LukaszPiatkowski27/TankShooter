import pygame.draw

from scene import Scene
from tank import Tank
from random import random


class GameScene(Scene):

    def __init__(self, game, mode=0):       # modes: 0 - single_player; 1 - lan; 2 - hot seat
        Scene.__init__(self, game)
        self.mode = mode
        self.player = Tank()
        self.opponent = Tank()
        self.map = []
        self.generate_map(100, 100, 300, 10)

    def draw(self):
        Scene.draw(self)
        self.draw_map()

    def generate_map(self, vertex_count, min_elevation, max_elevation, split):
        self.map = []
        generated = []
        for i in range(vertex_count):
            generated.append(random() * (max_elevation - min_elevation) + self.height - max_elevation)
        for i in range(split):
            temp = generated
            generated = [temp[0]]
            for j in range(1, len(temp), 2):
                generated.append((temp[j - 1] + temp[j]) / 2)
                if j < len(temp) - 1:
                    generated.append((temp[j + 1] + temp[j]) / 2)
            generated.append(temp[-1])
            self.map = generated

    def draw_map(self):
        poly_map = [(i * self.width / (len(self.map) - 1), value) for i, value in enumerate(self.map)]
        poly_map.append((self.width, self.height))
        poly_map.append((0, self.height))
        pygame.draw.polygon(
            self.surface,
            (150, 150, 150),
            poly_map
        )
