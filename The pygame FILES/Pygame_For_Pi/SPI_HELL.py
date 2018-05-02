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

while(message==True):

    if(GPIO.input(22) == True):
        msg_status, pic_key = key_locking([0x60])

        if msg_status == True:        
            write_msg([[0xA1],[0xA4],[0xee],[0x04],[0x30],[0x31],[0x30],[0x30]])
            message=False            
        
    
        
    
    
