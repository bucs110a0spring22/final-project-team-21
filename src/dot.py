import pygame

class Dot(pygame.sprite.Sprite):

  def __init__ (self, x, y, img_file="", is_superdot= False):
    '''
    creates a small dot that the player collects to increase score
    x: int, x-coordinate of the dot
    y: int, y-coordinate of the dot
    img_file: str, calls an image that the dot uses as a sprite
    '''
    super().__init__(self)
    self.image = pygame.image.load(img_file)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.is_superdot = is_superdot
    if self.super_dot:
        """double the size"""


  def superDot(self, x, y, img_file=""):
    '''
    creates a big dot that the user collects that increase score and makes the "friends" vulnerable
    x: int, x-coordinate of the superdot
    y: int, y-coordinate of the superdot
    img_file: str, calls an image the superdot uses as a sprite
    '''
    super().__init__(self)
    self.image = pygame.image.load(img_file)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

    
  def fish(self, x, y, img_file=""):
    '''
    creates the fish object that the user can collect for additional points
    x: int, x-coordinate for the fish
    y: int, y-coordinate for the fish
    img_file: str, calls an image that the fish uses as the sprite
    '''
    super().__init__(self)
    self.image = pygame.image.load(img_file)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y