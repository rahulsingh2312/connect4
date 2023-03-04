import numpy
import pygame
import sys
import math

pygame.init()

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW=(0,255,0)


ROW_COUNT=6
COL_COUNT=7
def matrix():
    board = numpy.zeros((ROW_COUNT,COL_COUNT))
    return board
board=matrix()
BOARDF=numpy.flip(board,0)
def board_f(board):
    # BOARDF=numpy.flip(board,0)
    print(BOARDF)

square= 100
height=((ROW_COUNT+1)*square)
width= (COL_COUNT*square)   
size=(width,height)
radius=50
screen = pygame.display.set_mode(size)
game_over=0
pygame.display.set_caption("Connect Four")
font_name = "monospace"
font_size = 75
myfont = pygame.font.SysFont(font_name, font_size)
# fonts = pygame.font.get_fonts()
# print(fonts)
# text = pygame.font.SysFont("monospace",75)
def drawboard(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*square,(r*square)+square,square,square))
            pygame.draw.circle(screen,BLACK,(int(c*square+square/2), int(r*square+square+square/2)),radius)
            if BOARDF[r][c]==0:
                pygame.draw.circle(screen,BLACK,(int(c*square+square/2), int(r*square+square+square/2)),radius)
            elif BOARDF[r][c]==1:
                pygame.draw.circle(screen,RED,(int(c*square+square/2), int(r*square+square+square/2)),radius)
            else:
                pygame.draw.circle(screen,YELLOW,(int(c*square+square/2), int(r*square+square+square/2)),radius)

    pygame.display.update()

def check_ifempty(board,COL_COUNT):
    return board[ROW_COUNT-1][COL_COUNT]==0

def droppeic(board,row,col,piece):
    board[row,col]=piece

def getnextrow(board,col):
    for r in range(ROW_COUNT):
        if board[r,col]==0:
            return r
        
def winning_move(board,piece):
    #hori
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]== piece and board[r][c+1]== piece and board[r][c+2]== piece and board[r][c+3]== piece:
                return True
    #for verti        
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT):
            if board[r][c]== piece and board[r+1][c]== piece and board[r+2][c]== piece and board[r+3][c]== piece:
                # pygame.time.wait(3000)
                return True
    #slopes
    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT-3):
            if board[r][c]== piece and board[r+1][c+1]== piece and board[r+2][c+2]== piece and board[r+3][c+3]== piece:
                # pygame.time.wait(1000)
                return True    
    for r in range(3,ROW_COUNT):
        for c in range(COL_COUNT-3):
            if board[r][c]== piece and board[r-1][c+1]== piece and board[r-2][c+2]== piece and board[r-3][c+3]== piece:

                return True            

pygame.init()

turn=0

while not game_over:
    drawboard(board)
    # posx = event.pos[0]
    # col = int(input("1*6"))
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,square))
            if turn==0:
                posx = event.pos[0]
                pygame.draw.circle(screen,YELLOW,(posx,int(square/2)),radius)
            else:
                posx = event.pos[0]
                pygame.draw.circle(screen,RED,(posx,int(square/2)),radius)

        if event.type==pygame.MOUSEBUTTONDOWN:
        # print(event.pos)
        # posx = event.pos[0]
        # col = int(math.floor(posx/square))
            if turn==0:
                posx = event.pos[0]
                col = int(math.floor(posx/square))
                if check_ifempty(board,col):
                    row = getnextrow(board,col)
                    droppeic(board,row,col,2)
                board_f(board)
                if winning_move(board,2):
                    print("player 1 wins")
                    label = myfont.render("player 1 wins",1,RED)
                    screen.blit(label,(40,10))
                    pygame.display.update()
                    game_over=1
                turn = 1
                pygame.display.update()
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/square))
                if check_ifempty(board,col):
                    row = getnextrow(board,col)
                    droppeic(board,row,col,1)
                board_f(board)
                if winning_move(board,1):
                    print("player 2 wins")
                    label = myfont.render("player 2 wins",1,YELLOW)
                    screen.blit(label,(40,10))
                    game_over=1
                    pygame.display.update()
                turn = 0
                pygame.display.update()
    if game_over:
        pygame.display.update()
        pygame.time.wait(3000)
