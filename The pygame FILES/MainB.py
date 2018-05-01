
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

def opt_menuA(text, opt, size, pos_x, pos_y, dist_sq):
    txt_size=msg.write(set_dict, pos_x*scale_w, pos_y*scale_h, text, color.WHITE,size)
    sqx= (pos_x-dist_sq)*scale_w        #point x du rect
    sqy= (pos_y-dist_sq)*scale_h        #point y du rect
    obt_width= (txt_size[0]+(dist_sq*2))*scale_w    #longueur du rect
    obt_height= (txt_size[1]+(dist_sq*2))*scale_h                           #hauteur du rect
    if(curr_pos==opt):      # numero d'option 
        if(press_dwn == 1):
            pygame.draw.rect(screen, color.RED2, (sqx,sqy,obt_width,obt_height))            
        else:
            pygame.draw.rect(screen, color.GRAY, (sqx,sqy,obt_width,obt_height))
    else:
        pygame.draw.rect(screen, color.WHITE, (sqx,sqy,obt_width,obt_height), 4)
    txt_size=msg.write(set_dict, pos_x*scale_w, pos_y*scale_h, text, color.WHITE,size)



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
sauvegarde = 0
counter_action =0 
menu = 0x00
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
    if menu == 0x00:   # Menu principal
        if curr_pos  == 0:      #Choix jeu
            if(action==1):
                menu = 0xA0
                action = 0
        elif curr_pos ==1:      #Choix option
            if(action==1):
                menu = 0xB0
                action = 0
        elif curr_pos ==2:      #choix Parametre avance
            if(action==1):
                menu = 0xC0
                action = 0
        elif curr_pos ==3:      #choix quitter
            if(action==1):
                menu = 0xD0
                action = 0

    if menu == 0xA0:
        if curr_pos  == 0:
            if(action==1):
                menu = 0xA1
                action = 0
        elif curr_pos ==1:
            if(action==1):
                menu = 0xA2
                action = 0

    if menu == 0xA1:
    	if curr_pos  == 0:
            if(action==1):
                #SEND ACTIVATE GAME

    if counter_action == 1:
        menu=0
        counter_action = 0
        action = 0
        curr_pos = 0
        
    #____________________________________________________________________

            


    #______________ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT_________
    screen.fill(color.BLACK)
    if menu == 0x00:
        opt_menuA("Jeu", 0, 110, 450, 200, 20)
        opt_menuA("Options", 1, 110, 450, 400, 20)
        opt_menuA("Parametres avances", 2, 110, 450, 600, 20)
        opt_menuA("Quitter", 3, 110, 450, 800, 20)
        
    if menu == 0xA0:        #Si on choisi Jeu
        opt_menuA("Choisir Jeu", 0, 110, 400, 400, 20)
        opt_menuA("Reprendre Jeu", 1, 110, 400, 800, 20)

    if menu == 0xA1:        #Si on choisi Jeu
        opt_menuA("Gwent", 0, 50, 400, 400, 20)
        opt_menuA("Blackjack", 1, 50, 400, 800, 20)

    if menu == 0xA2:        #Si on choisi Jeu
        if sauvegarde==0:
            opt_menuA("Aucune sauvegarde", 0, 50, 400, 400, 20)
        if sauvegarde==1:
            opt_menuA("Reprendre jeu", 1, 50, 400, 400, 20)

    if menu == 0xB0:        #Si on choisi Options
        opt_menuA("Son", 0, 50, 250, 500, 20)
        opt_menuA("Mute", 1, 50, 650, 500, 20)
        opt_menuA("Manette", 2, 50, 1050, 500, 20)

    if menu == 0xC0:        #Parametre avance
        opt_menuA("Fermer les manettes",  0, 50, 450, 200, 20)
        opt_menuA("Console",              1, 50, 450, 400, 20)
        opt_menuA("Supprimer profil",     2, 50, 450, 600, 20)
        opt_menuA("Supprimer Sauvegarde", 3, 50, 450, 800, 20)

    if menu == 0xD0:        #Quitter
        done=True
        
    pygame.display.flip()

    #____________________________________________________________________

    
    #FRAME RATE______________DO NOT CHANGE VALUE_________________________
    clock.tick(20)

##----------------------------------END----------------------------------
pygame.quit()
