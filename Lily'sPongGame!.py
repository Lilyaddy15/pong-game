#Lily's Pong Game!
#July 19, 2017
#Planet Bravo Techno-Tainment Camp

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()


#Create Variables

player_paddle_x = 30
player_paddle_y = 215

ai_1_paddle_x = 970
ai_1_paddle_y = 215

pong_ball_x = 60
pong_ball_y = 215

ball_x_velocity = 1
ball_y_velocity = 1

ai_speed = 0.28

movePaddle = 0
speed = 0.3

playerScore = 0
aiScore = 0

gameover = True
font = pygame.font.SysFont("calibri",40)

#Create Game Window

screen = pygame.display.set_mode((1000, 480),0,0)
pygame.display.set_caption("Lily's Pong Game!")

#Create Background
while gameover:
    
    pong_ball_x = pong_ball_x + ball_x_velocity
    pong_ball_y = pong_ball_y + ball_y_velocity
    
    bg = pygame.Surface((1000, 480))
    background = bg.convert()
    background.fill ((157, 116, 247))

    score1 = font.render(str(playerScore), True, (252,213,70))
    score2 = font.render(str(aiScore), True, (252,213,70))
    screen.blit(score1, (250,210))
    screen.blit(score2, (380,210))

    #Create Paddles and Ball

    player_paddle = pygame.Surface((10,90))
    player_1_paddle = player_paddle.convert()
    player_1_paddle.fill ((0,0,0))

    ai_paddle = player_paddle.convert()

    pong_ball = pygame.Surface((30,30))
    pong_ball_1 = pong_ball.convert()
    pygame.draw.circle(pong_ball_1, (1,1,1), (15,15), 15) 
    pong_ball_1.set_colorkey ((0,0,0))

    #Ball bouncing off paddles
    if pong_ball_x <= player_paddle_x + 10:
        if pong_ball_y >= player_paddle_y - 7.5 and pong_ball_y <= player_paddle_y + 50:
            ball_x = 10
            ball_x_velocity = -ball_x_velocity

    if pong_ball_x >= ai_1_paddle_x - 15:
        if pong_ball_y >= ai_1_paddle_y - 7.5 and pong_ball_y <= ai_1_paddle_y + 50:
            ball_x = 595
            ball_x_velocity = -ball_x_velocity

    #Ball bouncing off ceiling and floor
    if pong_ball_y <= 10:
        ball_y_velocity = -ball_y_velocity
        ball_y = 20
    elif pong_ball_y >= 458:
        ball_y_velocity = -ball_y_velocity
        pong_ball_y = 458

    #AI Paddle Movement
    if ai_1_paddle_y < pong_ball_y +7.5:
        ai_1_paddle_y = ai_1_paddle_y + ai_speed
    if ai_1_paddle_y > pong_ball_y -42.5:
        ai_1_paddle_y = ai_1_paddle_y - ai_speed

    #Get input from keyboard
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                movePaddle = -speed
            elif event.key == K_DOWN:
                movePaddle = speed
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                movePaddle = 0

    player_paddle_y = player_paddle_y + movePaddle

    #Stop both paddles from moving through ceiling and floors
    
    if player_paddle_y <= 0:
        player_paddle_y = 0
    elif player_paddle_y >= 400:
        player_paddle_y = 400

    if ai_1_paddle_y <= 0:
        ai_1_paddle_y = 0
    elif ai_1_paddle_y >= 400:
        ai_1_paddle_y = 400

    #Scoring
    if pong_ball_x < 5:
        aiScore =  aiScore + 1
        pong_ball_x = 320
        pong_ball_y = 233
     
        player_paddle_y = 215
    elif pong_ball_x > 995:
        playerScore = playerScore + 1
        pong_ball_x = 308
        pong_ball_y = 233

        ai_1_paddle_y = 215

    if aiScore == 5:
        whoWon = "AI Wins"
        gameover = False
    elif playerScore == 5:
        whoWon = "Player 1 Wins"
        gameover = False
    
    #Update Screen

    screen.blit(background, (0,0))

    pygame.draw.line(screen, (0,0,0), (500,0), (500, 480), 10)

    screen.blit (player_1_paddle, (player_paddle_x, player_paddle_y))
    screen.blit (ai_paddle, (ai_1_paddle_x, ai_1_paddle_y))

    screen.blit (pong_ball_1, (pong_ball_x, pong_ball_y))
    
    endgame = font.render(str(playerScore), True, (240,200,50))
    screen.blit(endgame, (200,100))

    endgame = font.render(str(aiScore), True, (240,200,50))
    screen.blit(endgame, (600,100))
    
    pygame.display.update() 

endgame = font.render(whoWon, True, (252,213,70))
screen.blit(endgame, (200,150))
  
pygame.display.update()


