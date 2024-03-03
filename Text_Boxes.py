import pygame
class Text_Box:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = "Type something to continue"

    def __str__(self):
        return self.text
