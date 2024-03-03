import pygame

class Weapon:
    def __init__(self, name:str, strength:int, image_loc:str):
        self.name = name
        self.strength = strength
        self.image = pygame.image.load(image_loc)
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.small_img = pygame.transform.scale(self.image, (200, 200))
    
    def __str__(self):
        return f"{self.name}, Strength: {self.strength}"

    def return_name(self):
        return self.name
    
    def return_strength(self):
        return self.strength
    
    def draw(self, surface:pygame.Surface, loc:tuple):
        surface.blit(self.image, self.image.get_rect(center=loc))
    
    def inventory_disp(self, surface, loc):
        pygame.draw.rect(surface, (255, 255, 255), self.small_img.get_rect(center=loc), border_radius = 10)
        surface.blit(self.small_img, self.small_img.get_rect(center=loc))