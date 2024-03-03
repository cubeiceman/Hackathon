from xml.dom.pulldom import parseString
import pygame
from pygame.locals import *
from Buttons import Button
from gacha import gacha
from weapon import Weapon


# ----- VARIABLES ----- #

total_words = 0
num_tokens = 1
scene_name = "home"
owned_weapons = []
equipped_weapons = []

background_dir = "images/background/"
buttons_dir = "images/buttons/"
weapons_dir = "images/weapons/"
other_dir = "images/other/"

# items dictionary with Weapon a_weapon : integer probability
items = {
    Weapon("Weapon 1", 10, weapons_dir+"random.png"):1,
    Weapon("Weapon 2", 20, weapons_dir+"random.png"):3,
}

pygame.font.init()
default_font = pygame.font.Font("MadimiOne-Regular.ttf", 50)
big_font = pygame.font.Font("MadimiOne-Regular.ttf", 200)
med_font = pygame.font.Font("MadimiOne-Regular.ttf", 100)

equipped_text = default_font.render("EQUIPPED WEAPONS", True, (250, 250, 250))
owned_text = default_font.render("OWNED WEAPONS", True, (250, 250, 250))

title_the = med_font.render("The", True, (0, 0, 0))
title_big = big_font.render("BIG", True, (59, 144, 209))
title_penguin = med_font.render("PENGUIN", True, (200, 200, 255))

# ----- PYGAME ----- #
pygame.init()

WIDTH, HEIGHT = (1600, 900)
HEIGHT -= 80
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("The Big Penguin")
c = pygame.time.Clock()
WHITE = (255, 255, 255)
GREY = (75, 75, 75)

home_bg = pygame.image.load(background_dir+"bg placeholder.png")
home_bg = pygame.transform.scale(home_bg, (WIDTH, HEIGHT))

fight_bg = pygame.image.load(background_dir+"bg placeholder.png")
fight_bg = pygame.transform.scale(fight_bg, (WIDTH, HEIGHT))

inventory_bg = pygame.image.load(background_dir+"bg placeholder.png")
inventory_bg = pygame.transform.scale(inventory_bg, (WIDTH, HEIGHT))

notes_bg = pygame.image.load(background_dir+"bg placeholder.png")
notes_bg = pygame.transform.scale(notes_bg, (WIDTH, HEIGHT))

gacha_bg = pygame.image.load(background_dir+"bg placeholder.png")
gacha_bg = pygame.transform.scale(gacha_bg, (WIDTH, HEIGHT))

chest_img = pygame.image.load(other_dir+"chest.png")
chest_img = pygame.transform.scale(chest_img, (400, 500))

fight_button = Button(100, 700, 100, 50, buttons_dir+"random.png")
inventory_button = Button(300, 700, 100, 50, buttons_dir+"random.png")
notes_button = Button(500, 700, 100, 50, buttons_dir+"random.png")
gacha_button = Button(700, 700, 100, 50, buttons_dir+"random.png")
home_button = Button(20, 20, 50, 50, buttons_dir+"random.png")

penguin_img = pygame.image.load(other_dir+"penguin.png").convert_alpha()
penguin_img = pygame.transform.scale(penguin_img, (500, 500))

run = True
frame_num = 0

while run:
    clicked = False
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    
    match scene_name:
        case "home":
            window.blit(home_bg, (0, 0))

            # draw title
            pygame.draw.rect(window, (255, 255, 255), (100, 150, 650, 450), border_radius=20)
            window.blit(title_the, (200, 200))
            window.blit(title_big, (225, 225))
            window.blit(title_penguin, (270, 400))

            window.blit(penguin_img, penguin_img.get_rect(center=(1200,HEIGHT//2)))
            # display progress bar

            gacha_button.draw(window)
            if gacha_button.check_click(mouse_pos, clicked):
                scene_name = "gacha"
                frame_num = 0

            fight_button.draw(window)
            if fight_button.check_click(mouse_pos, clicked):
                scene_name = "fight"
                frame_num = 0
            
            notes_button.draw(window)
            if notes_button.check_click(mouse_pos, clicked):
                scene_name = "notes"
                frame_num = 0
            
            inventory_button.draw(window)
            if inventory_button.check_click(mouse_pos, clicked):
                scene_name = "inventory"
                frame_num = 0

        case "fight":
            window.blit(fight_bg, (0, 0))
            # compare fighting powers
            # if winnable -> win animation
            # if lose -> lose animation
            home_button.draw(window)
            if home_button.check_click(mouse_pos, clicked):
                scene_name = "home"
                frame_num = 0

        
        case "inventory":
            if frame_num == 1:
                if len(owned_weapons) <= 5:
                    equipped_weapons = owned_weapons.copy()
                
                print(owned_weapons)
                print(equipped_weapons)

            # equip weapons
            #window.blit(inventory_bg, (0, 0))
            window.fill((209, 117, 100))

            window.blit(equipped_text, equipped_text.get_rect(center=(WIDTH//2, 100)))
            window.blit(owned_text, owned_text.get_rect(center=(WIDTH//2, 475)))

            # equipped item display
            for i in range(5):
                location_x = 75 + 300*i + 125
                location_y = 275
                pygame.draw.rect(window, (128, 128, 128), (location_x-125, location_y-125, 250, 250))
                if i<len(equipped_weapons):
                    equipped_weapons[i].inventory_disp(window, (location_x, location_y))

            # owned item display
            for i in range(10):
                location_x = 75 + 300 * i + 125
                location_y = 650
                pygame.draw.rect(window, (128, 128, 128), (location_x-125, location_y-125, 250, 250))
            pygame.draw.rect(window, (209, 117, 100), (0, 525, 75, 375))
            pygame.draw.rect(window, (209, 117, 100), (1525, 525, 75, 375))
            
            home_button.draw(window)
            if home_button.check_click(mouse_pos, clicked):
                scene_name = "home"
                frame_num = 0

        case "notes":
            # take notes, get points
            window.blit(notes_bg, (0, 0))

            home_button.draw(window)
            if home_button.check_click(mouse_pos, clicked):
                scene_name = "home"
                frame_num = 0

        case "gacha":
            if frame_num == 1:
                if num_tokens > 0:
                    can_roll = True
                else:
                    can_roll = False
                display_item = False
                rolled_item = None
                display_frame = 0
            
            window.blit(gacha_bg, (0, 0))

            if can_roll:
                window.blit(chest_img, chest_img.get_rect(center = (WIDTH//2, HEIGHT//2)))

                if clicked and chest_img.get_rect(center = (WIDTH//2, HEIGHT//2)).collidepoint(*mouse_pos):
                    rolled_item = gacha(items)
                    if rolled_item not in owned_weapons:
                        owned_weapons.append(rolled_item)
                    num_tokens -= 1
                    display_item = True

                    if num_tokens > 0:
                        can_roll = True
                    else:
                        can_roll = False

            else:
                pass
                
            if display_item and rolled_item is not None:
                rolled_item.draw(window, (WIDTH//2, HEIGHT//2))
                display_frame += 1
                if display_frame == 100:
                    display_item = False
            
            home_button.draw(window)
            if home_button.check_click(mouse_pos, clicked):
                scene_name = "home"
                frame_num = 0

    frame_num+=1
    pygame.display.flip()

    c.tick(60)

