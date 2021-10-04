from random import randint

import pygame
from pygame.draw import *

pygame.init()

FPS = 30

IMAGE_WIDTH = 1000
IMAGE_HEIGHT = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
SKY_COLOR = (255, 255, 0)
SUN_COLOR = (0, 255, 255)

screen = pygame.display.set_mode((IMAGE_WIDTH, IMAGE_HEIGHT))

surf = pygame.Surface((IMAGE_WIDTH, IMAGE_HEIGHT))
surf.fill(WHITE)


def pictureofbear(x, y, scale, screen):
    '''
    risuet medvedya
    x,y - position
    scale - coefficient uvelicheniya
    screen - poverhnost' dlya risovaniya
    '''
    circle(screen, WHITE, (x + scale * 60, y - scale * 10), 7)#uho
    ellipse(screen, WHITE, [x, y, scale * 100, scale * 200])#telo
    ellipse(screen, WHITE, [x + scale * 60, y - scale * 20, scale * 80, scale * 40])#morda
    ellipse(screen, WHITE, [x + scale * 90, y + scale * 60, scale * 60, scale * 20])#ruka
    ellipse(screen, WHITE, [x + scale * 40, y + scale * 170, scale * 80, scale * 60])#lyazhka
    ellipse(screen, WHITE, [x + scale * 100, y + scale * 200, scale * 100, scale * 40])#stupnya

    circle(screen, BLACK, (x + scale * 90, y - scale * 10), 3) #glaz
    circle(screen, BLACK, (x + scale * 140, y), 3) #nos
    circle(screen, BLACK, (x + scale * 60, y - scale * 10), 7, 2)#uho
    lines(screen, BLACK, False, [[x + scale * 100, y + scale * 10], [x + scale * 120, y + scale * 10]], 5)#rot
    ellipse(screen, BLACK, [x, y, scale * 100, scale * 200], 2)#telo
    ellipse(screen, BLACK, [x + scale * 60, y - scale * 20, scale * 80, scale * 40], 2)#morda
    ellipse(screen, BLACK, [x + scale * 90, y + scale * 60, scale * 60, scale * 20], 2)#ruka
    ellipse(screen, BLACK, [x + scale * 40, y + scale * 170, scale * 80, scale * 60], 2)#lyazhka
    ellipse(screen, BLACK, [x + scale * 100, y + scale * 200, scale * 100, scale * 40], 2)#stupnya
    ellipse(screen, BLACK, [x + scale * 270, y + scale * 160, scale * 120, scale * 60])#wneshluzha
    ellipse(screen, (randint(0, 255), randint(0, 255), randint(0, 255)),
            [x + scale * 280, y + scale * 170, scale * 100,scale * 40])#inluzha
    lines(screen, BLACK, False, [[x + scale * 100, y + scale * 100], [x + scale * 120, y + scale * 100 - scale * 20],
                                 [x + scale * 320, y - scale * 20],
                                 [x + scale * 320, y + scale * 180]], 5)#udochka


def pictureoffish(x, y, scale, screen):
    '''
    risuet ribu
    x,y - position
    scale - coefficient uvelicheniya
    screen - poverhnost' dlya risovaniya
    '''
    ellipse(screen, WHITE, [x, y + scale * 50, scale * 400, scale * 100])#telo
    ellipse(screen, BLACK, [x, y + scale * 50, scale * 400, scale * 100], 2)#telo
    polygon(screen, BLACK,
            [(x, y + scale * 100), (x - scale * 100, y), (x - scale * 100, y + scale * 200),
             (x, y + scale * 100)])#hwost
    circle(screen, BLACK, (x + scale * 300, y + scale * 100), scale * 20)#glaz
    circle(screen, (200, 0, 0), (x + scale * 300, y + scale * 100), scale * 10)#zrachok


rect(surf, SUN_COLOR, (0, 0, 1000, 300))
rect(surf, BLACK, (0, 300, 1000, 10))#granica neba i zemli
circle(surf, SKY_COLOR, (700, 200), 100)
circle(surf, SUN_COLOR, (700, 200), 80)
rect(surf, SKY_COLOR, (600, 200, 200 + 5, 10))
rect(surf, SKY_COLOR, (600 + 100, 200 - 100, 10, 200))

for i in range(1):
    x = randint(0, 1)
    if x == 1:
        xbool = True
    else:
        xbool = False
    surf = pygame.transform.flip(surf, xbool, False)
    pictureofbear(randint(0, 800), randint(200, 800), randint(1, 20) / 20, surf)
    pictureoffish(randint(200, 800), randint(400, 800), randint(1, 20) / 30, surf)
    surf = pygame.transform.flip(surf, xbool, False)

screen.blit(surf, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
