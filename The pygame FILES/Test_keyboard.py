import pygame

pygame.init()



# Define some colors
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

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
## ---------------------------Main loop----------------------------------


while running==True:
    #______________ALL EVENT PROCESSING BELOW THIS COMMENT_______________
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN and flag_up == 1:
            
            if event.key == pygame.K_UP:
                y_sensor -= 10
            elif event.key == pygame.K_DOWN:
                y_sensor += 10
            elif event.key == pygame.K_RIGHT:
                x_sensor += 10
            elif event.key == pygame.K_LEFT:
                x_sensor -= 10
            else:
                a = str(pygame.key.name(event.key))
                if a == "space":
                    a = " "
                    test= test + a
                elif a.isalpha():             
                    test= test + a
                    
            flag_up=0
            
        if event.type == pygame.KEYUP and flag_up == 0:
            flag_up = 1
        
    #____________________________________________________________________
            

            

    #______________ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT___________
            

    #____________________________________________________________________

            


    #______________ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT_________
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render(test, True, BLUE)
    pygame.draw.rect(screen, GREEN, [270,180,60 + x_sensor,30 + y_sensor], 1)
    screen.blit(text,[280,190]) 
    pygame.display.flip()
    #____________________________________________________________________

    
    #FRAME RATE______________DO NOT CHANGE VALUE_________________________
    clock.tick(20)

##----------------------------------END----------------------------------
pygame.quit()
