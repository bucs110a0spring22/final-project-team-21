import pygame
import random 

class Ghost:
  super()
 def __init__(self, x=0 ,y=0, img_file):
   """iniates the movement of the ghosts which chase the player
   x = (int) x location of each of the ghost
   y = (int) y location of each of the ghost
   img_file = (str) calls the image file of the ghost
   return = none"""
    self.image = pygame.image.load(file_name)
    for x in range(100):
      self.rect= self.image.get_rect()
  