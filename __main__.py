import DMM_34401a as dmm
print("Init")
#Init the DMM with the Serial port
dmm.__init__(self, "/dev/ttyUSB0")

#if dmm.DMM_ID_CHECK == 1:
#    dmm.conf_SET_VOLT_DC_AUTO()

#dmm.__close__()
    #print dmm.DMM_read()