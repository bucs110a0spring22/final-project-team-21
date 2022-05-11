import sys
import pygame

from src import winnie
from src import maze

vec = pygame.math.Vector2

class Controller:
  
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load("assets/maze3.png")
        self.width = self.background.get_rect().w
        self.height = self.background.get_rect().h
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.winnie = winnie.Winnie(195, 330, 15, 15)
        self.sprites = pygame.sprite.Group()
        self.mazeWalls = pygame.sprite.Group()
        self.sprites.add(self.winnie)
        wall1 = maze.Wall(5, 4, 390, 6)
        wall2 = maze.Wall(33, 33, 49, 34)
        wall3 = maze.Wall(190, 4, 21, 64)
        wall4 = maze.Wall(105, 33, 63, 34)
        wall5 = maze.Wall(390, 4, 6, 135)
        wall6 = maze.Wall(5, 4, 5, 135)
        wall7 = maze.Wall(33, 90, 49, 20)
        wall8 = maze.Wall(6, 133, 76, 6)
        wall9 = maze.Wall(319, 133, 75, 6)
        wall10 = maze.Wall(233, 33, 63, 34)
        wall11 = maze.Wall(76, 133, 6, 148)
        wall12 = maze.Wall(319, 133, 6, 148)
        wall13 = maze.Wall(319, 33, 49, 34)
        wall14 = maze.Wall(5, 275, 76, 6)
        wall15 = maze.Wall(319, 275, 76, 6)
        wall16 = maze.Wall(319, 90, 49, 20)
        wall17 = maze.Wall(5, 275, 5, 162)
        wall18 = maze.Wall(390, 275, 6, 162)
        wall19 = maze.Wall(148, 90, 105, 20)
        wall20 = maze.Wall(5, 347, 34, 21)
        wall21 = maze.Wall(362, 347, 34, 21)
        wall22 = maze.Wall(5, 433, 391, 6)
        wall23 = maze.Wall(190, 110, 21, 43)
        wall24 = maze.Wall(190, 282, 21, 43)
        wall25 = maze.Wall(148, 261, 105, 21)
        wall26 = maze.Wall(276, 90, 20, 106)
        wall27 = maze.Wall(105, 90, 20, 106)
        wall28 = maze.Wall(148, 347, 105, 21)
        wall29 = maze.Wall(120, 132, 47, 20)
        wall30 = maze.Wall(233, 132, 45, 20)
        wall31 = maze.Wall(190, 368, 21, 43)
        wall32 = maze.Wall(105, 218, 20, 64)
        wall33 = maze.Wall(276, 218, 20, 64)
        wall34 = maze.Wall(233, 304, 63, 21)
        wall35 = maze.Wall(33, 390, 135, 21)
        wall36 = maze.Wall(105, 304, 63, 21)
        wall37 = maze.Wall(233, 390, 135, 21)
        wall38 = maze.Wall(33, 304, 49, 21)
        wall39 = maze.Wall(319, 304, 49, 21)
        wall40 = maze.Wall(105, 347, 20, 43)
        wall41 = maze.Wall(62, 304, 20, 63)
        wall42 = maze.Wall(319, 304, 20, 63)
        wall43 = maze.Wall(276, 347, 20, 43)
        wall44 = maze.Wall(212, 176, 41, 6)
        wall45 = maze.Wall(147, 176, 38, 6)
        wall46 = maze.Wall(147, 176, 6, 62)
        wall47 = maze.Wall(247, 176, 6, 62)
        wall48 = maze.Wall(147, 232, 100, 6)
        self.mazeWalls.add(wall1, wall2, wall3, wall4 , wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21,wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48)
        pygame.font.init()
        pygame.key.set_repeat(1, 50)
        pygame.display.flip()
        """Load the sprites that we need"""


    def mainLoop(self):
        oldPlyerX, oldPlyerY = self.winnie.rect.topleft
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if not pygame.sprite.spritecollide(self.winnie, self.mazeWalls, False):
                      oldPlyerX, oldPlyerY = self.winnie.rect.topleft
                      if event.key == pygame.K_UP:
                        self.winnie.move_up()
                      if event.key == pygame.K_DOWN:
                        self.winnie.move_down()
                      if event.key == pygame.K_LEFT:
                        self.winnie.move_left()
                      if event.key == pygame.K_RIGHT:
                        self.winnie.move_right() 
                    else:
                      self.winnie.rect.topleft = oldPlyerX, oldPlyerY
               
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            # self.mazeWalls.draw(self.screen)
            pygame.display.flip()