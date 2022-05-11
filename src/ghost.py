import pygame
import random 

class Ghost(pygame.sprite.Sprite):
  def __init__(self, color, x, y, width, height):
    """
    iniates the movement of the ghosts which chase the player
    x = (int) x location of each of the ghost
    y = (int) y location of each of the ghost
    img_file = (str) calls the image file of the ghost
    return = none
    """
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.rect.height = height
    self.rect.width = width
    
  def update(self):
      self.rect.x += random.randint(-5, 5)
      self.rect.y += random.randint(-5, 5)