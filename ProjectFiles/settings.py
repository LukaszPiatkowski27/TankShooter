import configparser


class Settings:

    def __init__(self):
        self.RESOLUTION = None
        self.FULL_SCREEN = None
        self.FPS = None
        self.UPS = None
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        self.config.read('config.ini')
        self.FULL_SCREEN = self.config['ACTIVE'].getboolean('full_screen_mode')
        self.RESOLUTION = (self.WIDTH, self.HEIGHT) = (
            int(self.config['ACTIVE']['resolution_width']),
            int(self.config['ACTIVE']['resolution_height'])
        )
        self.FPS = int(self.config['ACTIVE']['fps'])
        self.UPS = int(self.config['ACTIVE']['ups'])

    def reset_config_to_default(self):
        self.config['ACTIVE'] = self.config['DEFAULT']
