import pygame 

class Winnie(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, img_file, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.rect.height = height
        self.rect.width = width
        self.speed = 2
  '''
  Defines the character "Winnie" that the user takes control of.
  Args:
    x[int]: x location of Winnie
    y[int]: y location of Winnie
    width[int]: width of the hitbox of Winnie
    height[int]: height of the hitbox of Winnie
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

  