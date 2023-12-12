from classes import *
import pygame, sys, random
from pygame.locals import *
##from functions import *
from functions import *
from abomination import *
pygame.init()
from random import randrange

#load images
test_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/testbutton.png").convert_alpha()
play_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/playbutton.png").convert_alpha()
howtoplay_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/howtoplaybutton.png").convert_alpha()
quit_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/quitbutton.png").convert_alpha()
pellet = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/pellet.png").convert_alpha()

playeri = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/genericBar.png").convert_alpha()
playeri = pygame.transform.scale(playeri, (96,144))

#create button
test_button = Button(360, 125, test_img, 1)
quit_button = Button(360, 325, quit_img, 1)
play_button = Button(360, 125, play_img, 1)
howto_button = Button(360, 225, howtoplay_img, 1)



#Game vars
game_paused = False 
show_instructs = False
play_game = False
show_menu = True
tempnum = 0

width = 1200
height = 800
fps = 60
# player
playerWidth = 330
playerHeight = 35
player_speed = 15
player = pygame.Rect(width // 2 - playerWidth // 2, height - playerHeight - 10, playerWidth, playerHeight)

# ball
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(randrange(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)
ballVelx, ballVely = 1, -1

'''blockArray = abomination(playeri, True)
rectArray = abomination(playeri, False)

playeri = pygame.transform.scale(playeri, (64,64))
player = changColor(playeri, (255, 255, 255, 1))


pellet = pygame.transform.scale(pellet, (24,24))
pellet_rect = pellet.get_rect(topleft=(400,300))

player_rect = player.get_rect(topleft=(0, 400))

paddle = pygame.Rect(300, 400, 64, 12)'''



# blocks settings
block_list = [pygame.Rect(120 * i, 70 * j, 115, 65) for i in range(10) for j in range(4)]

pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def detect_collision(ballVelx, ballVely, ball, rect):
    if ballVelx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if ballVely > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        ballVelx, ballVely = -ballVelx, -ballVely
    elif delta_x > delta_y:
        ballVely = -ballVely
    elif delta_y > delta_x:
        ballVelx = -ballVelx
    return ballVelx, ballVely


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  window.blit(img, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))
    if show_instructs:
        drawTextInBox(text1,window,coordinates)

  elif play_game:
    
    # drawing world
    [pygame.draw.rect(window, (255,255,255), block) for color, block in enumerate(block_list)]
    pygame.draw.rect(window, pygame.Color('yellow'), player)
    pygame.draw.circle(window, pygame.Color('white'), ball.center, ball_radius)
    # ball movement
    ball.x += ball_speed * ballVelx
    ball.y += ball_speed * ballVely
    # collision left right
    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        ballVelx = -ballVelx
    # collision top
    if ball.centery < ball_radius:
        ballVely = -ballVely
    # collision player
    if ball.colliderect(player) and ballVely > 0:
        ballVelx, ballVely = detect_collision(ballVelx, ballVely, ball, player)
    # collision blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        ballVelx, ballVely = detect_collision(ballVelx, ballVely, ball, hit_rect)
        # special effect
        fps += 2
    # win, game over
    if ball.bottom > height:
        print('GAME OVER!')
        exit()
    elif not len(block_list):
        print('WIN!!!')
        exit()
    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.left > 0:
        player.left -= player_speed
    if key[pygame.K_RIGHT] and player.right < width:
        player.right += player_speed
    
    
    else:
        if quit_button.draw(window):
            pygame.quit()
            sys.exit()
        elif play_button.draw(window):
            play_game = True
        elif howto_button.draw(window):
            show_instructs = True 
    # update windowreen
    pygame.display.flip()
    clock.tick(fps)
