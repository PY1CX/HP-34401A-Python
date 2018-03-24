import DMM_34401a as dmm
import time

#Init the DMM with the Serial port
dmm0 = dmm.DMM_init("/dev/ttyUSB0")
f = open("data.txt", "a+")
time.sleep(1)
while True:
    time.sleep(2)
    x  = dmm.DMM_read_float(dmm0)
    f.write(str(x) + '\n')
    print(x)


