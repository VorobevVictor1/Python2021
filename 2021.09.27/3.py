import pygame
from pygame.draw import *
print()
pygame.init()

FPS = 30
BLACK=(0,0,0)
WHITE=(255,255,255)
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255,255,255))

def pictureofbear(x,y,k):
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
    ellipse(screen, (0, 128, 0), [x+k*320-k*50+k*10, y+k*100-k*20-k*100+k*200-k*20+k*10, k*100, k*40])
    lines(screen, BLACK, False, [[x+k*100, y+k*100], [x+k*120, y+k*100-k*20],[x+k*320, y+k*100-k*20-k*100],[x+k*320, y+k*100-k*20-k*100+k*200]], 5)

def pictureoffish(x,y,k):
    ellipse(screen, WHITE, [x, y+k*50, k*400, k*100])
    ellipse(screen, (0,0,0), [x, y+k*50, k*400, k*100], 2)
    polygon(screen, (0, 0, 0), [(x,y+k*100),(x-k*100,y+k*100-k*100),(x-k*100,y+k*100+k*100),(x,y+k*100)])
    circle(screen, (0, 0, 0), (x+k*300, y+k*100), 20)
    circle(screen, (200, 0, 0), (x+k*300, y+k*100), 10)
    x+=200
    y-=40
    k=k*0.5
    polygon(screen, (0, 0, 0), [(x,y+k*100),(x-k*100,y+k*100-k*100),(x-k*100,y+k*100+k*100),(x,y+k*100)])

rect(screen, (0, 255, 255), (0, 0, 1000, 500))
rect(screen, (0, 0, 0), (0, 500, 1000, 10))
circle(screen, (255, 255, 0), (700, 200), 100)
circle(screen, (0, 255, 255), (700, 200), 80)
rect(screen, (255, 255, 0), (600, 200, 200+5, 10))
rect(screen, (255, 255, 0), (600+100, 200-100, 10, 200))
pictureofbear(150,300,1.43432)
pictureoffish(500,700,1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
