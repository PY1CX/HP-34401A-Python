import serial
import time

""" 34401a Driver Class """

def __init__(self, port_number): 
    self.ser = serial.Serial(port = port_number,
                        baudrate = 9600,
                        parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_TWO,
                        bytesize = serial.EIGHTBITS,
                        xonxoff=True)
    self.ser.isOpen()
    time.sleep(0.5)
    self.ser.write("SYSTem:REMote".encode())
    print("Serial open") 
    self.close()

def __close__(self):
    self.ser.close()
    print("Serial Closed")

"""
ATTENTION:
Before trying to read or config anything in the DMM
you MUST send a SYSTem:REMote, so the DMM will start
accepting serial commands
"""

#Asks for identification and returns the serial data
def DMM_ID():
    ser.write("*IDN?\n".encode())
    return ser.read()
    
"""
Check if the connected DMM is the 34401A
"""
def DMM_ID_CHECK():
    ser.write("*IDN?\n".encode())
    s = ser.read()
    if s.find("34401A") == 1:
        return 1
    else:
        return 0

"""
Configuration functions
The following functions make a configuration into
the 34401A DMM. You should read after doing all
configs
"""
#Voltage DC - Range AUTO
def conf_SET_VOLT_DC_AUTO():
    ser.write("CONF:VOLT:DC AUTO\n".encode())
    
#Voltage AC - Range AUTO
def conf_SET_VOLT_AC_AUTO():
    ser.write("CONF:VOLT:AC AUTO\n".encode())   

"""
This function asks the DMM to send a single read
with the current configuration programmed into 
the 34401a
"""
def DMM_read():
    ser.write("READ?\n".encode())
    return ser.readline()
