from classes import *
import pygame, sys, random
from pygame.locals import *
##from functions import *
from functions import *
from abomination import *
pygame.init()
 
 
print(pygame.font.get_fonts()[1])
#Game vars
game_paused = False 
show_instructs = False
play_game = False
show_menu = True
tempnum = 0

text1 = "instructions.txt"
coordinates = (200, 200)
 
# Colours
background = (0, 0, 0)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
windowWidth = 760
windowHeight = 500
 
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Breakout!!!')

#load images
test_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/testbutton.png").convert_alpha()
play_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/playbutton.png").convert_alpha()
howtoplay_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/howtoplaybutton.png").convert_alpha()
quit_img = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/quitbutton.png").convert_alpha()
pellet = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/pellet.png").convert_alpha()

playeri = pygame.image.load("cs121Final/cs121-final-henrygawlowski/resources/genericBar.png").convert_alpha()
playeri = pygame.transform.scale(playeri, (96,144))

score = 0
lives = 1

all_sprites_list = pygame.sprite.Group()

player = Player((255, 255, 255), 100, 10)
player.rect.x = 350
player.rect.y = 560

all_sprites_list.add(player)
'''blockArray = abomination(playeri, True)
rectArray = abomination(playeri, False)

playeri = pygame.transform.scale(playeri, (64,64))
player = changColor(playeri, (255, 255, 255, 1))


pellet = pygame.transform.scale(pellet, (24,24))
pellet_rect = pellet.get_rect(topleft=(400,300))

player_rect = player.get_rect(topleft=(0, 400))

paddle = pygame.Rect(300, 400, 64, 12)'''

#create button
test_button = Button(360, 125, test_img, 1)
quit_button = Button(360, 325, quit_img, 1)
play_button = Button(360, 125, play_img, 1)
howto_button = Button(360, 225, howtoplay_img, 1)
  
#def fonts
font = pygame.font.SysFont("arialblack", 40)

#def colors
text_col = (0, 0, 0)

ballVelx = 2
ballVely = -2

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  window.blit(img, (x, y))

    
'''def draw(pos: pygame.Rect):
  #window.blit(mapPrototype_img, (0, 0))
  
  window.fill(background)
  window.blit(player, player_rect)
  window.blit(pellet, pellet_rect)
  for i in range(len(blockArray)):
    window.blit(blockArray[i], rectArray[i])
    
def ballMove2 () :
  if pellet.center <= 24 :
    ballVelx = -ballVelx'''
 
#main function; game controller

run = True

#main game loop
while run :
  window.fill(background)
  #get inputs
  #keysPressed = pygame.key.get_pressed()
  #handle_keys(keysPressed, player_rect)
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player.moveLeft(5)
  if keys[pygame.K_RIGHT]:
    player.moveRight(5) 
        
  for event in pygame.event.get() :
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == QUIT :
      pygame.quit()
      sys.exit()
  
  #processing

  #render elements of the game
  #window.blit(player, player_rect)
  #check if game is paused
  if game_paused :
    if test_button.draw(window):
      game_paused = False
  elif show_instructs:
    drawTextInBox(text1,window,coordinates)

  elif play_game:
    #draw(player_rect)
    #ballMove(player_rect, pellet_rect, ballVelx, ballVely)
    all_sprites_list.update()
    
    pygame.draw.line(window, (255, 255, 255), [0, 38], [800, 38], 2)
    all_sprites_list.draw(window)
    pygame.display.flip()
  else:
    if quit_button.draw(window):
      pygame.quit()
      sys.exit()
    elif play_button.draw(window):
      play_game = True
    elif howto_button.draw(window):
      show_instructs = True 
      
      
  pygame.display.update()
  fpsClock.tick(FPS)
 
