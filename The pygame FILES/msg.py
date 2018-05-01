import pygame

def write(dict, x, y, msg="pygame is cool", color= (0,0,0),font=25):
    myfont = pygame.font.Font(None,font)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    dict['screen'].blit(mytext,[x,y])
    text_width = mytext.get_width()
    text_height = mytext.get_height()
    
    return text_width, text_height