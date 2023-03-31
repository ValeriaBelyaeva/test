import pygame
import random, time, sys
from pygame.locals import *

pygame.init()
from settings import *

screen = pygame.display.set_mode((window_w, window_h))
# pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption('Тетрис')
desk = [[4 for i in range(8)] for i in range(11)]

flRunning = True
pause=0
FPS = 1        # число кадров в секунду
clock = pygame.time.Clock()


while flRunning:
    if briсk_type == -1:
        briсk_type = random.randint(0, 6)
        briсk_cl = 2
        briсk_st = 0 # random.randint(0, 6)


    for j in range(11):
        for i in range(8):
            color = colors[desk[j][i]]
            if chek_ij_in_bkick(i, j):
                color = 1
            pygame.draw.rect(screen,color,(50+i*int(side*1.2),150+j*int(side*1.2),side,side))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

        if event.type == KEYUP:
            if event.key == K_SPACE:
                if pause==0:
                    pause = 1

                    screen.fill(colors[0])
                #else: pause.fill(())


    clock.tick(FPS)
    print(clock)