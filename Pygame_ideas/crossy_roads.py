import pygame as p#saves typing pygame all the time
import time#used to make dog move slower

class Dog(p.sprite.Sprite):#inheriting dog from sprite module
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.width = 100
        self.height = 50

        #IMAGES NEED TO UPDATE
        #DOG 1 right
        self.dog1 = p.image.load('../logic/assets/images/characters/dogtective_sprite/Idle.png').convert_alpha()
        """#DOG 2 left
        self.dog2 = p.image.load('dog2.png') # update to file name
        #Dog idle right
        self.dog3 = p.image.load('../logic/assets/images/characters/dogtective_sprite/Walk.png')
        #Dog idle left - need to update
        self.dog4 = p.image.load('dog4.png')"""
        #set width and height for dog image 1
        self.dog1 = p.transform.scale(self.dog1, (self.width, self.height))
        #set width and height for dog image 2
        self.dog2 = p.transform.flip(self.dog1, True, False)#flips dog image 1 to face the other direction
        #set width and height for dog image 3
        """self.dog3 = p.transform.scale(self.dog3, (self.width, self.height))
        #set width and height for dog image 3
        self.dog4 = p.transform.scale(self.dog4, (self.width, self.height))"""
        
        self.image = self.dog1
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.correction()
        self.checkCollision()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()
        """ if not any(keys):#if no keys are pressed
            if 'right' == 'right':
                self.image = self.dog3
            else:
                self.image = self.dog4
                #shows different idle images based on the last key pressed"""

        if keys[p.K_LEFT]:
            self.x -= self.vel
            #left key pressed negative velocity
            self.image = self.dog2 #switch to dog image 2


        elif keys[p.K_RIGHT]:
            self.x += self.vel
            #right key pressed positive velocity
            self.image = self.dog1 #switch to dog image 1

        if keys[p.K_UP]:
            self.y -= self.vel
            # left key up negative velocity

        elif keys[p.K_DOWN]:
            self.y += self.vel
            # right key down positive velocity

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2 #prevents dog from going off of the screen on the right side of the screen

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2 #prevents dog from going off of the screen on the left side of the screen

        if self.y - self.width / 2 < 0:
            self.y = self.width / 2 #prevents dog from going off of the screen on the top of the screen

        elif self.y + self.width / 2 > WIDTH:
            self.y = WIDTH - self.width / 2 #prevents dog from going off of the screen on the bottom of the screen

    def checkCollision(self):
        car_check = p.sprite.spritecollide(self, car_group, False, p.sprite.collide_mask)
        if car_check:
            explosion.explode(self.x, self.y)
class Car(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.x = 190 #initial x position
            self.image = p.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
            """self.image = p.transform.rotate(self.image, 90)#rotates the car 90 degrees"""
            self.vel = -4 #velocity of the car (slow)

        else:
            self.x = 460 #where it is on the x axis
            self.image = p.image.load('../logic/assets/images/obstacles/car.png').convert_alpha()
            """self.image = p.transform.rotate(self.image, -90)#rotates the car -90 degrees"""
            self.vel = 5 #velocity of the car (fast)
            #both cars go at different directions

        self.y = 300
        self.width = 100#image width
        self.height = 150#image height
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        self.y += self.vel

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1

        elif self.y + self.height /2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1
            #prevents cars from going off the edge of the background image
"""class Screen(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = p.image.load('Scene.png')#Update with scenery images
        self.img2 = p.image.load('You Win.png')#shows when a player has won, update png once image has been confirmed
        self.img3 = p.image.load('You lose.png')# shows when a player has lost, update png once image has been confirmed

        self.img1 = p.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = p.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = p.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)"""
class Flag(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.number = number

        if self.number == 1:
            self.image = p.image.load('../Pygame_ideas/src/Bone.png').convert_alpha()#update name once image loaded
            self.visible = True #shows as visible
            self.x = 50
            self.width = 100
            self.height = 100

        else:
            self.image = p.image.load('../Pygame_ideas/src/Bone.png').convert_alpha()#update name once image loaded
            self.visible = True
            self.x = 580#opposite end of the screen
            self.width = 100
            self.height = 100

        self.y = 200
        self.image = p.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def update(self):
        if self.visible:
            self.collision()
            self.rect.center = (self.x, self.y)

    def collision(self):
        global SCORE, dog

        flag_hit = p.sprite.spritecollide(self, dog_group, False, p.sprite.collide_mask)

        if flag_hit:
            self.visible = False

            if self.number == 1:
                white_flag.visible = True
                if SCORE < 5:
                    SwitchLevel()
                else:
                    dog_group.empty()
                    DeleteOtherItems()
                    EndScreen(1)

            else:
                green_flag.visible = True
class Explosion(object):
    def __init__(self):
        self.costume = 1
        self.width = 100
        self.height = 50
        #hurt dog right facing
        self.dog_hurt_right = p.image.load('../logic/assets/images/characters/dogtective_sprite/Hurt.png').convert_alpha()
        self.dog_hurt_right = p.transform.scale(self.dog_hurt_right, (self.width, self.height))#updates the size of the image
        #hurt dog left facing
        self.dog_hurt_left = p.transform.flip(self.dog_hurt_right, True, False)#flip dog to face left.
        
        self.image = self.dog_hurt_right
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)

    def explode(self, x, y, last_direction):
        x = x - self.width / 2
        y = y - self.height / 2
        
        #check the last direction
        if last_direction == 'left':
            self.image = self.dog_hurt_left
        else:
            self.image = self.dog_hurt_right
        
        DeleteDog()

        while self.costume < 9:
            if last_direction == 'left':
                self.image = self.dog_hurt_left
            else:
                self.image = self.dog_hurt_right
                
            win.blit(self.image, (x, y))
            p.display.update()

            self.costume += 1
            time.sleep(0.1)#slows down the frame time

        DeleteOtherItems()
        EndScreen(0)
class Road(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.x = 190 #image size
            
        else:
            self.x = 460 #where it is on the x axis

        self.image = p.image.load('Pygame_ideas\src\Road.png').convert_alpha()
        self.width = 90#image width
        self.height = 200#image height
        self.image = p.transform.scale(self.image, (self.width, self.height))
        
        self.y = 0
        self.rect = self.image.get_rect(topleft=(self.width, self.height))
        self.mask = p.mask.from_surface(self.image)
        
        def update(self):
            pass
def scoreDisplay():
    global gameOn
    

    if gameOn:
        score_text = score_font.render(f"Score: {SCORE}", True, (0, 0, 0))#set font to black, and show the level out of 5
    win.blit(score_text, (255, 10))#x and y position of score text
def checkFlags():
    for flag in flags:
        if not flag.visible:
            flag.kill()#if flag isn't visible kill the sprite
        else:
            if not flag.alive():
                flag_group.add(flag)
def SwitchLevel():
    global SCORE

    if slow_car.vel < 0:
        slow_car.vel -= 1

    else:
        slow_car.vel += 1

    if fast_car.vel < 0:
        fast_car.vel -= 1

    else:
        fast_car.vel += 1

    SCORE += 1
def DeleteDog():
    global dog

    dog.kill()
    """screen_group.draw(win)"""
    car_group.draw(win)
    flag_group.draw(win)

    """screen_group.update()"""
    car_group.update()
    flag_group.update()

    p.display.update()
def DeleteOtherItems():
    car_group.empty()
    
    flag_group.empty()
    flags.clear()
def EndScreen(n):
    global gameOn

    gameOn = False
    """if n == 0:
        bg.image = bg.img3 #you loose background image, need to update based on images saved

    elif n == 1:
        bg.image = bg.img2 #you win background image, need to update based on images saved
def Health():
    pass#need to update later on once images loaded and at adding health stage"""

WIDTH = 640
HEIGHT = 480

p.init()#initialise all modules within pygame

win = p.display.set_mode((WIDTH, HEIGHT)) #dimensions for background
p.display.set_caption('Crossy Road')
clock = p.time.Clock() # timer

SCORE = 0
score_font = p.font.SysFont('comicsans', 80, True)#set font to comic sans, size 80px, bold
"""HEALTH = 5
health.font = p.font.SysFont('comicsans', 80, True)"""#this one needs work to be similar to score but be image based instead,
# this is a bit more complex, may need help

"""bg = Screen()
screen_group = p.sprite.Group()
screen_group.add(bg)"""
road1 = Road(1)
road2 = Road(2)
road_group = p.sprite.Group(road1, road2)
road_group.add(road1, road2)

dog = Dog()
dog_group = p.sprite.Group()
dog_group.add(dog)

slow_car = Car(1)
fast_car = Car(2)
car_group = p.sprite.Group()
car_group.add(slow_car, fast_car)

green_flag = Flag(1)
white_flag = Flag(2)
flag_group = p.sprite.Group()
flag_group.add(green_flag, white_flag)
flags = [green_flag, white_flag]

explosion = Explosion()

gameOn = True

run = True
while run:
    clock = p.time.Clock()#makes the game less laggy
    clock.tick(60)#sets to 60 frames per second
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False # end game if quit is entered
        win.fill((0, 255, 0))#sets the background colour to show bright green"""
        """screen_group.draw(win)# draw the background based on images"""
        

        scoreDisplay()
        checkFlags()
        
        road_group.draw(win)

        car_group.draw(win)# show the cars on the screen
        dog_group.draw(win)  # show the dogs on the screen similar to turtle
        flag_group.draw(win)
        
        road_group.update()

        car_group.update()
        dog_group.update()
        flag_group.update()

        """screen_group.update()"""

        p.display.update()#user can see the changes going on

p.quit() #prevents an endless loop

