import pygame
import math
import time

pygame.init()

###############Constantes##########################
# Boucle jusqu'a la fermeture du clavier
done = False

shift =  0   #pour l'appui des touches en extra

transparence = 125  #transparence des touches

maj = False

###############COULEURS############################
black = (0,0,0)
white = (255,255,255)

#reds
red = (255,0,0)
lightred = (255,51,51)
persianred = (204,51,51)
hotpink = (255,105,180, 255) #cuisse de nymphe emue
bloodorange = (255,102,51)
orange = (255,153,51)
ocre = (255,204,51)
jaune = (255,255,51)

#greens
lightgreen = (153,255,51)
green = (0,255,0)
aquamarine = (51,255,153,20)
turquoise = (48,213,200)

#blues
paleblue = (51,153,255)
blue = (0,0,255)
violet =(153,51,255)
mauve = (102,0,204)

##################Taille de la fenetre##############################
size = [640,480]        #214 pour juste clavier

screen = pygame.display.set_mode(size)

pygame.display.set_caption("GUI Keyboard")

#################Technicalites######################################
#Controle de refresh de l'ecran
clock = pygame.time.Clock()

#Police
font = pygame.font.Font(None, 25) #exemple, taille de la police, police doit etre mis
                                                             #dans le meme dossier que le programme
Message = ""
text = ""

#Array
TABW = 42
TABH = 42
MARGIN = 1

GRID = []
for row in range(5):
    GRID.append([])
    for column in range (12):
        GRID[row].append(0)

#Images de font
#background = pygame.image.load("test.jpg")

################Touches du clavier#################################
#ne pas oublier que certaines touches avec shift donne d'autres lettres
touches = ('1','2','3','4','5','6','7','8','9','0','-','=',
           'q','w','e','r','t','y','u','i','o','p',chr(8),chr(8),#backspace
           'a','s','d','f','g','h','j','k','l',';','^',chr(13),#return
            None,'z','x','c','v','b','n','m',chr(91),chr(93),'.',chr(13),#bracketg,d,backslash
           'Ctrl',None,'TAB',chr(32),chr(32),chr(32),chr(32),chr(44),chr(123),chr(125),chr(126),chr(13))#allcaps,space, virgule, crochetg,
shiftkeys = ('!','@','/','$','%','?','&','*','(',')','_','+',':','apos','|','<','>',chr(92)) #ligne des caracteres donnes par shift



##############Positions des touches################################

##############Boucle du programme principal########################
while done == False:
    # -----Boucle principale
    for event in pygame.event.get():    #lutilisateur fait quelque chose
        if event.type == pygame.QUIT: #si lutilisateur clique pour fermer la page
            done = True

    # -----Logique des appuis de touche


    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseposx = pygame.mouse.get_pos()[0]
        mouseposy = pygame.mouse.get_pos()[1]
        #print mouseposx

        column = mouseposx // (TABW + MARGIN)
        row = mouseposy // (TABH + MARGIN)

        tabpos = ((column)+((row*12)+1))-1

        if tabpos == 49:
            maj = not maj

    #ALLCAPS
        if maj == True:
            char = (str(touches[tabpos])).upper()
            if char != "NONE":
                Message = Message + char
        else:
            char = (str(touches[tabpos]))
            if char != "None":
                Message = Message + char

    #Traitement texte
            
        if tabpos == 22 or tabpos == 23:    #backspace
            Message = Message[:-2]

        if tabpos == 35 or tabpos == 47 or tabpos == 59:    #return le message
            print Message
            Message =""



    # --------------------------------- #


    # ----- Logique de dessin du clavier            
    screen.fill(turquoise)
   #screen.blit(background,[0,0])
    posx = 0
    posy = 0
    couleur = aquamarine
         
    text = font.render(""+ str(Message),True,hotpink)
    screen.blit(text,[5,220])



    for i in range(0,5):
        for j in range(0,12):
            
            if posx >= 129 and posx < 258 and posy > 171:   #space
                s = pygame.Surface((43,42))
                s.set_alpha(transparence)
                s.fill(couleur)
                screen.blit(s,(posx,posy))
            elif posx >= 430 and posy >= 43 and posy < 86:  #backspace
                s = pygame.Surface((43,42))
                s.set_alpha(transparence)
                s.fill(couleur)
                screen.blit(s,(posx,posy))
            elif posx >= 473 and posy >= 86 and posy <= 129:    #return
                s = pygame.Surface((42,43))
                s.set_alpha(transparence)
                s.fill(couleur)
                screen.blit(s,(posx,posy))
            else:
                s = pygame.Surface((42,42))
                s.set_alpha(transparence)
                s.fill(couleur)
                screen.blit(s,(posx,posy))
            
            posx += 43
            
        posx = 0
        
        posy += 43
        
    posy = 0
    
    textx = 16
    texty = 16
    k = 0
    x = 0
    y = 12
    if shift == 0:
        for i in range(0,5):        
            for k in range(x,y):
                if k >= len(touches):break
                text2 = font.render(touches[k], True,black)
                screen.blit(text2,[textx,texty])
                textx += 43
            x += 12
            y += 12
            textx = 16
            texty += 43
        
        
   # screen.blit(shift,[0,129])
   # screen.blit(backspace,[43,230])
    pygame.display.flip()       #update l'image de la fenetre
    # --------------------------------- #
    clock.tick(10)  #refresh de l'image 60x par seconde
pygame.quit()
