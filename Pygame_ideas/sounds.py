import pygame

def makeSound(filename):
    pygame.mixer.init()
    thissound = pygame.mixer.Sound(filename)

    return thissound

def playSound(sound, loops=0):
    sound.play(loops)

def stopSound(sound):
    sound.stop()

def playSoundAndWait(sound):
    sound.play()
    while pygame.mixer.get_busy():
        # pause
        pause(10)


def makeMusic(filename):
    pygame.mixer.music.load(filename)


def playMusic(loops=0):
    global musicPaused
    if musicPaused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play(loops)
    musicPaused = False

def stopMusic():
    pygame.mixer.music.stop()


def pauseMusic():
    global musicPaused
    pygame.mixer.music.pause()
    musicPaused = True