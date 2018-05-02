import RPi.GPIO as GPIO
import spidev
spi=spidev.SpiDev()
message=True
#--------------------------------Fonctions---------------------------------#
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN) #input pour le pull a la pin 22

    #SPI setup
    CLK = 40
    MISO = 35
    MOSI = 38
    CS = 36
   
    spi.open(1,2) #bus 1 device 0
    spi.max_speed_hz = 7629

def write_msg(msg):
    for current in range(len(msg)):
        readDummy = spi.xfer2(msg[current])
    
def receive():
    global readData
    for current in range(4):
        readData[current] = spi.xfer2([0x55])
    for current in range(readData[3]):
        readData[current+4] = spi.xfer2([0x55])
        return readData

def key_locking(master):    
    pic_key = spi.xfer2(master) #le pic renvoie A6 pour ecrire ou 06 pour lire
    if (pic_key[0] == 0xa6) or (pic_key[0] == 0x06):
        return True, pic_key
    else:
        return False, pic_key

#-------------------Programme principal------------------------------------#
init()  #initialisation des IO et du bus spi
you_got_mail=False
msg_status=False
envoie=True
done=False
msg_to_send=[[0xA1],[0xA4],[0xee],[0x04],[0x30],[0x31],[0x30],[0x30]]
Msg=[]
while done == False:        #on observe si la valeur de fin du programme est toujours a false avant de continuer
    if(GPIO.input(22) == True):     # Pin d'activation de la comm venant du PIC
        #spi.open(1,2)              # Activation Pi de son port spi
        #spi_actif = True           # Flag up
        
        if (envoi == False) or (envoi == None):         # Si on Envoie aucun message = Byte 6F sent
            msg_status, pic_is = key_locking([0x6F])    # Reception T or F du handshake, PIC status 

        elif envoi == True:                             #Si on envoie un message = Byte 60 sent
            msg_status,pic_is = key_locking([0x60])     #Reception du handshake et pic status
            envoi = False                               #Retour a false du flag apres single transmission

        if msg_status == True:                          #PI et PIC ont etabli une communication
            if pic_is[0] == 0xa6:                       #PIC veut parler
                Msg = receive()                         #Capture du message
                if Msg[2] == 0xEE:                      #Si message est un text
                    you_got_mail = True                 #Flag up for later purpose
                    boite_reception.append(Msg)         #List contenant message

                elif Msg[2] == 0xDD:                    #Si message est de l'information
                    pass    #TODO ajouter le reception de game data

            if pic_is[0] == 0x06:                       #PI veut parler
                write_msg(msg_to_send)                  #PI send message (Peut etre n'importe quel type de message)
                del msg_to_send[:]                      #CLEANSING
            done=True
        else:
            pass

    else:
        pass
        #if spi_actif == True:
        #    spi.close(1,2)

if you_got_mail == True:
    print boite_reception
        
    
    
