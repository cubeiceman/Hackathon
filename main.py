import pygame
from pygame.locals import *
import time
import Buttons
import Functions
import Scenes

pygame.init()

def game_loop(scene, win):
    Functions.check_user_input(scene)
    Functions.run_ai()
    Functions.move_everything()
    Functions.resolve_collisions()
    Functions.draw_scene(scene, win)
    Functions.play_sounds()


WIDTH, HEIGHT = pygame.display.get_desktop_sizes()[0]
HEIGHT -= 60
window = pygame.display.set_mode([WIDTH, HEIGHT], RESIZABLE)
c = pygame.time.Clock()
WHITE = (255, 255, 255)
GREY = (75, 75, 75)

BACKGROUND_IMAGE = pygame.image.load("bg placeholder.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

before_time = time.time()

game_scene = Scenes.Game_Scene(WIDTH, HEIGHT, BACKGROUND_IMAGE)

while game_scene.active:
    after_time = time.time()
    delta_time = after_time - before_time
    before_time = after_time

    game_loop(game_scene, window)

    c.tick(60)
