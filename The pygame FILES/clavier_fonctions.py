def clavier():
    global donekb
    global tabposkb
    global couleur
    global shift
    global maj
    global symbol
    global couleurclavier
    global mode_ecran
    global Message
    global Message1
    global Message2
    global Message3
    global Message4
    global Message5
    global Message6
    global Message7
    global Message8
    

    ################--Taille de la fenetre--############################
    sizeclaviery = 240
    size = [516,sizeclaviery]        #environ la moitie de l'ecran tactile
    screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
 
    #############--Constantes--########################
    # Boucle jusqu a la fermeture du clavier
    donekb = False    #valeur determinant la fin du programme
    transparence = 255  #transparence des touches

    #valeurs de base des touches de traitement
    maj = False #allcaps
    shift = False
    tabposkb = None   #tab
    espace = False
    symbol =  0   #pour l appui des touches en extra
    
    #Message = ""    #string du message qu on print
    text = ""       #string du message qui apparait pendant l ecriture

    #Array
    TABW = 42       #largeur des cases du tableau graphique
    TABH = 42       #hauteur
    MARGIN = 1      #1 pixel entre chaque case

    GRID = []       #declaration du tableau graphique

    for row in range(5):    #ici on dessine le tableau
        GRID.append([])
        for column in range (12):
            GRID[row].append(0)

    #background = pygame.image.load("lion.jpg")

    ##############--Touches du clavier--###############################
    touches = ('','1','2','3','4','5','6','7','8','9','0','-',
               'q','w','e','r','t','y','u','i','o','p',chr(8),chr(8),#backspace
               'a','s','d','f','g','h','j','k','l',';','^',chr(13),#return
               'St','z','x','c','v','b','n','m',chr(91),chr(93),'.',chr(13),#bracketg,d,backslash
               'SYM','CAP','TAB',chr(32),chr(32),chr(32),chr(32),chr(44),chr(123),chr(125),chr(126),chr(13))#space, virgule, crochetg,

    #touches en extra quand on appuie sur SYM
    symkeys = ('!','@','/','$','%','?','&','*','(',')','_','+',
                 '','','','','','','','','','=',chr(8),chr(8),
                 '','','','','','','','','',':','|',chr(13),
                 '','','','','','','','','<','>',chr(92),chr(13),
                 'abc','','',chr(32),chr(32),chr(32),chr(32),chr(39),'','','',chr(13))

    ############--Programme principal--######################
    while mode_ecran == 4:        #on observe si la valeur de fin du programme est toujours a false avant de continuer

        # -----Boucle principale
        try:
            for event in pygame.event.get():    #lutilisateur fait quelque chose
                if event.type == pygame.QUIT: #si lutilisateur clique pour fermer la page
                    mode_ecran = 2
                elif event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_ESCAPE:    #sortie avec esc s'il y a un bug
                        mode_ecran = 2

            # -----Logique des appuis de touches
            
                elif event.type == pygame.MOUSEBUTTONDOWN:  #evenement d appui de la souris
                    mouseposx = pygame.mouse.get_pos()[0]   #position de la souris en x
                    mouseposy = pygame.mouse.get_pos()[1]   #et en y
                    column = mouseposx // (TABW + MARGIN)   #ici on distribue les positions de la souris selon le tableau graphique
                    row = mouseposy // (TABH + MARGIN)
                    tabposkb = ((column)+((row*12)+1))-1      #comme ca, on a la position de la case associee a une lettre
                    
                    if tabposkb == 0:
                        size = [520,280]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        Message = ""
                        mode_ecran = 2

                    #--- Gestion de Message
                    if tabposkb == 36:    #position de shift
                        shift = True
                        break;

                    elif tabposkb == 48:  #position de SYM
                        symbol = not symbol

                    elif tabposkb == 49:  #position de CAP pour all caps
                        maj = not maj

                    if symbol == 0:     #selon si on est avec le clavier des touches supplementaires ou non
                        if maj == True: #ALLCAPS
                            if shift == False:      #gestion de shift quand on est en mode all caps
                                if (tabposkb == 48) or (tabposkb == 49):
                                    char = ""
                                else:
                                    char = (str(touches[tabposkb])).upper()
                            elif shift == True:
                                char = (str(touches[tabposkb]))

                            
                            elif tabposkb == 50:    #Tab => apparait comme une case sur clavier, mais print reellement une tabulation horizontale
                                char = "\t"

                            elif char == "SYM":     #pour ne pas ecrire SYM et CAP dans la barre de texte du clavier
                                char = ""
                                
                            Message = Message + char
                        else:
                            if shift == False:  #gestion de shift
                                char = (str(touches[tabposkb]))
                            elif shift == True:
                                char = (str(touches[tabposkb])).upper()
                            
                            if tabposkb == 50:    #tab
                                char = "\t"

                            elif char == "SYM": 
                                char = ""

                            elif char == "CAP":
                                char = ""
                                
                            Message = Message + char
                            
                    if symbol == 1:     #gestion du clavier symboles
                            char = (str(symkeys[tabposkb]))

                            if tabposkb == 50:    #tab
                                char = "\t"

                            elif char == "abc": #pour ne pas ecrire le abc qui ramene au clavier principal
                                char = ""

                            elif char == "CAP": #pour ne pas ecrire CAP
                                char = ""
                                
                            Message = Message + char

                #Traitement texte
                        
                    if tabposkb == 22 or tabposkb == 23:    #backspace
                        Message = Message[:-2]

                    if tabposkb == 35 or tabposkb == 47 or tabposkb == 59:    #return le message
                        Message = Message [:-1]
                        size = [520,280]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        mode_ecran = 2
                        #Message = ""
                        
                    shift = False
                # --------------------------------- 


                # ----- Logique de dessin du clavier            
                screen.fill(black)  #fond noir
                #screen.blit(background,[0,0])  #uncomment la ligne si on a une image de background
                posx = 0    #les positions des carres representants les touches
                posy = 0
                space = 0

                Message1 = Message[0:30]
                Message2 = Message[30:60]
                Message3 = Message[60:90]
                Message4 = Message[90:120]
                Message5 = Message[120:150]
                Message6 = Message[150:180]
                Message7 = Message[180:210]
                Message8 = Message[210:240]

                if (len(Message)>=0) and (len(Message)<30):
                    if sizeclaviery > 240:
                        sizeclaviery = 240
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])

                if (len(Message)>=30) and (len(Message)<60):
                    if sizeclaviery < 260:
                        sizeclaviery = 260
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 260:
                        sizeclaviery = 260
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    
                if (len(Message)>=60) and (len(Message)<90):
                    if sizeclaviery < 280:
                        sizeclaviery = 280
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 280:
                        sizeclaviery = 280
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    
                if (len(Message)>=90) and (len(Message)<120):
                    if sizeclaviery < 300:
                        sizeclaviery = 300
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 300:
                        sizeclaviery = 300
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    
                if (len(Message)>=120) and (len(Message)<150):
                    if sizeclaviery < 320:
                        sizeclaviery = 320
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 320:
                        sizeclaviery = 320
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    textboite5 = fontcouleur.render(""+ str(Message5),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite5,[5,300])
                    
                if (len(Message)>=150) and (len(Message)<180):
                    if sizeclaviery < 340:
                        sizeclaviery = 340
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 340:
                        sizeclaviery = 340
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    textboite5 = fontcouleur.render(""+ str(Message5),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite5,[5,300])
                    textboite6 = fontcouleur.render(""+ str(Message6),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite6,[5,320])

                if (len(Message)>=180) and (len(Message)<210):
                    if sizeclaviery < 360:
                        sizeclaviery = 360
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                    if sizeclaviery > 360:
                        sizeclaviery = 360
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    textboite5 = fontcouleur.render(""+ str(Message5),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite5,[5,300])
                    textboite6 = fontcouleur.render(""+ str(Message6),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite6,[5,320])
                    textboite7 = fontcouleur.render(""+ str(Message7),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite7,[5,340])

                if (len(Message)>=210) and (len(Message)<240):
                    if sizeclaviery < 380:
                        sizeclaviery = 380
                        size = [516,sizeclaviery]
                        screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
                        
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    textboite5 = fontcouleur.render(""+ str(Message5),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite5,[5,300])
                    textboite6 = fontcouleur.render(""+ str(Message6),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite6,[5,320])
                    textboite7 = fontcouleur.render(""+ str(Message7),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite7,[5,340])
                    textboite8 = fontcouleur.render(""+ str(Message8),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite8,[5,360])        

                if len(Message)>= 239:
                    textboite1 = fontcouleur.render(""+ str(Message1),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite1,[5,220])
                    textboite2 = fontcouleur.render(""+ str(Message2),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite2,[5,240])
                    textboite3 = fontcouleur.render(""+ str(Message3),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite3,[5,260])
                    textboite4 = fontcouleur.render(""+ str(Message4),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite4,[5,280])
                    textboite5 = fontcouleur.render(""+ str(Message5),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite5,[5,300])
                    textboite6 = fontcouleur.render(""+ str(Message6),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite6,[5,320])
                    textboite7 = fontcouleur.render(""+ str(Message7),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite7,[5,340])
                    textboite8 = fontcouleur.render(""+ str(Message8),True,white) #affichage du message qu on ecrit dans la barre de texte
                    screen.blit(textboite8,[5,360])              




                for i in range(0,5):                    #ici on dessine les touches de clavier et on controle la couleur
                    for j in range(0,12):
                        coulpos = ((j)+((i*12)+1))-1
                        if coulpos == tabposkb:
                            couleurclavier = persianred
                            
                        if posx == 129 and posx <= 258 and posy > 171:   #space
                            s = pygame.Surface((171,42)) 
                            s.set_alpha(transparence)       #transparence des touches, si on a un background par exemple
                            s.fill(couleurspace)
                            screen.blit(s,(posx,posy))
                            space = 1
                            
                        elif posx == 0 and posy == 129:     #shift
                            if shift == True:
                                if symbol != 1:
                                    couleurshift = persianred
                            else: couleurshift = white
                            s = pygame.Surface((42,42))
                            s.set_alpha(transparence)
                            s.fill(couleurshift)
                            screen.blit(s,(posx,posy))
                            
                        elif posx == 43 and posy == 172:    #allcaps
                            if maj == True:
                                couleurmaj = persianred
                            else: couleurmaj = white
                            s = pygame.Surface((42,42))
                            s.set_alpha(transparence)
                            s.fill(couleurmaj)
                            screen.blit(s,(posx,posy))
                            
                        elif posx >= 430 and posy >= 43 and posy < 86:  #backspace
                            s = pygame.Surface((43,42))
                            s.set_alpha(transparence)
                            s.fill(couleurclavier)
                            screen.blit(s,(posx,posy))
                            
                        elif posx >= 473 and posy >= 86 and posy <= 129:    #return
                            s = pygame.Surface((42,43))
                            s.set_alpha(transparence)
                            s.fill(couleurclavier)
                            screen.blit(s,(posx,posy))
                            
                        else:
                            if space == 1:
                                if posx >= 258:
                                    space = 0
                            else:                           #toutes les autres touches
                                s = pygame.Surface((42,42)) 
                                s.set_alpha(transparence)
                                s.fill(couleurclavier)
                                screen.blit(s,(posx,posy))
                            
                        couleurclavier = white
                        posx += 43  #distance de 43 px entre les carres
                        
                    posx = 0
                    
                    posy += 43 #43 px mais en hauteur
                    
                space = 0
                tabposkb = None
                posy = 0
                
                textx = 16  #positions des lettres
                texty = 16
                k = 0
                x = 0
                y = 12

                #--------Caracteres sur clavier
                if symbol == 0:
                    for i in range(0,5):        
                        for k in range(x,y):
                            if k >= len(touches):break
                            if (k == 22 or k == 23 or k == 35 or k == 47 or k == 59):   #on ne dessine pas ce qu'il y a dans la case pour ne pas afficher les symboles non-necessaires
                                m = "Il ne se passe rien"
                            else:
                                text2 = fontcouleur.render(touches[k], True,black)     #ici on dessine les symboles des caracteres sur le clavier
                                screen.blit(text2,[textx,texty])
                                textx += 43
                        x += 12
                        y += 12
                        textx = 16
                        texty += 43
                        
                if symbol == 1:                     #meme logique de dessin des caracteres, mais avec les symboles
                    for i in range(0,5):        
                        for k in range(x,y):
                            if k >= len(symkeys):break
                            if (k == 22 or k == 23 or k == 35 or k == 47 or k == 59):
                                m = "Il ne se passe rien"
                            else:
                                text2 = fontcouleur.render(symkeys[k], True,black)
                                screen.blit(text2,[textx,texty])
                                textx += 43
                        x += 12
                        y += 12
                        textx = 16
                        texty += 43        

                pygame.display.flip()       #update l'image de la fenetre
                # --------------------------------- #
                clock.tick(refresh)             #refresh l'image 120x par seconde
        
        except IndexError:                  #gestion d'erreur si on clique dans la case de texte du clavier
            print "en dehors du clavier"

    return mode_ecran, Message,refresh, couleurclavier, couleurspace, couleurshift,couleurmaj,Message1,Message2,Message3,Message4,Message5,Message6,Message7,Message8
