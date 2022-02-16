

class Scene:

    def __init__(self, game):
        self.surface = game.screen
        self.width = game.width
        self.height = game.height
        self.buttons = []

    def draw(self):
        self.surface.fill((43, 43, 43))
