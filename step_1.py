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

#rotate function
def rotate_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#load images
bg=pygame.image.load(os.path.join('images','bg.jpg'))
debris=pygame.image.load(os.path.join('images','debris2_brown.png'))
ship=pygame.image.load(os.path.join('images','ship.png'))
# draw game function
ship_x = WIDTH/2-50
ship_y = HEIGHT/2-50
ship_angle = 0
ship_is_rotating = False
ship_direction = 0
ship_speed = 10
ship_is_foward = False
def draw(canvas):
    global time
    canvas.fill(BLACK)  # fill the canvas with black
    canvas.blit(bg, (0, 0))  # draw the background image
    
    # Draw the debris image at the correct positions
    canvas.blit(debris, (time * 0.3, 0))  
    canvas.blit(debris, (time * 0.3 - WIDTH, 0))  
    
    time += 1  # Increment time
    canvas.blit(rotate_center(ship, ship_angle), (ship_x,ship_y))

#(0,0) is the top left corner of the screen
#(WIDTH,0) is the top right corner of the screen
#(0,HEIGHT) is the bottom left corner of the screen
#(WIDTH,HEIGHT) is the bottom right corner of the screen
#handle input function

def handle_input():
    global ship_angle, ship_is_rotating, ship_direction, ship_speed
    global ship_is_foward, ship_x, ship_y

    for event in pygame.event.get():  # Lặp qua tất cả các sự kiện trong hàng đợi sự kiện của Pygame
        if event.type == pygame.QUIT:  # Kiểm tra xem sự kiện có phải là yêu cầu thoát chương trình không
            pygame.quit()  # Thoát khỏi Pygame
            sys.exit()  # Đóng ứng dụng

        elif event.type == pygame.KEYDOWN:  # Kiểm tra xem phím có được nhấn xuống không
            if event.key == pygame.K_RIGHT:  # Nếu phím phải được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 1  # Đặt hướng xoay về bên phải
            elif event.key == pygame.K_LEFT:  # Nếu phím trái được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 0  # Đặt hướng xoay về bên trái
            elif event.key == pygame.K_UP:  # Nếu phím lên được nhấn
                ship_is_foward = True  # Đặt cờ cho biết tàu đang di chuyển về phía trước

        elif event.type == pygame.KEYUP:  # Kiểm tra xem phím có được nhả ra không
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                ship_is_rotating = False  # Dừng việc xoay tàu
            if event.key == pygame.K_UP:
                ship_is_foward = False  # Dừng việc di chuyển về phía trước

def update_screen():
    global time
    time+=1
    pygame.display.update()
    fpsClock.tick(30)


while True:
    draw(window)
    handle_input()
    update_screen()