import pygame
import threading
import time
from settings import Settings
from main_menu import MainMenu


class Game:

    def __init__(self):
        pygame.init()
        self.EXIT_EVENT = pygame.USEREVENT
        self.settings = Settings()

        self.title_font = pygame.font.Font(None, 64)
        self.width = self.settings.WIDTH
        self.height = self.settings.HEIGHT
        flags = pygame.FULLSCREEN if self.settings.FULL_SCREEN else 0
        self.screen = pygame.display.set_mode(self.settings.RESOLUTION, flags)
        pygame.display.set_caption("Tank Shooter")

        self.fixed_update_thread = threading.Thread(target=self.fixed_update, daemon=True)
        self.running = False

        self.active_scene = MainMenu(self)

        self.clock = pygame.time.Clock()

    def update(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == self.EXIT_EVENT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(self.active_scene.buttons)):
                        if self.active_scene.buttons[i].hover():
                            self.active_scene.buttons[i].on_click()
                            break

            self.active_scene.draw()
            pygame.display.update()
            self.clock.tick(self.settings.FPS)

    def fixed_update(self):
        while self.running:
            # all the physics / logic updates
            time.sleep(1 / self.settings.UPS)

    def run(self):
        self.running = True
        self.fixed_update_thread.start()
        self.update()


game = Game()
game.run()
















