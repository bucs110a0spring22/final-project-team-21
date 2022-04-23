import pygame

class Background:
  
  screen_width = 0 
  screen_height = 0

  def __init__(self, screen_height, screen_width):
    '''Sets up the background.
    Args: None
    Return: None'''
    self.screen_height = screen_height
    self.screen_width = screen_width
    self.background_color = "black"

  

