import pygame 
import random

class Winnie(pygame.sprite.Sprite):
  def __init__(self,x=0, y=0, filenames=None):
    super()
    self.image_set = [pygame.image.load(file_name) for f in filenames]
    self.current_image = 0
    self.image = self.image_set[self.current_image]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  '''
  Defines the character "Winnie" that the user takes control of.
  Args:
    x[int]: x location of Winnie
    y[int]: y location of Winnie
    filenames[str]: calls an image that Winnie uses as the sprite
  Return: 
    None
  '''
    
  def move(self, direction):
    if direction == "UP":
      self.rect.y = self.rect.y - 1
    elif direction == "DOWN":
      self.rect.y = self.rect.y + 1
    elif direction == "LEFT":
      self.rect.x = self.rect.x - 1
    elif direction == "RIGHT":
      self.rect.x = self.rect.x + 1

  '''
  Moves Winnie on the x and y axis depending on which direction the player wants to go.
  Args:
    direction[str]: The direction in which Winnie is moving.
  Return: 
    None
  '''
  
  def collide(self):
    '''
    allows for the player to collide and collect the dots, superdots, and fish
    Args = None
    return = none
    '''
    return random.randrange(3)

    def update(): 
      '''updates the game appearance each time Winnie moves and/or collides
          Args = None
          Return = None
      
      '''
      self.current_image = (self.current_image + 1) % len(self.image_set)
      self.image = self.image_set[self.current_image]
  