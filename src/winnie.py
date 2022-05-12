import pygame 

class Winnie(pygame.sprite.Sprite):
  
  def __init__(self, x, y, width, height, img_file, name):
      '''
      Defines the character "Winnie" that the user takes control of.
      Args:
      x = (int) x location of Winnie
      y = (int) y location of Winnie
      width = (int) width of the hitbox of Winnie
      height = (int) height of the hitbox of Winnie
      img_file = (str) image file name you want to use for Winnie
      name = (str) the name you want Winnie to use 
      Return = None
      '''
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(img_file).convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.name = name
      self.rect.height = height
      self.rect.width = width
      self.speed = 2
 
    
  def move_up(self):
    '''
    Moves Winnie up on the y axis
    Args = None
    Return = None
    '''
    self.rect.y -= self.speed
  def move_down(self):
    '''
    Moves Winnie down on the y axis
    Args = None
    Return = None
    '''
    self.rect.y += self.speed
  def move_left(self):
    '''
    Moves Winnie left on the x axis
    Args = None
    Return = None
    '''
    self.rect.x -= self.speed
  def move_right(self):
    '''
    Moves Winnie right on the x axis
    Args = None
    Return = None
    '''
    self.rect.x += self.speed
  
  