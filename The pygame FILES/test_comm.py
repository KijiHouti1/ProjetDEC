import RPi.GPIO as GPIO
import spidev as spidev
import spicomm 
import colours
from clavier_fonctions import *
import pygame
#pew pew pew
#############--INIT--##########################
spi = spidev.SpiDev()
SPIinit()
pygame.init()

global refresh
refresh = 45
mode_ecran = 0
#############--Constantes--########################
# Boucle jusqu a la fermeture du clavier
done = False    #valeur determinant la fin du programme
transparence = 255  #transparence des touches

#Texte d'affichage du menu principal
textjeu = "Jeu"
textmessage = "Messagerie"
textsettings = "Parametres"
textquit = "Quitter"

#Texte d'affichage du menu jeu
textback = "Retour"
textchanger = "Couleurs"
textqui = "Joueur"
textgo = "Go"

#Texte d'affichage du menu messagerie
textopen = "Clavier"
textclavier = ""
textefface = "Effacer"

#############--FONCTIONS--#########################

def action():
    global mode_ecran
    global fond
    global selection1
    global selection2
    global selection3
    global selection4
    global selection5
    global selection6
    global selection7
    global selection8
    global Message
    global msg_type
    global envoi
    
    msg_type = None
    global dest
    global game_data

    if mode_ecran == 1:                                 #actions effectuees a l'ecran jeu
        if (position >= 0 and position <= 4):
            mode_ecran = 0  #menu principal

        if (position >= 55 and position <= 64):
            game_data = hex(position -55)
            print game_data
        elif (position >= 81 and position <= 90):
            game_data = hex(position -71)
            print game_data
        else:
            pass

        if position == 71:              #selection joueur 1
            if selection1 == black:
                selection1 = white
                selection2 = black
                selection3 = black
                selection4 = black
                dest = 0xA1
            elif selection1 == white:
                selection1 = black
                selection2 = black
                selection3 = black
                selection4 = black
                dest = None
        elif position == 97:            #selection joueur 2
            if selection2 == black:
                selection1 = black
                selection2 = white
                selection3 = black
                selection4 = black
                dest = 0xA2
            elif selection2 == white:
                selection1 = black
                selection2 = black
                selection3 = black
                selection4 = black
                dest = None
        elif position == 123:           #selection joueur 3
            if selection3 == black:
                selection1 = black
                selection2 = black
                selection3 = white
                selection4 = black
                dest = 0xA3
            elif selection3 == white:
                selection1 = black
                selection2 = black
                selection3 = black
                selection4 = black
                dest = None
        elif position == 149:           #selection joueur 4
            if selection4 == black:
                selection1 = black
                selection2 = black
                selection3 = black
                selection4 = white
                dest = 0xA4
            elif selection4 == white:
                selection1 = black
                selection2 = black
                selection3 = black
                selection4 = black
                dest = None
        else:
            pass

        if (position >= 181 and position <= 182):               #go -> send message
            global msg_to_send
            global msg_type
            msg_to_send = []    #message que l'on envoie
            msg_type = 0xDD         #gamedata
            msg_to_send.append(hex(source))
            msg_to_send.append(hex(dest))
            msg_to_send.append(hex(msg_type))
            msg_to_send.append(hex(len(game_data)))
            msg_to_send.append(game_data)
            envoi = True
            print msg_to_send
            selection1 = black
            selection2 = black
            selection3 = black
            selection4 = black            

    if mode_ecran == 2: 
        if (position >= 0 and position <= 4):
            mode_ecran = 0  #menu principal

        if (position >= 27 and position <= 31):
            mode_ecran = 4

        if (position >= 157 and position <= 161):
            Message = ""
            
        

        if position == 76:
            if selection5 == black:
                selection5 = white
                selection6 = black
                selection3 = black
                selection4 = black
                dest = 0xA1
            elif selection5 == white:
                selection5 = black
                selection6 = black
                selection7 = black
                selection8 = black
                dest = None
        elif position == 102:
            if selection6 == black:
                selection5 = black
                selection6 = white
                selection7 = black
                selection8 = black
                dest = 0xA2
            elif selection6 == white:
                selection5 = black
                selection6 = black
                selection7 = black
                selection8 = black
                dest = None
        elif position == 128:
            if selection7 == black:
                selection5 = black
                selection6 = black
                selection7 = white
                selection8 = black
                dest = 0xA3
            elif selection7 == white:
                selection5 = black
                selection6 = black
                selection7 = black
                selection8 = black
                dest = None
        elif position == 154:  #cliquer sur 4
            if selection8 == black:
                selection5 = black
                selection6 = black
                selection7 = black
                selection8 = white
                dest = 0xA4
                hex(dest)
                print type(dest)
            elif selection8 == white:
                selection5 = black
                selection6 = black
                selection7 = black
                selection8 = black
                dest = None
            
        else:
            pass

                    
        if (position >= 181 and position <= 182):
            global msg_to_send
            global msg_type
            
            msg_to_send = []    #message que l'on envoie
            msg_type = 0xEE         #textdata
            msg_to_send.append(hex(source))
            msg_to_send.append(hex(dest))
            msg_to_send.append(hex(msg_type))
            msg_to_send.append(hex(len(Message)+4))

            for i in range(0,(len(Message))):
                msg_to_send.append(hex(ord(Message[i])))
            envoi = True
            print msg_to_send
        
            selection5 = black
            selection6 = black
            selection7 = black
            selection8 = black
            Message = ""
            print "oui"
        

    if mode_ecran == 3:
        if (position >= 0 and position <= 4):
            mode_ecran = 0  #menu principal

        if (position >= 55 and position <= 74):
            fond = couleurs[position - 55]

    if mode_ecran == 4:
        clavier()


    return mode_ecran,envoi, fond, selection1, selection2, selection3, selection4,selection5, selection6, selection7, selection8, Message, dest, msg_type, position

def affichage():
    global mode_ecran
    global fond
    global selection1
    global selection2
    global selection3
    global selection4
    global selection5
    global selection6
    global selection7
    global selection8
    global Message
        
    if mode_ecran == 0:
        screen.fill(fond)
            
        text = font.render(textjeu, True, white)
        text2 = font.render(textmessage, True, white)
        text3 = font.render(textsettings, True, white)
        text4 = font.render(textquit, True, white)
                
        screen.blit(text,[50,15])
        screen.blit(text2,[50,55])
        screen.blit(text3,[50,95])
        screen.blit(text4,[50,135])

    if mode_ecran == 1:  #jeu
        screen.fill(fond)

        text = font.render(textback, True, white)    
        text2 = font.render(textchanger, True, white)
        text3 = font.render(textqui, True, white)
        text4 = font.render(textgo, True, white)
        text5 = font.render("1", True, white)    
        text6 = font.render("2", True, white)
        text7 = font.render("3", True, white)
        text8 = font.render("4", True, white)
                
        screen.blit(text,[0,0])
        screen.blit(text2,[115,55])
        screen.blit(text3,[300,55])
        screen.blit(text4,[485,255])
        screen.blit(text5,[335,90])
        screen.blit(text6,[335,130])
        screen.blit(text7,[335,170])
        screen.blit(text8,[335,210])
        
        for i in range(0,len(couleurs)):
            if i >= 10 :
                posy = 130
                posx = 50 + (i-10)*20
            else:
                posx = 50 + i*20
                posy = 100
            pygame.draw.circle(screen,couleurs[i],[posx,posy],10)
            pygame.draw.circle(screen,white,[posx,posy],10,1)

        pygame.draw.circle(screen,selection1,[365,100],10)
        pygame.draw.circle(screen,white,[365,100],10,4)

        pygame.draw.circle(screen,selection2,[365,140],10)
        pygame.draw.circle(screen,white,[365,140],10,4)

        pygame.draw.circle(screen,selection3,[365,180],10)
        pygame.draw.circle(screen,white,[365,180],10,4)

        pygame.draw.circle(screen,selection4,[365,220],10)
        pygame.draw.circle(screen,white,[365,220],10,4)

    if mode_ecran == 2:
        screen.fill(fond)

        text = font.render(textback, True, white)    
        text2 = font.render(textopen, True, white)
        
        text4 = font.render(textqui, True, white)
        text5 = font.render(textgo, True, white)
        text6 = font.render(textefface, True, white)
        text7 = font.render("1", True, white)    
        text8 = font.render("2", True, white)
        text9 = font.render("3", True, white)
        text10 = font.render("4", True, white)
        
        text11 = fontmessage.render(Message[0:27], True, black)
        text12 = fontmessage.render(Message[27:54], True, black)
        text13 = fontmessage.render(Message[54:81], True, black)
        text14 = fontmessage.render(Message[81:108], True, black)
        text15 = fontmessage.render(Message[108:135], True, black)
        text16 = fontmessage.render(Message[135:162], True, black)
        text17 = fontmessage.render(Message[162:189], True, black)
        text18 = fontmessage.render(Message[189:216], True, black)
        text19 = fontmessage.render(Message[216:240], True, black)
          
        pygame.draw.rect(screen, white, [5, 70, 440, 180])
        
        pygame.draw.circle(screen,selection5,[475,102],10)
        pygame.draw.circle(screen,white,[475,102],10,4)

        pygame.draw.circle(screen,selection6,[475,142],10)
        pygame.draw.circle(screen,white,[475,142],10,4)

        pygame.draw.circle(screen,selection7,[475,182],10)
        pygame.draw.circle(screen,white,[475,182],10,4)

        pygame.draw.circle(screen,selection8,[475,222],10)
        pygame.draw.circle(screen,white,[475,222],10,4)
        
        screen.blit(text,[0,0])
        screen.blit(text2,[1,40])
        
        screen.blit(text11,[6,71])
        screen.blit(text12,[6,91])
        screen.blit(text13,[6,111])
        screen.blit(text14,[6,131])
        screen.blit(text15,[6,151])
        screen.blit(text16,[6,171])
        screen.blit(text17,[6,191])
        screen.blit(text18,[6,211])
        screen.blit(text19,[6,231])
        
        screen.blit(text4,[430,40])
        screen.blit(text5,[485,255])
        screen.blit(text6,[1,255])
        screen.blit(text7,[450,90])
        screen.blit(text8,[450,130])
        screen.blit(text9,[450,170])
        screen.blit(text10,[450,210])


    if mode_ecran == 3:
        screen.fill(fond)

        text = font.render(textback, True, white)    
        text2 = font.render(textchanger, True, white)
                
        screen.blit(text,[0,0])
        screen.blit(text2,[0,55])

        
        
        for i in range(0,len(couleurs)):
            posx = 50 + i*20
            pygame.draw.circle(screen,couleurs[i],[posx,100],10)
            pygame.draw.circle(screen,white,[posx,100],10,1)

    return Message
        

#######################--DEBUT DU PROGRAMME--############################
MY_ADDR = 0xA1



fond = black
selection1 = fond
selection2 = fond
selection3 = fond
selection4 = fond
selection5 = fond
selection6 = fond
selection7 = fond
selection8 = fond


couleurclavier = white
couleurspace = white
couleurshift = white
couleurmaj = white

################--Taille de la fenetre--############################
size = [520,280]
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption("Test Communication")  #nom de la fenetre

###############--Technicalites--####################################
dest = None

#Controle de refresh de l'ecran
clock = pygame.time.Clock()

#Police
font = pygame.font.Font(None, 35) #exemple, taille de la police, police doit etre mis
                                                             #dans le meme dossier que le programme
fontmessage = pygame.font.Font(None, 25)

fontcouleur = pygame.font.Font(None, 25)

Message = ""
Message1 = ""
Message2 = ""
Message3 = ""
Message4 = ""
Message5 = ""
Message6 = ""
Message7 = ""
Message8 = ""

global source
global msg_type
global msg_status
source = MY_ADDR
envoi = None

#Array
TABW = 20       #largeur des cases du tableau graphique
TABH = 40       #hauteur
GRID = []       #declaration du tableau graphique

for row in range(5):    #ici on dessine le tableau
    GRID.append([])
    for column in range (26):
        GRID[row].append(0)
        

############--Programme principal--######################
while done == False:        #on observe si la valeur de fin du programme est toujours a false avant de continuer
    if(GPIO.input(22) == True):
        if (envoi == False) or (envoi == None):
            msg_status, pic_is = key_locking([0x6F])

        elif envoi == True:
            msg_status,pic_is = key_locking([0x60])
            envoi = False

        if msg_status == True:
            if pic_is == 0xa6:
                Msg = receive()
            if pic_is == 0x06:
                print "youra"
                write_msg(msg_to_send)
                del msg_to_send[:]
        else:
            pass

    # -----Boucle principale
    try:
        for event in pygame.event.get():    #lutilisateur fait quelque chose
            if event.type == pygame.QUIT: #si lutilisateur clique pour fermer la page
                done = True
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:    #sortie avec esc s'il y a un bug
                    done = True

        # -----Logique des appuis de touches
        
            elif event.type == pygame.MOUSEBUTTONDOWN:  #evenement d appui de la souris
                mouseposx = pygame.mouse.get_pos()[0]   #position de la souris en x
                mouseposy = pygame.mouse.get_pos()[1]   #et en y
                #print pygame.mouse.get_pos()
                column = mouseposx // (TABW)   #ici on distribue les positions de la souris selon le tableau graphique
                row = mouseposy // (TABH)
                position = ((column)+(row*26))+1
               #print position

                if mode_ecran == 0 :
                    if (position >= 3 and position <= 5):
                        mode_ecran = 1  #jeu

                    if (position >= 30 and position <= 38):
                        mode_ecran = 2  #messagerie

                    if (position >= 55 and position <= 62):
                        mode_ecran = 3  #parametres

                    if (position >= 82 and position <= 85):
                        done = True  #quitter

                else:
                    action()

            # --------------------------------- 


            # ----- Logique de dessin du clavier
            affichage()
            
            pygame.display.flip()       #update l'image de la fenetre
            # --------------------------------- #
            clock.tick(refresh)             #refresh l'image 120x par seconde
    
    except IndexError:                  #gestion d'erreur si on clique dans la case de texte du clavier
        print "en dehors de la zone"
pygame.quit()
