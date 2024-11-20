import pygame as p

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
        self.dog1 = p.image.load('dog1.png') # update to file name
        #DOG 2 left
        self.dog2 = p.image.load('dog2.png') # update to file name
        #set width and height for dog image 1
        self.dog1 = p.transform.scale(self.dog1, (self.width, self.height))
        #set width and hieght for dog image 2
        self.dog2 = p.transform.scale(self.dog2, (self.width, self.height))

        self.image = self.dog1
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = p.key.get_pressed()
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

class Car(p.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        if number == 1:
            self.x = 190 #image size
            self.image = p.image.load('Slow Car.png')#rename once proper image loaded will start with .
            self.vel = -4 #velocity of the car (slow)

        else:
            self.x = 460 #image size
            self.image = p.image.load('Fast Car.png')#rename once proper image loaded will start with .
            self.vel = 5 #velocity of the car (fast)
            #both cars go at different directions

        self.y = HEIGHT / 2
        self.width = 100
        self.height = 150
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

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
class Screen(p.sprite.Sprite):
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
        self.rect.topleft = (self.x, self.y)

WIDTH = 640
HEIGHT = 480

p.init()#initialise all modules within pygame

win = p.display.set_mode((WIDTH, HEIGHT)) #dimensions for background
p.display.set_caption('Crossy Road')
clock = p.time.Clock() # timer

bg = Screen()
screen_group = p.sprite.Group()
screen_group.add(bg)

dog = Dog()
dog_group = p.sprite.Group()
dog_group.add(dog)

slow_car = Car(1)
fast_car = Car(2)
car_group = p.sprite.Group()
car_group.add(slow_car, fast_car)

run = True
while run:
    clock.tick(60)#sets to 60 frames per second
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False # end game if quit is entered

        win.fill((0, 255, 0))#bright green background colour, need to change (based on Red, green, blue (RGB))

        dog_group.draw(win)#show the dogs on the screen similar to turtle
        car_group.draw(win)# show the cars on the screen
        dog_group.update()
        car_group.update()

        p.display.update()#user can see the changes going on

p.quit() #prevents an endless loop

