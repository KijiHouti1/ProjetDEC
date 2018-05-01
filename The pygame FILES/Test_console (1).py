import pygame

pygame.init()



# Define some colors
#            R    G    B
GREY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

#Define size of screen
width= 700
height= 400
screen=pygame.display.set_mode([width,height])

#Global variable section
running=True

#Window parameter
pygame.display.set_caption("FIRST_TRY")
clock=pygame.time.Clock()

##---------------------Initial Variable----------------------------------

y_sensor=0
x_sensor=0
flag_up = 1
text=""
a = ""
test = ""
coord_x = 30
coord_y = -70
SQUARE1=RED
SQUARE2=GREEN
SQUARE3=RED
SQUARE4=GREEN
SQUARE5=GREEN
## ---------------------------Main loop----------------------------------


while running==True:
    #______________ALL EVENT PROCESSING BELOW THIS COMMENT_______________
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_sensor = -5
                flag_up = 0
            elif event.key == pygame.K_DOWN:
                y_sensor = 5
                flag_up = 0
            elif event.key == pygame.K_1:
                if SQUARE1 == GREEN:
                    SQUARE1=RED
                else:
                    SQUARE1=GREEN
            elif event.key == pygame.K_2:
                 if SQUARE2 == GREEN:
                    SQUARE2=RED
                 else:
                    SQUARE2=GREEN
            elif event.key == pygame.K_3:
                 if SQUARE3 == GREEN:
                    SQUARE3=RED
                 else:
                    SQUARE3=GREEN
            elif event.key == pygame.K_4:
                 if SQUARE4 == GREEN:
                    SQUARE4=RED
                 else:
                    SQUARE4=GREEN
            elif event.key == pygame.K_5:
                 if SQUARE5 == GREEN:
                    SQUARE5=RED
                 else:
                    SQUARE5=GREEN
            else:
                a = str(pygame.key.name(event.key))
                if a == "space":
                    a = " "
                    test= test + a
                elif a.isalpha():             
                    test= test + a
                    
            
        if event.type == pygame.KEYUP:
            flag_up = 1
        
    #____________________________________________________________________
            

            

    #______________ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT___________
    if flag_up == 0:
        #coord_x += x_sensor
        coord_y += y_sensor
        if coord_y == 5:
            coord_y = 0
        if coord_y == -75:
            coord_y = -70
    sizeP_x = 50
    sizeP_y = 50

    
    #____________________________________________________________________

            


    #______________ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT_________
    screen.fill(WHITE)
    font = pygame.font.Font(None, 32)
    text = font.render("Appuie sur les fleches", True, BLUE)
    pygame.draw.rect(screen, BLACK, [0,0,700,480])
    pygame.draw.rect(screen, GREY, [270,180,30,-70])
    pygame.draw.rect(screen, GREEN, [270,180,coord_x,coord_y])

    pygame.draw.rect(screen, GREY, [320,180,30,-70])
    pygame.draw.rect(screen, GREEN, [320,180,coord_x,coord_y])

    pygame.draw.rect(screen, GREY, [370,180,30,-70])
    pygame.draw.rect(screen, GREEN, [370,180,coord_x,coord_y])

    pygame.draw.rect(screen, GREY, [420,180,30,-70])
    pygame.draw.rect(screen, GREEN, [420,180,coord_x,coord_y])

    pygame.draw.rect(screen, GREY, [470,180,30,-70])
    pygame.draw.rect(screen, GREEN, [470,180,coord_x,coord_y])

    pygame.draw.rect(screen, SQUARE1, [270,90,15,15])
    pygame.draw.rect(screen, SQUARE2, [320,90,15,15])
    pygame.draw.rect(screen, SQUARE3, [370,90,15,15])
    pygame.draw.rect(screen, SQUARE4, [420,90,15,15])
    pygame.draw.rect(screen, SQUARE5, [470,90,15,15])

    
    screen.blit(text,[280,190]) 
    pygame.display.flip()
    #____________________________________________________________________

    
    #FRAME RATE______________DO NOT CHANGE VALUE_________________________
    clock.tick(20)

##----------------------------------END----------------------------------
pygame.quit()
