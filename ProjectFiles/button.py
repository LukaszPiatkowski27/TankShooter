import pygame


class Button:

    def __init__(self, surface, size, center, on_click=None,
                 bg_color=(100, 100, 100), fg_color=(255, 255, 255), txt=""):
        self.surface = surface
        self.size = size
        self.rect = pygame.Rect(center[0] - size[0] / 2, center[1] - size[1] / 2, size[0], size[1])
        self.on_click = on_click
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text = txt
        self.font = pygame.font.Font(None, 32)

    def hover(self) -> bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, bg_hover=None, fg_hover=None):
        if self.hover():
            pygame.draw.rect(self.surface, bg_hover if bg_hover is not None else self.bg_color, self.rect)
            caption = self.font.render(self.text, True, fg_hover if fg_hover is not None else self.fg_color)
        else:
            pygame.draw.rect(self.surface, self.bg_color, self.rect)
            caption = self.font.render(self.text, True, self.fg_color)
        caption_rect = caption.get_rect(center=self.rect.center)
        self.surface.blit(caption, caption_rect)
