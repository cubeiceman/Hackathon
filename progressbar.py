import pygame
progress = 0

#this line of code needs to be in main to work
progressbar = pygame.image.load('progressbar0.png') 

max_bar_length = 100
max_words = 100 
current_words = progress
scale = current_words / max_words 

greenbar = pygame.Surface((100, progress))

class Progress_Bar:
    
    #this draws the greenbar
    def draw():
        greenbar.fill((0, 255, 0)) 

    #this reads the wordcount from notes and adds to the progress bar
    def add(wordcount):
        progress += wordcount  


