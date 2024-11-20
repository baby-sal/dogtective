import pygame as p

class Dog(p.sprite.Sprite)#inheriting dog from sprite module

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

        win.fill((0, 255, 0))#bright green colour
        p.display.update()#user can see the changes going on

p.quit() #prevents an endless loop

