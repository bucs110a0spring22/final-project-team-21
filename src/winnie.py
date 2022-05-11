import pygame 
import random

class Winnie(pygame.sprite.Sprite):
  # def __init__(self, x=0, y=0, width=0, height=0, img_file=None):
  #   super().__init__()
  #   pygame.sprite.Sprite.__init__(self)
  #   self.image = pygame.image.load(img_file).convert_alpha()
  #       #get the rectangle for positioning
  #   self.rect = self.image.get_rect()
  #   self.rect.x = x
  #   self.rect.y = y
  #   self.rect.height = height
  #   self.rect.width = width
  #       #set other attributes
  #   self.speed = 2
  #   self.health = 3
  def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        ########## PROF COMMENTS ###############
        #your code is doing what you told it to do
        self.image = pygame.Surface([width, height])
        self.image.fill("red")
        #if you want the image, set an image instead of a red square
        #self.image = pygame.image.load("assets/winniethepooh.png").convert_alpha()
        ########################################
      
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height = height
        self.rect.width = width
        self.speed = 2
  '''
  Defines the character "Winnie" that the user takes control of.
  Args:
    x[int]: x location of Winnie
    y[int]: y location of Winnie
    filenames[str]: calls an image that Winnie uses as the sprite
  Return: 
    None
  '''
    
  def move_up(self):
      self.rect.y -= self.speed
  def move_down(self):
      self.rect.y += self.speed
  def move_left(self):
      self.rect.x -= self.speed
  def move_right(self):
      self.rect.x += self.speed

  
  '''
  Moves Winnie on the x and y axis depending on which direction the player wants to go.
  Args:
    direction[str]: The direction in which Winnie is moving.
  Return: 
    None
  '''
  
  # def collide(self, opponent):
  #   '''
  #   allows for the player to collide and collect the dots, superdots, and fish
  #   Args = None
  #   return = none
  #   '''
  #   if (random.randrange(1)):
  #     self.health -= 1
  #     return False