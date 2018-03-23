from serial import serial

class DMM34401a:
    """ 34401a Driver Class """
    def __init__(self): 
        ser = serial.Serial(port = "/dev/ttyUSB0",
                            baudrate = 9600,
                            parity = serial.PARITY_NONE,
                            stopbits = serial.STOPBITS_TWO,
                            bytesize = serial.EIGHTBITS)
        ser.isOpen()

    """
    ATTENTION:
    Before trying to read or config anything in the DMM
    you MUST send a SYSTem:REMote, so the DMM will start
    accepting serial commands
    """
    def start:
        ser.write("SYSTem:REMote")


    #Asks for identification and returns the serial data
    def DMM_ID:
        ser.write("*IDN?")
        return ser.read()
    
    #Check if the connected DMM is the 34401A
    def DMM_ID_CHECK:
        ser.write("*IDN?")
        s = ser.read()
        if s.find("34401A") == 1:
            return TRUE
        else:
            return FALSE
    


    """
    Configuration functions
    The following functions make a configuration into
    the 34401A DMM. You should read after doing all
    configs
    """
    #Voltage DC - Range AUTO
    def conf_SET_VOLT_DC_AUTO(self):
        ser.write("CONF:VOLT:DC AUTO")
    
    #Voltage AC - Range AUTO
    def conf_SET_VOLT_AC_AUTO(self):
        ser.write("CONF:VOLT:AC AUTO")   



    """
    This function asks the DMM to send a single read
    with the current configuration programmed into 
    the 34401a
    """
    def DMM_read(self):
        ser.write("READ?")
        return ser.readline()
