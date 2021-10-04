import pygame
from pygame.draw import *
from random import *
print()
pygame.init()

FPS = 30
BLACK=(0,0,0)
WHITE=(255,255,255)
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255,255,255))

surf=pygame.Surface((1000,1000))
surf.fill((255,255,255))

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def pictureofbear(x,y,k,screen):
    circle(screen, WHITE, (x+k*100-k*10, y-k*10),3)
    circle(screen, WHITE, (x+k*100+k*40, y),3)
    circle(screen, WHITE, (x+k*100-k*40, y-k*10), 7)
    ellipse(screen, WHITE, [x, y, k*100, k*200])
    ellipse(screen, WHITE, [x+k*60, y-k*20, k*80, k*40])
    ellipse(screen, WHITE, [x+k*100-k*10, y+k*60, k*60, k*20])
    ellipse(screen, WHITE, [x+k*100-k*60, y+k*200-k*30, k*80, k*60])
    ellipse(screen, WHITE, [x+k*100, y+k*200, k*100, k*40])

    circle(screen, (0, 0, 0), (x+k*100-k*10, y-k*10), 3)
    circle(screen, (0, 0, 0), (x+k*100+k*40, y), 3)
    circle(screen, (0, 0, 0), (x+k*100-k*40, y-k*10), 7,2)
    lines(screen, BLACK, False, [[x+k*100, y+k*10], [x+k*120, y+k*10]], 5)
    ellipse(screen, (0,0,0), [x, y, k*100, k*200], 2)
    ellipse(screen, (0,0,0), [x+k*60, y-k*20, k*80, k*40], 2)
    ellipse(screen, (0,0,0), [x+k*100-k*10, y+k*60, k*60, k*20], 2)
    ellipse(screen, (0,0,0), [x+k*100-k*60, y+k*200-k*30, k*80, k*60], 2)
    ellipse(screen, (0,0,0), [x+k*100, y+k*200, k*100, k*40], 2)
    ellipse(screen, (0, 0, 0), [x+k*320-k*50, y+k*100-k*20-k*100+k*200-k*20, k*120, k*60])
    ellipse(screen, (randint(0,255), randint(0,255), randint(0,255)), [x+k*320-k*50+k*10, y+k*100-k*20-k*100+k*200-k*20+k*10, k*100, k*40])
    lines(screen, BLACK, False, [[x+k*100, y+k*100], [x+k*120, y+k*100-k*20],[x+k*320, y+k*100-k*20-k*100],[x+k*320, y+k*100-k*20-k*100+k*200]], 5)

def pictureoffish(x,y,k,screen):
    ellipse(screen, WHITE, [x, y+k*50, k*400, k*100])
    ellipse(screen, (0,0,0), [x, y+k*50, k*400, k*100], 2)
    polygon(screen, (0, 0, 0), [(x,y+k*100),(x-k*100,y+k*100-k*100),(x-k*100,y+k*100+k*100),(x,y+k*100)])
    circle(screen, (0, 0, 0), (x+k*300, y+k*100), k*20)
    circle(screen, (200, 0, 0), (x+k*300, y+k*100), k*10)

rect(surf, (0, 255, 255), (0, 0, 1000, 300))
rect(surf, (0, 0, 0), (0, 300, 1000, 10))
circle(surf, (255, 255, 0), (700, 200), 100)
circle(surf, (0, 255, 255), (700, 200), 80)
rect(surf, (255, 255, 0), (600, 200, 200+5, 10))
rect(surf, (255, 255, 0), (600+100, 200-100, 10, 200))


for i in range(1,11,1):
    x=randint(0,1)
    if x==1: xbool=True
    if x==0: xbool=False
    surf=pygame.transform.flip(surf ,xbool,False)
    pictureofbear(randint(0,800),randint(400,800),randint(1,20)/20,surf)
    pictureoffish(randint(200,800),randint(400,800),randint(1,20)/30,surf)
    surf=pygame.transform.flip(surf ,xbool,False)

'''
for i in range(5):
    surf1=pygame.Surface((400,400))
    surf1.fill((255,255,255))
    surf2=pygame.Surface((300,300))
    surf2.fill((255,255,255))
    #pygame.Surface.set_alpha(surf1,100)
    #pygame.Surface.set_alpha(surf2,100)

    x=randint(0,1)
    if x==1: xbool=True
    if x==0: xbool=False

    pictureofbear(100,150,randint(1,20)/20,surf1)
    pictureofbear(100,100,1,surf1)
    #pictureoffish(0,0,randint(1,20)/30,surf2)
    surf1=pygame.transform.flip(surf1 , xbool ,False)
    surf1=rot_center(surf2, angle)
    surf1=pygame.transform.flip(surf2 ,xbool,False)

    surf.blit(surf1, (randint(0,800), randint(400,800)))
    surf.blit(surf1, (400, 200))
    surf.blit(surf2, (randint(200,800), randint(400,800)))
'''



#surf=pygame.transform.rotate(surf,90)
#sur=pygame.Surface(pictureoffish(randint(200,800),randint(400,800),randint(1,20)/30))
#pictureoffish(500,700,1)

screen.blit(surf, (0, 0))

#pygame.transform.flip(screen ,True ,False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
