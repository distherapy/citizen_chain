#!/usr/bin/env python
#
#  main.py
#  
#  copyright 2021  <sixie6e@paracosmoclast>
#  
import pygame
import sys
from pygame.locals import *
import characters
# bubbles, land in one and the person tries to keep you in there. you have to get out of the bubble with them, pulling them from their paracosm.
pygame.init()
pygame.display.set_caption('citizen_chain')
window_size = (400, 400)
screen = pygame.display.set_mode(window_size, 0, 32)
avatar = pygame.image.load('/home/pi/Documents/citizen_chain/img/protag0.png')
location = [50,50]
backdrop = pygame.image.load('stage0.png')
backdropbox = backdrop.get_rect()
move_right = False
move_left = False

while True:
    screen.blit(backdrop, backdropbox)
    screen.blit(avatar, location)
    if move_right == True:
        location[0] =+ 4
    if move_left == True:
        location[0] -= 1
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False
            
    pygame.display.update()


