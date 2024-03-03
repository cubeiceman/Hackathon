import pygame
def in_rect(points, rectangle):
    return (rectangle.rect.x < points[0] < rectangle.rect.x + rectangle.rect.width) and (
            rectangle.rect.y < points[1] < rectangle.rect.y + rectangle.rect.height)

def check_user_input(scene):
    scene.handle_keyboard()

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