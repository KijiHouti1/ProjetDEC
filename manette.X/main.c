/**
  Generated Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This is the main file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  Description:
    This header file provides implementations for driver APIs for all modules selected in the GUI.
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.65.2
        Device            :  PIC16F1508
        Driver Version    :  2.00
*/

/*
    (c) 2018 Microchip Technology Inc. and its subsidiaries. 
    
    Subject to your compliance with these terms, you may use Microchip software and any 
    derivatives exclusively with Microchip products. It is your responsibility to comply with third party 
    license terms applicable to your use of third party software (including open source software) that 
    may accompany Microchip software.
    
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY 
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS 
    FOR A PARTICULAR PURPOSE.
    
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP 
    HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO 
    THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL 
    CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT 
    OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS 
    SOFTWARE.
*/

#include "mcc_generated_files/mcc.h"

/*
                         Main application
 */
void main(void)
{
    // initialize the device
    SYSTEM_Initialize();
    char msg, master;
    bool msg_up=false;
    
    // When using interrupts, you need to set the Global and Peripheral Interrupt Enable bits
    // Use the following macros to:

    // Enable the Global Interrupts
    //INTERRUPT_GlobalInterruptEnable();

    // Enable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptEnable();

    // Disable the Global Interrupts
    //INTERRUPT_GlobalInterruptDisable();

    // Disable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptDisable();

    while (1)
    {
       int K_A=IO_RA2_GetValue();
       int K_EXTRA=IO_RB4_GetValue();
       int K_DWN=IO_RB6_GetValue();
       int K_LFT=IO_RC0_GetValue();
       int K_UP=IO_RC1_GetValue();
       int K_RIGHT=IO_RC2_GetValue();
       int K_B=IO_RC7_GetValue();
       
       
        master=EUSART_Read();
        if (master == 'w'){
            if (msg_up == true){
                EUSART_Write('1');
            }
            else if(msg_up == false){
                EUSART_Write('0');
            }
            EUSART_Write(msg);
            msg_up=false;
        }
       if(K_A==1){      //button A
           msg='A';
           msg_up=true;
           while (K_A == 1){
              K_A=IO_RA2_GetValue(); 
           }
           Red_SetHigh();
           green_SetLow();
           Blue_SetLow();
       }
       else if(K_EXTRA==1){      //BUTON EXTRA
           msg='X';
           msg_up=true;
           while (K_EXTRA == 1){
              K_EXTRA=IO_RB4_GetValue();
           }
           Red_SetLow();
           green_SetHigh();
           Blue_SetLow();
       }
       else if(K_DWN==1){      //button Down
           msg='D';
           msg_up=true;
           while (K_DWN == 1){
              K_DWN=IO_RB6_GetValue();
           }
           Red_SetLow();
           green_SetLow();
           Blue_SetHigh();
       }
       else if(K_LFT==1){      //Button left
           msg = 'L';
           msg_up=true;
           while (K_LFT == 1){
              K_LFT=IO_RC0_GetValue();
           }
           Red_SetLow();
           green_SetHigh();
           Blue_SetHigh(); 
       }
       else if(K_UP==1){      //button UP
           msg='U';
           msg_up=true;
           while (K_UP==1){
              K_UP=IO_RC1_GetValue();
           }
           Red_SetHigh();
           green_SetLow();
           Blue_SetHigh();
       }
       else if(K_RIGHT==1){      //BUTON Right
           msg='R';
           msg_up=true;
           while (K_RIGHT==1){
              K_RIGHT=IO_RC2_GetValue();
           }
           Red_SetLow();
           green_SetLow();
           Blue_SetLow();
       }
       else if(K_B==1){      //button b
           msg='B';
           msg_up=true;
           while (K_B==1){
              K_B=IO_RC7_GetValue();
           }
           Red_SetHigh();
           green_SetLow();
           Blue_SetLow();
       }
       else{
           EUSART_Write('0');
       }
    }
}
/**
 End of File
*/