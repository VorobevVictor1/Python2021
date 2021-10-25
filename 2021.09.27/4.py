from random import randint

import pygame
from pygame.draw import *

pygame.init()

FPS = 30

IMAGE_WIDTH = 1000
IMAGE_HEIGHT = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SUN_COLOR = (255, 255, 0)
SKY_COLOR = (0, 255, 255)

screen = pygame.display.set_mode((IMAGE_WIDTH, IMAGE_HEIGHT))

surf = pygame.Surface((IMAGE_WIDTH, IMAGE_HEIGHT))
surf.fill(WHITE)


def picture_of_bear(x, y, scale=1, screen=surf):
    '''
    Рисует медведя.
    x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
    scale - коэф. увеличения.
    SCREEN - поверхность для рисования pygame.surface
    '''

    def head(x, y, scale, screen):
        '''
        Рисует голову медведя белого цвета с церной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        head_x = x + scale * 60
        head_y = y - scale * 20
        head_width = scale * 80
        head_height = scale * 40
        ellipse(screen, WHITE, [head_x, head_y, head_width, head_height])
        ellipse(screen, BLACK, [head_x, head_y, head_width, head_height], 2)


    def bear_eye(x, y, scale, screen):
        '''
        Рисует глаз медведя на голове.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        bear_eye_x = x + scale * 90
        bear_eye_y = y - scale * 10
        bear_eye_radius = int(scale * 3)
        circle(screen, BLACK, (bear_eye_x, bear_eye_y), bear_eye_radius)

    def nose(x, y, scale, screen):
        '''
        Рисует нос медведя на голове.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        nose_x = x + scale * 140
        nose_y = y
        nose_radius = int(scale * 3)
        circle(screen, BLACK, (nose_x, nose_y), nose_radius)

    def ear(x, y, scale, screen):
        '''
        Рисует белое ухо с черной обводкой на голове медведя.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        ear_x = x + scale * 60
        ear_y = y - scale * 10
        ear_radius = int(scale * 7)
        circle(screen, WHITE, (ear_x, ear_y), ear_radius)
        circle(screen, BLACK, (ear_x, ear_y), ear_radius, 2)

    def mouth(x, y, scale, screen):
        '''
        Рисует рот медведя на голове.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        mouth_x = x + scale * 100
        mouth_y = y + scale * 10
        mouth_thickness = int(scale * 5)
        lines(screen, BLACK, False, [[mouth_x, mouth_y], [mouth_x + scale * 20, mouth_y]], mouth_thickness)

    def bear_body(x, y, scale, screen):
        '''
        Рисует белое тело медведя с черной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        bear_body_width = scale * 100
        bear_body_height = scale * 200
        ellipse(screen, WHITE, [x, y, bear_body_width, bear_body_height])
        ellipse(screen, BLACK, [x, y, bear_body_width, bear_body_height], 2)

    def arm(x, y, scale, screen):
        '''
        Рисует белую руку медведя с черной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        arm_x = x + scale * 90
        arm_y = y + scale * 60
        arm_width = scale * 60
        arm_height = scale * 20
        ellipse(screen, WHITE, [arm_x, arm_y, arm_width, arm_height])
        ellipse(screen, BLACK, [arm_x, arm_y, arm_width, arm_height], 2)

    def hip(x, y, scale, screen):
        '''
        Рисует белое бедро медведя с черной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        hip_x = x + scale * 40
        hip_y = y + scale * 170
        hip_width = scale * 80
        hip_height = scale * 60
        ellipse(screen, WHITE, [hip_x, hip_y, hip_width, hip_height])
        ellipse(screen, BLACK, [hip_x, hip_y, hip_width, hip_height], 2)

    def foot(x, y, scale, screen):
        '''
        Рисует белую ступню медведя с черной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        foot_x = x + scale * 100
        foot_y = y + scale * 200
        foot_width = scale * 100
        foot_height = scale * 40
        ellipse(screen, WHITE, [foot_x, foot_y, foot_width, foot_height])
        ellipse(screen, BLACK, [foot_x, foot_y, foot_width, foot_height], 2)

    def fish_rod(x, y, scale, screen):
        '''
        Рисует удочку медведя.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        fish_rod_x = x + scale * 100
        fish_rod_y = y + scale * 100
        fish_rod_thickness = int(scale * 5) + 1
        lines(screen, BLACK, False, [[fish_rod_x, fish_rod_y], [fish_rod_x + scale * 20, fish_rod_y - scale * 20],
                                     [fish_rod_x + scale * 220, fish_rod_y - scale * 120],
                                     [fish_rod_x + scale * 220, fish_rod_y + scale * 80]], fish_rod_thickness)

    def hole(x, y, scale, screen):
        '''
        Рисует прорубь с водой случайного цвета.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела медведя.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        hole_x = x + scale * 280
        hole_y = y + scale * 170
        hole_width = scale * 100
        hole_height = scale * 40
        ellipse(screen, (randint(0, 255), randint(0, 255), randint(0, 255)),
            [hole_x, hole_y, hole_width, hole_height])
        ellipse(screen, BLACK, [hole_x - scale * 10, hole_y - scale * 10, hole_width + scale * 20,
                                hole_height + scale * 20], int(scale * 12))

    head(x, y, scale, screen)
    bear_eye(x, y, scale, screen)
    nose(x, y, scale, screen)
    ear(x, y, scale, screen)
    mouth(x, y, scale, screen)
    bear_body(x, y, scale, screen)
    arm(x, y, scale, screen)
    hip(x, y, scale, screen)
    foot(x, y, scale, screen)
    fish_rod(x, y, scale, screen)
    hole(x, y, scale, screen)


def picture_of_fish(x, y, scale=1, screen=surf):
    '''
    Рисует рыбу.
    x,y - точка прикрепления хвоста к телу.
    scale - коэф. увеличения.
    SCREEN - поверхность для рисования pygame.surface.
    '''

    def fish_body(x, y, scale, screen):
        '''
        Рисует белое тело рыбы с черной обводкой.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела рыбы.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        fish_body_width = scale * 400
        fish_body_height = scale * 100
        ellipse(screen, WHITE, [x, y, fish_body_width, fish_body_height])
        ellipse(screen, BLACK, [x, y, fish_body_width, fish_body_height], 2)

    def tale(x, y, scale, screen):
        '''
        Рисует черный хвост рыбы.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела рыбы.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        tale_x = x
        tale_y = y + scale * 50
        polygon(screen, BLACK,
                [(tale_x, tale_y), (tale_x - scale * 100, tale_y - scale * 100),
                 (tale_x - scale * 100, tale_y + scale * 100), (tale_x, tale_y)])

    def fish_eye(x, y, scale, screen):
        '''
        Рисует черный глаз рыбы с красным зрачком.
        x,y - координаты точки, с которой начинает рисоваться эллипс тела рыбы.
        scale - коэф. увеличения.
        SCREEN - поверхность для рисования pygame.surface.
        '''
        fish_eye_x = x + scale * 300
        fish_eye_y = y + scale * 50
        fish_eye_radius = int(scale * 20)
        circle(screen, BLACK, (fish_eye_x, fish_eye_y), fish_eye_radius)
        circle(screen, RED, (fish_eye_x, fish_eye_y), int(fish_eye_radius / 2))

    fish_body(x, y, scale, screen)
    tale(x, y, scale, screen)
    fish_eye(x, y, scale, screen)

def background(x, y, screen=surf):
    '''
    Функция рисует фон картинки.
    x, y - координаты центра солнца.
    SCREEN- поверхность для рисования pygame.surface.
    '''
    def sky(screen):
        '''
        Функция рисует небо и горизонт.
        x, y - координаты центра солнца.
        SCREEN- поверхность для рисования pygame.surface.
        '''
        sky_x = 0
        sky_y = 0
        sky_width = IMAGE_WIDTH
        sky_height = 300
        rect(surf, SKY_COLOR, (sky_x, sky_y, sky_width, sky_height))
        rect(surf, BLACK, (sky_x, sky_y + 300, sky_width, int(sky_height / 30)))

    def sun(x, y, screen):
        '''
        Функция рисует солнце на небе, состоящее из окружности и горизонтальной и вертикальной полос.
        x, y - координаты центра солнца.
        SCREEN- поверхность для рисования pygame.surface.
        '''
        sun_radius = 100
        sun_thickness = 20
        circle(surf, SUN_COLOR, (x, y), sun_radius, sun_thickness)
        rect(surf, SUN_COLOR, (x - 100, y, sun_radius * 2, int(sun_thickness / 2)))
        rect(surf, SUN_COLOR, (x, y - 100, int(sun_thickness / 2), sun_radius * 2))

    sky(screen)
    sun(x, y, screen)

background(700, 200)


for i in range(10):
    x = randint(0, 1)
    if x == 1:
        xbool = True
    else:
        xbool = False
    surf = pygame.transform.flip(surf, xbool, False)
    picture_of_bear(randint(0, 800), randint(200, 800), randint(1, 20) / 20, surf)
    picture_of_fish(randint(200, 800), randint(400, 800), randint(1, 20) / 30, surf)
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