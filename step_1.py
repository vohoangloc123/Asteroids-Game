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
    global ship_angle, ship_is_rotating, ship_direction  # Sử dụng các biến toàn cục để thay đổi trạng thái xoay của tàu

    for event in pygame.event.get():  # Lặp qua tất cả các sự kiện trong hàng đợi sự kiện của Pygame
        if event.type == QUIT:  # Kiểm tra xem sự kiện có phải là yêu cầu thoát chương trình không
            pygame.quit()  # Thoát khỏi Pygame
            sys.exit()  # Đóng ứng dụng

        elif event.type == KEYDOWN:  # Kiểm tra xem phím có được nhấn xuống không
            if event.key == K_LEFT:  # Nếu phím trái được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 0  # Đặt hướng xoay về bên trái
            if event.key == K_RIGHT:  # Nếu phím phải được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 1  # Đặt hướng xoay về bên phải

        elif event.type == KEYUP:  # Kiểm tra xem phím có được nhả ra không
            if event.key == K_LEFT or event.key == K_RIGHT:  # Nếu phím trái hoặc phải được nhả ra
                ship_is_rotating = False  # Đặt cờ để dừng việc xoay tàu

    # Kiểm tra nếu cờ `ship_is_rotating` đang được bật, có nghĩa là phím trái hoặc phải đang được giữ
    if ship_is_rotating:  
        if ship_direction == 0:  # Nếu hướng xoay là bên trái
            ship_angle -= 10  # Giảm góc của tàu (xoay ngược chiều kim đồng hồ)
        else:  # Nếu hướng xoay là bên phải
            ship_angle += 10  # Tăng góc của tàu (xoay theo chiều kim đồng hồ)

def update_screen():
    global time
    time+=1
    pygame.display.update()
    fpsClock.tick(30)


while True:
    draw(window)
    handle_input()
    update_screen()