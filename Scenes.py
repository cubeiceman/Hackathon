import pygame

class Scene:
    def __init__(self, width, height, image):
        self.width, self.height = width, height
        self.bg = image
        self.surface = pygame.Surface((width, height))
        self.active = True

    def add(self, type, key, value):
        # add some key and value to a determined dictionary inside the scene(game or menu)
        pass

    def handle_keyboard(self):
        # handles the keyboard, in this case, the quit button and the mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False

    def draw(self):
        # draws things onto the scene's surface, which is later drawn on the actual window
        pass

class Game_Scene(Scene):
    def __init__(self, width, height, image):
        super().__init__(width, height, image)
        self.active = True
        self.image_dict = {}

    def draw(self):
        self.surface.blit(self.bg, (0, 0))
