import pygame
import color
import msg
import PAdLib as padlib

def setting(screen,width,height, scale_w, scale_h):
    set_dict={}
    set_dict={'screen':screen,'width':width,'height':height, 'scale_w':scale_w, 'scale_h':scale_h}
    return set_dict

def cursor_pos(PlusouMoins, max_option):
    global curr_pos
    curr_pos=curr_pos+PlusouMoins
    if curr_pos < 0:
        curr_pos = 0
    if curr_pos > max_option + 1:
        curr_pos = max_option
    return curr_pos




pygame.init()


#Define size of screen
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen=pygame.display.set_mode((width,height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF )
scale_w, scale_h = width/1920, height/1080
set_dict=setting(screen,width,height,scale_w,scale_h)

#Global variable section
done=False
global curr_pos
curr_pos = 0
#Window parameter
pygame.display.set_caption("BBB_Python")
clock=pygame.time.Clock()

## ---------------------------Main loop----------------------------------


while done==False:
    #______________ALL EVENT PROCESSING BELOW THIS COMMENT_______________
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done=True
            if event.key == pygame.K_UP:
                curr_pos = cursor_pos(1,4)
            if event.key == pygame.K_DOWN:
                curr_pos = cursor_pos(-1,4)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            mousex=pos[0]*scale_w
            mousey=pos[1]*scale_h
            
    #____________________________________________________________________
            

            

    #______________ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT___________
    '''
    if curr_pos  == 0:
        
    elif curr_pos ==1:
    elif curr_pos ==2:
        
    elif curr_pos ==3:
    '''    
    #____________________________________________________________________

            


    #______________ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT_________
    screen.fill(color.BLACK)
    
    if(curr_pos==0):
        pygame.draw.rect(screen, color.GRAY, (430,180,txt_size[0]+40,txt_size[1]+40))
    else:
        pygame.draw.rect(screen, color.WHITE, (430,180,txt_size[0]+40,txt_size[1]+40), 4)
        txt_size=msg.write(set_dict, 450, 200, "Jeu", color.WHITE,110)

    
    txt_size=msg.write(set_dict, 450, 400, "Option", color.WHITE,110)
    pygame.draw.rect(screen, color.WHITE, (430,380,txt_size[0]+40,txt_size[1]+40), 4)

    txt_size=msg.write(set_dict, 450, 600, "Paramètre avancé", color.WHITE,110)
    pygame.draw.rect(screen, color.WHITE, (430,580,txt_size[0]+40,txt_size[1]+40), 4)

    txt_size=msg.write(set_dict, 450, 800, "Quitter", color.WHITE,110)
    pygame.draw.rect(screen, color.WHITE, (430,780,txt_size[0]+40,txt_size[1]+40), 4)



    x_shift = 0.01
    y_shift = 0.50
    '''
    for i in range(4):
        for l in range(10):
            if i == 0:
                padlib.draw.rrect(screen, color.BLACK, ( (x_shift*1825)-2, (y_shift*1024)-2 ,144,89), 10, 2  )
                padlib.draw.rrect(screen, color.GRAY87, ( x_shift*1825, y_shift*1024 ,140,85), 10  )
                x_shift += 0.10
            else: #Bank
                padlib.draw.rrect(screen, color.BLACK, ( (x_shift*1825)-2, (y_shift*1024)-2 ,129,114), 10, 2  )
                padlib.draw.rrect(screen, color.GRAY87, ( x_shift*1825, y_shift*1024 ,125,110), 10  )
                x_shift += 0.08
        if i == 1: 
            padlib.draw.rrect(screen, color.BLACK, ( (x_shift*1825)-2, (y_shift*1024)-2 ,184,114), 10, 2  )
            padlib.draw.rrect(screen, color.GRAY87, ( x_shift*1825, y_shift*1024 ,180,110), 10  )
        x_shift=0.01
        if i == 1:
            x_shift = 0.05
        elif i == 0:
            y_shift += 0.10
        else:
            y_shift +=0.12
    '''
    pygame.display.flip()

    #____________________________________________________________________

    
    #FRAME RATE______________DO NOT CHANGE VALUE_________________________
    clock.tick(20)

##----------------------------------END----------------------------------
pygame.quit()
