import pygame, sys, os, random, math
from pygame.locals import *

pygame.init()
fpsClock=pygame.time.Clock() #to control the frame rate

#color 
WHITE=(255,255,255) 
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0) 
#globals
WIDTH=800
HEIGHT=600 
time=0 

#canvas declaration
window=pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption('Asteroids') 

#load images
bg=pygame.image.load(os.path.join('images','bg.jpg'))
debris=pygame.image.load(os.path.join('images','debris2_brown.png'))
ship=pygame.image.load(os.path.join('images','ship.png'))
# draw game function
def draw(canvas):
    global time
    canvas.fill(BLACK)  # fill the canvas with black
    canvas.blit(bg, (0, 0))  # draw the background image
    
    # Draw the debris image at the correct positions
    canvas.blit(debris, (time * 0.3, 0))  
    canvas.blit(debris, (time * 0.3 - WIDTH, 0))  
    
    time += 1  # Increment time
    canvas.blit(ship, (WIDTH/2-50,HEIGHT/2-50))

#(0,0) is the top left corner of the screen
#(WIDTH,0) is the top right corner of the screen
#(0,HEIGHT) is the bottom left corner of the screen
#(WIDTH,HEIGHT) is the bottom right corner of the screen
#handle input function
def handle_input():
    global time
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen():
    global time
    time+=1
    pygame.display.update()
    fpsClock.tick(30)


while True:
    draw(window)
    handle_input()
    update_screen()