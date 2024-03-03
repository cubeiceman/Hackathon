import pygame
import Functions

class Scene:
    def __init__(self, width, height, image):
        self.width, self.height = width, height
        self.bg = image
        self.surface = pygame.Surface((width, height))
        self.active = True

    def add(self, value):
        # add some key and value to a determined dictionary inside the scene(game or menu)
        pass

    def handle_keyboard(self, text_box, keys, shift_keys, bar):
        # handles the keyboard, in this case, the quit button and the mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False
            if event.type == pygame.KEYDOWN:
                keys_state = pygame.key.get_pressed()
                if event.key == pygame.K_RETURN:
                    try:
                        chars = Functions.return_words(text_box.text)
                        #text_box.text = ""
                        bar.add(chars)
                    except FileNotFoundError:
                        pass
                if event.key == pygame.K_BACKSPACE:
                    text_box.text = text_box.text[:-1]
                try:
                    if keys_state[event.key] and (keys_state[pygame.K_RSHIFT] or keys_state[pygame.K_LSHIFT]):
                        text_box.add(shift_keys[event.key])
                    else:
                        text_box.add(keys[event.key])
                except KeyError:
                    pass


    def draw(self):
        # draws things onto the scene's surface, which is later drawn on the actual window
        pass

class Game_Scene(Scene):
    def __init__(self, width, height, image):
        super().__init__(width, height, image)
        self.active = True
        self.image_dict = {}
        self.text_box = None
        self.bar = None

    def add(self, value):
        self.text_box.append(value)

    def set_progress_bar(self, bar):
        self.bar = bar

    def set_text_box(self, val):
        self.text_box = val

    def draw(self):
        self.surface.blit(self.bg, (0, 0))
        self.text_box.draw(self.surface)
        self.bar.draw(self.surface)
