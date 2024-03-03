import pygame
from pygame.locals import *
import time
import Buttons
import Functions
import Scenes
import Text_Boxes

pygame.init()


WIDTH, HEIGHT = 1600, 900
window = pygame.display.set_mode([WIDTH, HEIGHT], RESIZABLE)
c = pygame.time.Clock()
WHITE = (255, 255, 255)
GREY = (75, 75, 75)

TYPE_FONT = pygame.font.SysFont('Arial', 20)
BACKGROUND_IMAGE = pygame.image.load("bg placeholder.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

before_time = time.time()

game_scene = Scenes.Game_Scene(WIDTH, HEIGHT, BACKGROUND_IMAGE)
keys = {pygame.K_a: "a", pygame.K_b: "b", pygame.K_c: "c", pygame.K_d: "d", pygame.K_e: "e", pygame.K_f: "f", pygame.K_g: "g",
        pygame.K_h: "h", pygame.K_i: "i", pygame.K_j: "j", pygame.K_k: "k", pygame.K_l: "l", pygame.K_m: "m", pygame.K_n: "n",
        pygame.K_o: "o", pygame.K_p: "p", pygame.K_q: "q", pygame.K_r: "r", pygame.K_s: "s", pygame.K_t: "t", pygame.K_u: "u",
        pygame.K_v: "v", pygame.K_w: "w", pygame.K_x: "x", pygame.K_y: "y", pygame.K_z: "z", pygame.K_SLASH: "/",
        pygame.K_BACKSLASH: "\\", pygame.K_SPACE: " ", pygame.K_SEMICOLON: "; ", pygame.K_KP_MINUS: "-", pygame.K_0: "0",
        pygame.K_1: "1", pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5", pygame.K_6: "6", pygame.K_7: "7",
        pygame.K_8: "8", pygame.K_9: "9", pygame.K_LEFTBRACKET: "[", pygame.K_RIGHTBRACKET: "]"}

keys_shift = {pygame.K_a: "A", pygame.K_b: "B", pygame.K_c: "C", pygame.K_d: "D", pygame.K_e: "E", pygame.K_f: "F",
              pygame.K_g: "G", pygame.K_h: "H", pygame.K_i: "I", pygame.K_j: "J", pygame.K_k: "K", pygame.K_l: "L",
              pygame.K_m: "M", pygame.K_n: "N", pygame.K_o: "O", pygame.K_p: "P", pygame.K_q: "Q", pygame.K_r: "R",
              pygame.K_s: "S", pygame.K_t: "T", pygame.K_u: "U", pygame.K_v: "V", pygame.K_w: "W", pygame.K_x: "X",
              pygame.K_y: "Y", pygame.K_z: "Z", pygame.K_SEMICOLON: ":", pygame.K_UNDERSCORE: "_", pygame.K_SPACE: " ",
              pygame.K_0: ")", pygame.K_1: "!", pygame.K_2: "@", pygame.K_3: "#", pygame.K_4: "$", pygame.K_5: "%", pygame.K_6: "^",
              pygame.K_7: "&", pygame.K_8: "*", pygame.K_9: "("}

import_text_box = Text_Boxes.Text_Box(100, 100, 200, 100, TYPE_FONT, (0, 0, 0), (255, 255, 255))

game_scene.set_text_box(import_text_box)

def game_loop(scene, win, keys, shift_keys):
    Functions.check_user_input(scene, import_text_box, keys, shift_keys)
    Functions.move_everything()
    Functions.resolve_collisions()
    Functions.draw_scene(scene, win)
    Functions.play_sounds()

while game_scene.active:
    after_time = time.time()
    delta_time = after_time - before_time
    before_time = after_time

    game_loop(game_scene, window, keys, keys_shift)

    c.tick(60)
