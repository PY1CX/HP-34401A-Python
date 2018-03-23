import DMM_34401a as dmm
import time

#Init the DMM with the Serial port
dmm0 = dmm.DMM_init("/dev/ttyUSB0")
dmm.conf_SET_VOLT_DC_AUTO(dmm0)
#print(dmm.DMM_read(dmm0))
dmm.DMM_close(dmm0)


