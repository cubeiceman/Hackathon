import pygame
import time

class Text_Box:
    def __init__(self, x, y, w, h, f, c, bgc):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.font = f
        self.color = c
        self.bg_color = bgc
        self.can_add = True

    def add(self, letter):
        if self.can_add:
            self.text += letter
        if len(self.text) > 200:
            self.can_add = False
        else:
            self.can_add = True

    def draw(self, surface):
        text_show = self.font.render(self.text, False, self.color)
        cursor_rect = pygame.Rect(self.rect.x + text_show.get_width(), self.rect.y, 5, text_show.get_height())

        pygame.draw.rect(surface, self.bg_color, self.rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(surface, self.color, cursor_rect)
        surface.blit(text_show, (self.rect.x, self.rect.y))
