import pygame.event
from button import Button
from scene import Scene


class MainMenu(Scene):

    def __init__(self, game):
        Scene.__init__(self, game)
        self.EXIT_EVENT = game.EXIT_EVENT
        self.game = game

        self.title = game.title_font.render("TANK SHOOTER", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(self.width / 2, self.height / 8))

        first_btn_top = 3 * self.height / 11

        for i in range(5):
            self.buttons.append(
                Button(
                    self.surface,
                    size=(self.width / 2, 50),
                    center=(self.width / 2, first_btn_top + 75 * i)
                )
            )

        self.buttons[0].text = "SINGLE PLAYER"
        self.buttons[0].on_click = self.goto_single

        self.buttons[1].text = "LOCAL MULTIPLAYER (LAN)"
        self.buttons[1].on_click = self.goto_lan

        self.buttons[2].text = "HOT SEAT"
        self.buttons[2].on_click = self.goto_hot_seat

        self.buttons[3].text = "OPTIONS"
        self.buttons[3].on_click = self.goto_options

        self.buttons[4].text = "EXIT"
        self.buttons[4].on_click = self.exit
        self.buttons[4].rect.centery = first_btn_top + 340

    def draw(self):
        Scene.draw(self)
        self.surface.blit(self.title, self.title_rect)
        for i in range(len(self.buttons)):
            self.buttons[i].draw((150, 150, 150) if i != 4 else (200, 150, 150))

    def goto_single(self):
        print("SINGLE PLAYER")
        # TODO: go to GAME SCENE (SINGLE PLAYER)

    def goto_lan(self):
        print("LAN")
        # TODO: go to LAN CONNECTION SCENE

    def goto_hot_seat(self):
        print("HOT SEAT")
        # TODO: go to GAME SCENE (HOT SEAT)

    def goto_options(self):
        print("OPTIONS")
        # TODO: go to OPTIONS SCENE

    def exit(self):
        pygame.event.post(pygame.event.Event(self.EXIT_EVENT))