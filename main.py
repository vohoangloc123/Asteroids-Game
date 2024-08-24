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
ship_thrusted=pygame.image.load(os.path.join('images','ship_thrusted.png'))
asteroid=pygame.image.load(os.path.join('images','asteroid.png'))
# draw game function
ship_x = WIDTH/2-50
ship_y = HEIGHT/2-50
ship_angle = 0
ship_is_rotating = False
ship_direction = 0
ship_speed = 10
ship_is_foward = False
no_asteroids = 5
asteroid_angle = []
asteroid_speed = 2
asteroid_x = [] #random.randint(0, WIDTH)
asteroid_y = [] #random.randint(0, HEIGHT)

for i in range(0, no_asteroids):
    asteroid_x.append(random.randint(0, WIDTH))
    asteroid_y.append(random.randint(0, HEIGHT))
    asteroid_angle.append(random.randint(0, 360))
def draw(canvas):
    global time
    global ship_is_foward
    canvas.fill(BLACK)  # fill the canvas with black
    canvas.blit(bg, (0, 0))  # draw the background image
    
    # Draw the debris image at the correct positions
    canvas.blit(debris, (time * 0.3, 0))  
    canvas.blit(debris, (time * 0.3 - WIDTH, 0))  
   
    time += 1  # Increment time
    for i in range(0, no_asteroids):
        canvas.blit(rotate_center(asteroid,time), (asteroid_x[i], asteroid_y[i]))
    if ship_is_foward:  # If the ship is moving forward
        canvas.blit(rotate_center(ship_thrusted, ship_angle), (ship_x,ship_y))
    else:
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

        elif event.type == KEYDOWN:  # Kiểm tra xem phím có được nhấn xuống không
            if event.key == K_RIGHT:  # Nếu phím phải được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 0  # Đặt hướng xoay về bên phải
            elif event.key == K_LEFT:  # Nếu phím trái được nhấn
                ship_is_rotating = True  # Đặt cờ cho biết tàu đang xoay
                ship_direction = 1  # Đặt hướng xoay về bên trái
            elif event.key == K_UP:  # Nếu phím lên được nhấn
                ship_is_foward = True  # Đặt cờ cho biết tàu đang di chuyển về phía trước
                ship_speed = 10  # Đặt tốc độ di chuyển của tàu
        elif event.type == KEYUP:  # Kiểm tra xem phím có được nhả ra không
                if event.key == K_RIGHT or event.key == K_LEFT:
                    ship_is_rotating = False  # Dừng việc xoay tàu
                else:
                    ship_is_foward = False
    # Cập nhật góc tàu khi đang xoay
    if ship_is_rotating:
        if ship_direction == 0:  # Nếu hướng xoay là bên trái
            ship_angle = ship_angle - 10  # Giảm góc của tàu (xoay ngược chiều kim đồng hồ)
        else:  # Nếu hướng xoay là bên phải
            ship_angle = ship_angle + 10  # Tăng góc của tàu (xoay theo chiều kim đồng hồ)

    # Cập nhật vị trí tàu khi di chuyển
    if ship_is_foward or ship_speed>0:
        ship_x = (ship_x + math.cos(math.radians(ship_angle))*ship_speed )
        ship_y = (ship_y + -math.sin(math.radians(ship_angle))*ship_speed )
        if ship_is_foward==False:
            ship_speed-=0.1
def update_screen():
    global time
    time+=1
    pygame.display.update()
    fpsClock.tick(30)

def game_logic():
    for i in range(0, no_asteroids):
        asteroid_x[i]=(asteroid_x[i]+math.cos(math.radians(asteroid_angle[i]))*asteroid_speed)
        asteroid_y[i]=(asteroid_y[i]+-math.sin(math.radians(asteroid_angle[i]))*asteroid_speed)   
        if asteroid_y[i]<0:
            asteroid_y[i]=HEIGHT #reset the position of the asteroid
        if asteroid_y[i]>HEIGHT:
            asteroid_y[i]=0 #reset the position of the asteroid
        if asteroid_x[i]<0:
            asteroid_x[i]=WIDTH #reset the position of the asteroid
        if asteroid_x[i]>WIDTH:
            asteroid_x[i]=0 #reset the position of the asteroid
while True:
    draw(window)
    handle_input()
    update_screen()
    game_logic()