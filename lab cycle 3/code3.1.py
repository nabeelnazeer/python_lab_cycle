#importing modules

import pygame
from pygame.locals import *

pygame.init()

#define variables
MARKERS = []

WIDTH = 300
HEIGHT = 300

LINE_WIDTH = 5

COLOR = (255, 255, 200)
GRIDCOLOR = (50, 50, 50)

clicked = False
pos = []

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToe')

def draw():
    WIN.fill(COLOR)
    for x in range(1, 3):
        pygame.draw.line(WIN, GRIDCOLOR, (0, x*100), (WIDTH, x*100), LINE_WIDTH )
        pygame.draw.line(WIN, GRIDCOLOR, (x*100, 0), (x*100, HEIGHT), LINE_WIDTH )

for x in range(3):
    row = [0]*3
    MARKERS.append(row)

print(MARKERS)

#loop for running the game
RUN = True
while RUN:

    draw()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked == True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked == False
            pos = pygame.mouse.get_pos()    
        


    pygame.display.update()        


pygame.quit()        