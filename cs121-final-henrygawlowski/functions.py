import pygame
pygame.init()



def drawTextInBox(text, window, coordinates) :
    font = pygame.font.SysFont(pygame.font.get_fonts()[48], 32)
    text = font.render(text, True, (255, 255, 255))
    window.blit(text, coordinates)
    
    
def adjustPosition (pos: pygame.Rect) :
    if (pos.x)%16 <= 4 :
        pos.x -= (pos.x)%16
        return True
    if (pos.y)%16 <= 4 :
        pos.y -= (pos.y)%16
        return True
    if (pos.x)%16 >= 12 :
        pos.x = pos.x - (pos.x)%16 + 16
        return True
    if (pos.y)%16 >= 12 :
        pos.y = pos.y - (pos.y)%16 + 16
        return True
    return False
        
        
def handle_keys(keys: list, pos: pygame.Rect):
    direction_pressed = False
    #adjustPosition(pos)
    # If D is pressed
    if keys[pygame.K_d] and pos.right <= 760:
        pos.x += 8
    # If A is pressed
    if keys[pygame.K_a] and pos.left >= 0:
        pos.x -= 8
     
'''        #If S is pressed
    if keys[pygame.K_s]:
        direction_pressed = True
        pos.y += 2
    
        #If D is pressed
        direction_pressed = True
        pos.x += 2'''

def set_color(surface, color):
    rect = surface.get_rect()
    surf = pygame.Surface(rect.size, pygame.SRCALPHA)
    surf.fill(color)

    surface.blit(surf, (0, 0), None, pygame.BLEND_ADD)
    
def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

def collisionDetect(barPos, ballPos):
    if (ballPos.y-10) < (barPos.y) :
        if abs(ballPos.x -barPos.x) < 24 :
            #bounce straight
            print("straight")
            return 0
        elif abs(ballPos.x -barPos.x) < 32 :
            #bounce crooked
            print("crooked")
            return 1
        else:
            #no collision
            print("clean")
            return 2
        
def ballMove (barPos, ballPos, ballVely, ballVelx) :
    print(ballVelx,ballVely)
    if collisionDetect(barPos, ballPos) == 0:
        ballPos.x *= -1
    elif collisionDetect(barPos, ballPos) == 1 :
        ballPos.x *= -1
    elif collisionDetect(barPos, ballPos) == 2 :
        ballPos.x += ballVelx
        ballPos.y += ballVely