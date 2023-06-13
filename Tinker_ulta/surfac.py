import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pydirectinput
import pyautogui
ArduinoSerial = serial.Serial('COM3',9600) #Create Serial port objectcalled arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to getestablished
while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial dataand print it as line
    print (incoming)
    # pyautogui.write('Hello There', interval = 0.5)
    if 'up' in incoming:                     
        pyautogui.press('up')
    if 'left' in incoming:                         
        pyautogui.press('left',presses=1)
    if 'right' in incoming:                              
        pyautogui.press('right',presses=1)
    if 'down' in incoming:
        pyautogui.press('down')
    #      else: 
    #     pyau         t ogui.pr   ess('up',1)
    # i  f 'Forw ard' in incoming:                                                  
    #     pyautogui.hotkey( 'H') 