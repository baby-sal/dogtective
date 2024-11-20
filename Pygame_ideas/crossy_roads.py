import pygame as p

WIDTH = 640
HEIGHT = 480

p.init()#initialise all modules within pygame

win = p.display.set_mode((WIDTH, HEIGHT)) #dimensions for background
p.display.set_caption('Crossy Road')
clock = p.time.Clock() # timer

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False # end game if quit is entered

p.quit() #prevents an endless loop

