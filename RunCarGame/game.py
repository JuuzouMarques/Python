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
            if event.type == QUIT:
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


# Configura Pygame, a janela e o cursor do mouse
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Car Race')
pygame.mouse.set_visible(False)

# Fontes
font = pygame.font.SysFont(None, 30)

# Sons
GameOverSound = pygame.mixer.Sound('RunCarGame\music\crash.wav')
pygame.mixer.music.load('RunCarGame\music\car.wav')
laugh = pygame.mixer.Sound('RunCarGame\music\laugh.wav')

# Imagens
PlayerImage = pygame.image.load('RunCarGame\image\car1.png')
car3 = pygame.image.load('RunCarGame\image\car3.jpg')
car4 = pygame.image.load('RunCarGame\image\car4.png')
PlayerRect = PlayerImage.get_rect()
BaddieImage = pygame.image.load('RunCarGame\image\car2.png')
Sample = [car3, car4, BaddieImage]
WallLeft = pygame.image.load('RunCarGame\image\left.png')
WallRight = pygame.image.load('RunCarGame\image\direita.png')

# "Inicia" a tela
DrawText('Pressione qualquer tecla para iniciar o jogo', font, windowSurface, (WINDOWWIDTH/3) - 30, (WINDOWHEIGHT/3))
DrawText('Aproveite!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
WaitForPlayerToPressKey()
zero = 0
if not os.path.exists('RunCarGame\data\save.dat'):
    f = open('RunCarGame\data\save.dat', 'w')
    f.write(str(zero))
    f.close()
v = open('RunCarGame\data\save.dat', 'r')
TopScore = int(v.readline())
v.close()

while (count>0):
    # Inicia o Jogo
    baddies = []
    score = 0
    PlayerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    MoveLeft = MoveRight = MoveUp = MoveDown = False
    ReverseCheat = SlowCheat = False
    BaddieAddCount = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:
        score += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                Terminate()
            
            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    ReverseCheat = True
                if event.key == ord('x'):
                    SlowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    MoveRight, MoveLeft = False, True
                if event.key == K_RIGHT or event.key == ord('d'):
                    MoveRight, MoveLeft = True, False
                if event.key == K_UP or event.key == ord('w'):
                    MoveUp, MoveDown = True, False
                if event.key == K_DOWN or event.key == ord('s'):
                    MoveUp, MoveDown = False, True
            
            if event.type == KEYUP:
                if event.key == ord('z'):
                    ReverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    SlowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    Terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    MoveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    MoveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    MoveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    MoveDown = False
                
        # Adiciona novos baddies no topo da tela
        if not ReverseCheat and not SlowCheat:
            BaddieAddCount += 1
        if BaddieAddCount == ADDNEWBADDIERATE:
            BaddieAddCount = 0
            BaddieSize = 30
            NewBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - BaddieSize, 23 , 47),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(random.choice(Sample), (23, 47)),
                        }
            baddies.append(NewBaddie)
            sideLeft= {'rect': pygame.Rect(0,0,126,600),
                       'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(WallLeft, (126, 599)),
                       }
            baddies.append(sideLeft)
            sideRight= {'rect': pygame.Rect(497,0,303,600),
                       'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(WallRight, (303, 599)),
                       }
            baddies.append(sideRight)
        
        # Move o jogador
        if MoveLeft and PlayerRect.left > 0:
            PlayerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if MoveRight and PlayerRect.right < WINDOWWIDTH:
            PlayerRect.move_ip(PLAYERMOVERATE, 0)
        if MoveUp and PlayerRect.top > 0:
            PlayerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if MoveDown and PlayerRect.bottom < WINDOWHEIGHT:
            PlayerRect.move_ip(0, PLAYERMOVERATE)
        
        for b in baddies:
            if not ReverseCheat and not SlowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif ReverseCheat:
                b['rect'].move_ip(0, -5)
            elif SlowCheat:
                b['rect'].move_ip(0, 1)
        
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
        
        # Desenha o mundo na janela
        windowSurface.fill(BACKGROUNDCOLOR)

        # Desenha a pontuação e o Record.
        DrawText('Pontuação: %s' % (score), font, windowSurface, 128, 0)
        DrawText('Top Score: %s' % (TopScore), font, windowSurface,128, 20)
        DrawText('Rest Life: %s' % (count), font, windowSurface,128, 40)

        windowSurface.blit(PlayerImage, PlayerRect)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
        
        pygame.display.update()

        # Verifica se algum carro o atingiu
        if PlayerHasHitBaddie(PlayerRect, baddies):
            if score > TopScore:
                g = open('RunCarGame\data\save.dat', 'w')
                g.write(str(score))
                g.close()
                TopScore = score
            break

        mainClock.tick(FPS)

    # Tela de Game Over.
    pygame.mixer.music.stop()
    count = count-1
    GameOverSound.play()
    time.sleep(1)
    if (count == 0):
        laugh.play()
        DrawText('Game Over', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        DrawText('Pressione qualquer tecla para jogar novamente.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        WaitForPlayerToPressKey()
        count = 3
        GameOverSound.stop()