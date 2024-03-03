import pygame

class Button:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(image)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Import_Button(Button):
    def __init__(self, x, y, w, h, image):
        pass