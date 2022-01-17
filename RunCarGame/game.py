import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH  = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count = 3

def Terminate():
    pygame.quit()
    sys.exit()

def WaitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT():
                Terminate()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    Terminate()
                return
            
def PlayerHasHitBaddie(PlayerRect, Baddies):
    for b in Baddies:
        if PlayerRect.colliderect(b['rect']):
            return True
        return False

def DrawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Configura Pygame, a janela e o cursor do mouse.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Car Race')
pygame.mouse.set_visible(False)

# Fontes
font = pygame.font.SysFont(None, 30)

# Sons
GameOverSound = pygame.mixer.Sound('')
pygame.mixer.music.load('')
laugh = pygame.mixer.Sound('')

# Imagens
PlayerImage = pygame.image.load('')
car3 = pygame.image.load('')
car4 = pygame.image.load('')
PlayerRect = PlayerImage.get_rect()
BaddieImage = pygame.image.load('')
Sample = [car3, car4, BaddieImage]
WallLeft = pygame.image.load('')
WallRight = pygame.image.load('')

