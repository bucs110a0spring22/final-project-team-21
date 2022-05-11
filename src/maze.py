import pygame

class Wall(pygame.sprite.Sprite):
    # def __init__(self, x=0, y=0):
    #     super().__init__()
    #     self.image = pygame.Surface((3,3))
    #     self.image.fill("white")
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height = height
        self.rect.width = width
       
        
    

class Maze:
  #make a dictionary of all blocks in maze 
  #make sure in a direction when he isn't colliding in that group
  #creat wall class, anything you interact on screen need a class
  #when pac man collides with wall sprite group, don't mov
  #different facing images 
  def __init__(self,):
      wall_images = ["C"] 
      #["─","┌", "┐","└","┘","├","┴","┬","┤", "│"]
      # wall_images = [ "─","┐", "┌","│", "└", "┘",]
      
    
      #dots = "·"
      #WALL = "─│┌┐└┘├┴┬┤"
      #GHOST_GATES = "═║╔╗╚╝ ╠╩╦╣"
      #SUPER_DOT = "*"
  
      mazedoc = '''
1111111111111111111111111111
1CCCCCCCCCCCC11CCCCCCCCCCCC1
1C1111C11111C11C11111C1111C1
1C1111C11111C11C11111C1111C1
1C1111C11111C11C11111C1111C1
1CCCCCCCCCCCCCCCCCCCCCCCCCC1
1C1111C11C11111111C11C1111C1
1C1111C11C11111111C11C1111C1
1CCCCCC11CCCC11CCCC11CCCCCC1
111111C11111C11C11111C111111
111111C11111C11C11111C111111
111111C11CCCCCCCCCC11C111111
111111C11C111BB111C11C111111
CCCCCCC11C15000041C11CCCCCCC
CCCCCCCCCC10000001CCCCCCCCCC
CCCCCCC11C12000031C11CCCCCCC
111111C11C11111111C11C111111
111111C11CCCCCCCCCC11C111111
111111C11C11111111C11C111111
111111C11C11111111C11C111111
1CCCCCCCCCCCC11CCCCCCCCCCCC1
1C1111C11111C11C11111C1111C1
1C1111C11111C11C11111C1111C1
1CCC11CCCCCCCCCCCCCCCC11CCC1
111C11C11C11111111C11C11C111
111C11C11C11111111C11C11C111
1CCCCCC11CCCC11CCCC11CCCCCC1
1C1111111111C11C1111111111C1
1C1111111111C11C1111111111C1
1CCCCCCCCCCCCCCCCCCCCCCCCCC1
1111111111111111111111111111
'''
# maze = 400 x 443
  
      self.walls = pygame.sprite.Group()
      x = 0
      y = 0
      for i in mazedoc:
        if i in wall_images:
          wall = Wall(x, y)
          print(x)
          self.walls.add(wall)
          
            
        width_of_window = 560
        if x == width_of_window:
            x = 0
            y += (620/31)
        x = (x + (560/28))
      # self.image = pygame.image.load(img_file).convert_alpha()