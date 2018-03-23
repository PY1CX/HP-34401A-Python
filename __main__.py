import DMM_34401a as dmm

#Init the DMM with the Serial port
dmm.__init__("/dev/ttyUSB0")

if dmm.DMM_ID_CHECK == 1:
    dmm.conf_SET_VOLT_DC_AUTO()
    print dmm.DMM_read()