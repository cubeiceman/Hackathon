import pygame

class Progress_Bar:
    def __init__(self, w, h, sx, sy):
        self.progress = 0
        self.max_bar_width = w

        self.max_bar_height = h
        self.max_chars = 10000
        self.current_chars = 0
        self.scale = self.progress / self.max_chars
        self.surface = pygame.Surface((self.max_bar_width, self.max_bar_height))
        self.rect = pygame.Rect(0, 0, w * self.scale, self.max_bar_height)
        self.bg_color = (0, 0, 0)
        self.color = (0, 255, 0)
        self.multiplier = 0
        self.surface_x = sx
        self.surface_y = sy

        #this draws the greenbar
    def draw(self, surface):
        self.surface.fill(self.bg_color)
        pygame.draw.rect(self.surface, self.color, self.rect)
        surface.blit(self.surface, (self.surface_x, self.surface_y))

    #this reads the charcount from notes and adds to the progress bar
    def add(self, char_count):
        self.progress += char_count
        self.scale = self.progress/self.max_chars
        while self.progress > self.max_chars:
            self.rect.width -= self.max_bar_width
            self.progress = 0
            self.multiplier += 1
        self.rect.width = self.max_bar_width * self.scale

