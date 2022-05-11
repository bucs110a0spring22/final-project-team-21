import pygame

class Dot(pygame.sprite.Sprite):
  def __init__ (self, x, y, width, height):
    '''
    creates a small dot that the player collects to increase score
    x: int, x-coordinate of the dot
    y: int, y-coordinate of the dot
    img_file: str, calls an image that the dot uses as a sprite
    '''
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([width, height])
    self.image.fill("yellow")
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y