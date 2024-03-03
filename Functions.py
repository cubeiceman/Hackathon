import pygame
def in_rect(points, rectangle):
    return (rectangle.rect.x < points[0] < rectangle.rect.x + rectangle.rect.width) and (
            rectangle.rect.y < points[1] < rectangle.rect.y + rectangle.rect.height)

def return_words(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        len = 0
        for character in content:
            if character != " ":
                len += 1
        return len

def check_user_input(scene, text_box, keys, shift_keys, bar):
    scene.handle_keyboard(text_box, keys, shift_keys, bar)

def run_ai():
    pass

def move_everything():
    pass

def resolve_collisions():
    pass

def play_sounds():
    pass

def draw_scene(scene, win):
    scene.draw()
    win.blit(scene.surface, (0, 0))
    pygame.display.flip()