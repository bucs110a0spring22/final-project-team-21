import pygame
import random 

class Ghost(pygame.sprite.Sprite):
  super()
  def __init__(self, name, x, y, img_file):
    """iniates the movement of the ghosts which chase the player
     x = (int) x location of each of the ghost
     y = (int) y location of each of the ghost
     img_file = (str) calls the image file of the ghost
     return = none"""
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convery_alpha()
    self.rect.x = x
    self.rect.y = y
    self.name = name +str(id(self))
    self.speed = 2
    for x in range(100):
      self.rect= self.image.get_rect()


  #method that moves the ghost in a specific direction
  #
    #make a update method stays within the maze, need to know the boundaries of the
  