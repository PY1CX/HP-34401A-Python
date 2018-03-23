import DMM_34401a as dmm
import time

#Init the DMM with the Serial port
dmm0 = dmm.DMM_init("/dev/ttyUSB0")
while True:
    time.sleep(2)
    print(dmm.DMM_read(dmm0))



