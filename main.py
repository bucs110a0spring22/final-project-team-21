import pygame
#import your controller

def main():
  my_list = []
  for i in range(4):
    num = int(input("Enter a number"))
    my_list.append(num)
  print(my_list,'\n')
  my_list[0], my_list[3] = my_list[3], my_list[0]
  pygame.init()


  

    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

