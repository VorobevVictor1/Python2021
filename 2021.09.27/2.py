import pygame
from pygame.draw import *
print()
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

screen.fill((100,0,0))
circle(screen, (0, 0, 0), (500, 500), 310)
circle(screen, (255, 255, 0), (500, 500), 300)
circle(screen, (0, 0, 0), (300, 400), 50)
circle(screen, (0, 0, 0), (700, 400), 50)
circle(screen, (139, 0, 0), (300, 400), 20)
circle(screen, (139, 0, 0), (700, 400), 20)
rect(screen, (0, 0, 0), (400, 700, 200, 50))
polygon(screen, (0, 0, 0), [(400, 350), (400, 400),
                               (200, 300), (200, 250),(400,350)])
polygon(screen, (0, 0, 0), [(1000-400, 350), (1000-400, 400),
                               (1000-200, 300), (1000-200, 250),(1000-400,350)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
