import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        '''
        creates rectangle objects that are used as 'walls' for Winnie and the ghosts to collide with.
        x = (int) x location of each of the wall object
        y = (int) y location of each of the wall object
        width = (int) width of the wall object
        height = (int) height of the wall object
        return = none
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.height = height
        self.rect.width = width