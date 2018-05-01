
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
    if curr_pos > max_option:
        curr_pos = max_option
    return curr_pos




pygame.init()


#Define size of screen
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen=pygame.display.set_mode((width,height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF )
scale_w, scale_h = float(width)/1920, float(height)/1080
set_dict=setting(screen,width,height,scale_w,scale_h)

#Global variable section
done=False
global curr_pos
curr_pos = 0
press_dwn = 0
action = 0
counter_action =0 
menu = 0
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
                curr_pos = cursor_pos(1,3)
            if event.key == pygame.K_DOWN:
                curr_pos = cursor_pos(-1,3)
            if event.key == pygame.K_a:
                press_dwn=1
            if event.key == pygame.K_b:
                counter_action = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                action = 1
                press_dwn = 0
            

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            mousex=pos[0]*scale_w
            mousey=pos[1]*scale_h
            
    #____________________________________________________________________
            

            

    #______________ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT___________
    if menu == 0:
        if curr_pos  == 0:
            if(action==1):
                menu = 1
                action = 0
        elif curr_pos ==1:
            if(action==1):
                menu = 2
                action = 0
        elif curr_pos ==2:
            if(action==1):
                menu = 3
                action = 0
        elif curr_pos ==3:
            if(action==1):
                menu = 4
                action = 0
    if counter_action == 1:
        menu=0
        counter_action = 0
        action = 0
        curr_pos = 0
        
    #____________________________________________________________________

            


    #______________ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT_________
    screen.fill(color.BLACK)
    print scale_w, scale_h
    print width, height
    if menu == 0:
        txt_size=msg.write(set_dict, 450*scale_w, 200*scale_h, "Jeu", color.WHITE,110)
        if(curr_pos==0):
            if(press_dwn == 1):
                pygame.draw.rect(screen, color.RED2, (430*scale_w,180*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))            
            else:
                pygame.draw.rect(screen, color.GRAY, (430*scale_w,180*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
        else:
            pygame.draw.rect(screen, color.WHITE, (430*scale_w,180*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h), 4)
        txt_size=msg.write(set_dict, 450*scale_w, 200*scale_h, "Jeu", color.WHITE,110)

        
        txt_size=msg.write(set_dict, 450*scale_w, 400*scale_h, "Options", color.WHITE,110)
        if(curr_pos==1):
            if(press_dwn == 1):
                pygame.draw.rect(screen, color.RED2, (430*scale_w,380*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
            else: 
                pygame.draw.rect(screen, color.GRAY, (430*scale_w,380*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
        else:
            pygame.draw.rect(screen, color.WHITE, (430*scale_w,380*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h), 4)
        txt_size=msg.write(set_dict, 450*scale_w, 400*scale_h, "Options", color.WHITE,110)

        txt_size=msg.write(set_dict, 450*scale_w, 600*scale_h, "Parametres avances", color.WHITE,110)
        if(curr_pos==2):
            if(press_dwn == 1):
                pygame.draw.rect(screen, color.RED2, (430*scale_w,580*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
            else: 
                pygame.draw.rect(screen, color.GRAY, (430*scale_w,580*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
        else:
            pygame.draw.rect(screen, color.WHITE, (430*scale_w,580*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h), 4)
        txt_size=msg.write(set_dict, 450*scale_w, 600*scale_h, "Parametres avances", color.WHITE,110)

        txt_size=msg.write(set_dict, 450*scale_w, 800*scale_h, "Quitter", color.WHITE,110)
        if(curr_pos==3):
            if(press_dwn == 1):
                pygame.draw.rect(screen, color.RED2, (430*scale_w,780*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
            else: 
                pygame.draw.rect(screen, color.GRAY, (430*scale_w,780*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h))
        else:
            pygame.draw.rect(screen, color.WHITE, (430*scale_w,780*scale_h,txt_size[0]+40*scale_w,txt_size[1]+40*scale_h), 4)
        txt_size=msg.write(set_dict, 450, 800*scale_h, "Quitter", color.WHITE,110)

    if menu ==1:
        txt_size=msg.write(set_dict, 300*scale_w, 333*scale_h, "GAB", color.WHITE,110)
        txt_size=msg.write(set_dict, 300*scale_w, (333*scale_h)+txt_size[1], "   0-1  ", color.WHITE,110)
        txt_size=msg.write(set_dict, 300*scale_w, (666*scale_h)+txt_size[1], "   0-1  ", color.WHITE,110)
        txt_size=msg.write(set_dict, 300*scale_w, 666*scale_h, "PHIL", color.WHITE,110)
        txt_size=msg.write(set_dict, 700*scale_w, 500*scale_h, "VS", color.WHITE,110)
        txt_size=msg.write(set_dict, 875*scale_w, 333*scale_h, "Francis", color.WHITE,110)
        txt_size=msg.write(set_dict, 875*scale_w, (333*scale_h)+txt_size[1], "   0-1  ", color.WHITE,110)
        txt_size=msg.write(set_dict, 875*scale_w, 666*scale_h, "LAURENT", color.WHITE,110)
        txt_size=msg.write(set_dict, 875*scale_w, (666*scale_h)+txt_size[1], "   0-1  ", color.WHITE,110)


    if menu ==2:
        txt_size=msg.write(set_dict, 200, 500*scale_h, "GROSSES OPTIONS SALES", color.WHITE,150)
    if menu ==3:
        txt_size=msg.write(set_dict, 200, 500*scale_h, "PARAMETRE", color.WHITE,100)
    if menu ==4:
        done=True
        
    pygame.display.flip()

    #____________________________________________________________________

    
    #FRAME RATE______________DO NOT CHANGE VALUE_________________________
    clock.tick(20)

##----------------------------------END----------------------------------
pygame.quit()
