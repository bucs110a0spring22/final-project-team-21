import json
import pygame
import sys
from src import winnie
from src import maze
from src import dot
from src import ghost

class Controller:
    def __init__(self):
        '''
        Creates the screen and displays the background. Creates and place the wall objects and the dot objects on the screen in their appropriate location. Creates Winnie for the player to control later. Also creates sprite groups for Winnie, the walls, and the dots and sets the state to GAME.
        Args = None
        return = none
        '''
        pygame.init()
        self.background = pygame.image.load("assets/maze3.png")
        self.width = self.background.get_rect().w
        self.height = self.background.get_rect().h
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.sprites = pygame.sprite.Group()
        self.alldots = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.winnie = winnie.Winnie(193, 330, 17, 17,"assets/winnie.png", "Winnie")
        self.ghost1 = ghost.Ghost("pink", 8, 10 , 10, 10)
        self.ghost2 = ghost.Ghost("orange", 380, 390 , 10, 10)
        self.ghost3 = ghost.Ghost("blue", 8, 390 , 10, 10)
        self.ghost4 = ghost.Ghost("red", 380, 10 , 10, 10)
        self.ghosts.add(self.ghost1, self.ghost2, self.ghost3, self.ghost4)
        self.sprites.add(self.winnie)
        for i in range(0, 19):
          self.alldots.add(dot.Dot(91, (20 + (19.75 * i)), 3, 3), dot.Dot(305, (20 + (19.75 * i)), 3, 3), dot.Dot((20+ (19.75 * i)), 76, 3, 3), dot.Dot((20 + (19.75 * i)), 420, 3, 3))
          self.alldots.add(dot.Dot((20 +(19.8 * i)), 76, 3, 3), dot.Dot((20 +(19.8 * i)), 420, 3, 3), dot.Dot((20 +(19.8 * i)), 290, 3, 3), dot.Dot((20 + (19.8 * i)), 19.75, 3, 3)) if i != 9 else self.alldots.add(dot.Dot((20 +(19.8 * i)), 76, 3, 3), dot.Dot((20 +(19.8 * i)), 420, 3, 3))
        for i in range(0, 7):
          self.alldots.add(dot.Dot(136 + (21 * i), 162, 3 , 3), dot.Dot(136 + (21 * i), 250, 3 , 3), dot.Dot(136 + (21 * i), 119, 3 , 3), dot.Dot(136 + (21 * i), 376, 3 , 3)) if i != 3 else self.alldots.add(dot.Dot(136 + (21 * i), 162, 3 , 3), dot.Dot(136 + (21 * i), 250, 3 , 3))
        self.mazeWalls = pygame.sprite.Group()
        self.mazeWalls.add(maze.Wall(5, 4, 390, 6), maze.Wall(33, 33, 49, 34), maze.Wall(190, 4, 21, 64), maze.Wall(105, 33, 63, 34), maze.Wall(390, 4, 6, 135), maze.Wall(5, 4, 5, 135), maze.Wall(33, 90, 49, 20), maze.Wall(6, 133, 76, 6), maze.Wall(319, 133, 75, 6), maze.Wall(233, 33, 63, 34), maze.Wall(76, 133, 6, 148), maze.Wall(319, 133, 6, 148), maze.Wall(319, 33, 49, 34), maze.Wall(5, 275, 76, 6), maze.Wall(319, 275, 76, 6), maze.Wall(319, 90, 49, 20), maze.Wall(5, 275, 5, 162), maze.Wall(390, 275, 6, 162), maze.Wall(148, 90, 105, 20), maze.Wall(5, 347, 34, 21), maze.Wall(362, 347, 34, 21), maze.Wall(5, 433, 391, 6), maze.Wall(190, 110, 21, 43), maze.Wall(190, 282, 21, 43), maze.Wall(148, 261, 105, 21), maze.Wall(276, 90, 20, 106), maze.Wall(105, 90, 20, 106), maze.Wall(148, 347, 105, 21), maze.Wall(120, 132, 47, 20), maze.Wall(233, 132, 45, 20), maze.Wall(190, 368, 21, 43), maze.Wall(105, 218, 20, 64), maze.Wall(276, 218, 20, 64), maze.Wall(233, 304, 63, 21), maze.Wall(33, 390, 135, 21), maze.Wall(105, 304, 63, 21), maze.Wall(233, 390, 135, 21), maze.Wall(33, 304, 49, 21), maze.Wall(319, 304, 49, 21), maze.Wall(105, 347, 20, 43), maze.Wall(62, 304, 20, 63), maze.Wall(319, 304, 20, 63), maze.Wall(276, 347, 20, 43), maze.Wall(213, 176, 40, 6), maze.Wall(147, 176, 41, 6), maze.Wall(147, 176, 6, 62), maze.Wall(247, 176, 6, 62), maze.Wall(147, 232, 100, 6))
        pygame.font.init()
        pygame.key.set_repeat(1, 50)
        pygame.display.set_caption("Winnie the Pooh-Man")
        self.state = "GAME"


    def mainLoop(self):
      '''
      Calls either the gameloop function, gameover function, or gamewin function depending on the state of the game. 
      Args = None
      Return = None 
      '''
      while True:
        if(self.state == "GAME"):
          self.gameloop()
        elif(self.state == "GAMEOVER"):
          self.gameover()
        elif(self.state == "WIN"):
          self.gamewin()

    def gameloop(self):
        '''
        Allows the player to move up, down, left, or right in response to an arrow key. Checks to see if the player or ghost objects collide with a wall object, so that they don't go through the walls. Sets the state to 'GAMEOVER' if Winnie collides with a ghost. Sets state to 'GAMEWIN' if the player collects all the dots.
        Args = None
        return = none
        '''
        oldPlyerX, oldPlyerY = self.winnie.rect.topleft
        oldGhostX1, oldGhostY1 = self.ghost1.rect.topleft
        oldGhostX2, oldGhostY2 = self.ghost2.rect.topleft
        oldGhostX3, oldGhostY3 = self.ghost3.rect.topleft
        oldGhostX4, oldGhostY4 = self.ghost4.rect.topleft
        score = 0
        font = pygame.font.SysFont("Times", 20)

        while self.state == "GAME":
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
      
            if pygame.sprite.spritecollide(self.winnie, self.alldots, True):
              score += 10
            score_screen = font.render("Score:" + str(score), True, (255, 255, 255))

          if pygame.sprite.groupcollide(self.ghosts, self.mazeWalls, False, False):
            self.ghost1.rect.topleft = oldGhostX1, oldGhostY1
          else: 
            oldGhostX1, oldGhostY1 = self.ghost1.rect.topleft

          if pygame.sprite.groupcollide(self.ghosts, self.mazeWalls, False, False):
            self.ghost2.rect.topleft = oldGhostX2, oldGhostY2
          else: 
            oldGhostX2, oldGhostY2 = self.ghost2.rect.topleft

          if pygame.sprite.groupcollide(self.ghosts, self.mazeWalls, False, False):
            self.ghost3.rect.topleft = oldGhostX3, oldGhostY3
          else: 
            oldGhostX3, oldGhostY3 = self.ghost3.rect.topleft

          if pygame.sprite.groupcollide(self.ghosts, self.mazeWalls, False, False):
            self.ghost4.rect.topleft = oldGhostX4, oldGhostY4
          else: 
            oldGhostX4, oldGhostY4 = self.ghost4.rect.topleft

          if pygame.sprite.spritecollide(self.winnie, self.ghosts, False):
            self.state = "GAMEOVER"
            record = open("assets/scores.txt", 'a+')
            record.write("\n")
            record = record.write("Score: " + str(score))
          if not self.alldots:
            self.state = "WIN"
            record = open("assets/scores.txt", 'a+')
            record.write("\n")
            record = record.write("Score: " + str(score))
          self.screen.blit(self.background, (0, 0))
          self.screen.blit(score_screen, (0,0))
          self.ghosts.update()
          self.sprites.draw(self.screen)
          self.alldots.draw(self.screen)
          self.ghosts.draw(self.screen)
          pygame.display.flip()

    def gamewin(self):
        '''
        Displays 'You Win' if the player collects all the dots on the screen.
        Args = None
        return = none
        '''
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('You Win', True, (255, 255, 255))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              sys.exit()

    def gameover(self):
      '''
      Displays game over if Winnie collides with a ghost object
      Args = None
      return = none
      '''
      myfont = pygame.font.SysFont(None, 30)
      message = myfont.render('Game Over', True, (255, 255, 255))
      self.screen.blit(message, (self.width / 2, self.height / 2))
      pygame.display.flip()
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()