import pygame
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        #get mouse pos
        pos = pygame.mouse.get_pos()
        
        #check clicked conditions and mouse over
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        #draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
    
class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def update(self):
        # Update object logic goes here
        pass
    
class Player(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
          
    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:
          self.rect.x = 700