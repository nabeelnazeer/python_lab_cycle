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
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
clicked = False
pos = []
player = 1
winner = 0
game_over = False

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

def draw_markers():
    x_pos = 0
    for x in MARKERS:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(WIN, GREEN, (x_pos*100 +15, y_pos * 100+15), (x_pos*100+85, y_pos*100+85), LINE_WIDTH )
                pygame.draw.line(WIN, GREEN, (x_pos*100 +15, y_pos * 100+85), (x_pos*100+85, y_pos*100+15), LINE_WIDTH )
            if y == -1:
                pygame.draw.circle(WIN, RED, (x_pos*100+50, y_pos*100+50), 38, LINE_WIDTH)
            y_pos += 1
        x_pos += 1 
def check_winner():
    global winner
    global game_over
    y_pos = 0
    for x in MARKERS:
        if sum(x) == 3:
            winner = 1
            game_over =  True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if MARKERS[0][y_pos] + MARKERS[1][y_pos] + MARKERS[2][y_pos] == 3:
            winner = 1
            game_over =  True
        if MARKERS[0][y_pos] + MARKERS[1][y_pos] + MARKERS[2][y_pos] == -3:
            winner = 2
            game_over =  True
        y_pos += 1 
        if MARKERS[0][0] + MARKERS[1][1] + MARKERS[2][2] == 3 or MARKERS[0][2] + MARKERS[1][1] + MARKERS[2][0] == 3:
            winner = 1
            game_over =  True

        if MARKERS[0][0] + MARKERS[1][1] + MARKERS[2][2] == -3 or MARKERS[0][2] + MARKERS[1][1] + MARKERS[2][0] == -3 :
            winner = 2
            game_over =  True

#define font
font = pygame.font.SysFont(None, 40)

#create play again rectangle

again_rect = Rect(WIDTH//2 - 80, HEIGHT//2+10, 160, 50)

def winner_txt(winner):
    win_txt = "player " + str(winner) + " wins!"
    win_img = font.render(win_txt, True, BLUE)
    pygame.draw.rect(WIN,  GREEN, (WIDTH//2-100, HEIGHT//2-60, 200, 60 ))
    WIN.blit(win_img, (WIDTH//2-100, HEIGHT//2-50))
    again = "play again"
    again_img = font.render(again, True, BLUE)
    pygame.draw.rect(WIN, GREEN, again_rect)
    WIN.blit(again_img, (WIDTH//2-80, HEIGHT//2+10 ))            

#loop for running the game
RUN = True
while RUN:

    draw()
    draw_markers()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100
                if MARKERS[cell_x][cell_y] == 0:
                    MARKERS[cell_x][cell_y] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        winner_txt(winner)
        #check for mouseclick from user to play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    MARKERS = []
                    pos = []
                    player = 1
                    winner = 0
                    game_over = False
                    for x in range(3):
                        row = [0]*3
                        MARKERS.append(row)
                     



    pygame.display.update()        

pygame.quit()        