import serial
import time

""" 34401a Driver Class """

def DMM_init(port_number): 
    ser = serial.Serial(port = port_number,
                        baudrate = 9600,
                        parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_TWO,
                        bytesize = serial.EIGHTBITS,
                        xonxoff=True)
    time.sleep(0.5)
    if ser.isOpen() == True:
        ser.write("SYSTem:REMote\n".encode())
        print("Serial open")
        return ser #Return ser as a handler
    else:
        return False   

def DMM_close(self):
    self.close()
    print("Serial Closed")

"""
ATTENTION:
Before trying to read or config anything in the DMM
you MUST send a SYSTem:REMote, so the DMM will start
accepting serial commands
"""

#Asks for identification and returns the serial data
def DMM_ID(self):
    print("Arrived here")
    self.write("*IDN?\n".encode())
    print(self.readline().encode())
    
"""
Check if the connected DMM is the 34401A
"""
def DMM_ID_CHECK(self):
    self.write("*IDN?\n".encode())
    s = self.readline()
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
def conf_SET_VOLT_DC_AUTO(self):
    self.write("CONF:VOLT:DC AUTO\n".encode())
    
#Voltage AC - Range AUTO
def conf_SET_VOLT_AC_AUTO(self):
    self.write("CONF:VOLT:AC AUTO\n".encode())   

"""
This function asks the DMM to send a single read
with the current configuration programmed into 
the 34401a
"""
def DMM_read(self):
    self.write("READ?\n".encode())
    return self.read()
