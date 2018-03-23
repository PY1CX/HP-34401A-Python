# HP-34401A-Python
A driver written in Python for the HP 34401A (WORK IN PROGRESS)

Got it working, but still need to finish the driver!

### Tricks with the HP 34401a serial comm
1. I got a lot of time around the serial comm with the HP 34401a. Sometime this script will not work, set the baudrate in the multimeter again! It made my multimeter stop working with a undefined behavior.
2. Make sure you're not trying to get data faster than the multimeter does the acquisition
3. I don't know why but there is some bug with the pySerial library. The multimeter works with xonxoff and also dsrdtr, but the 34401a uses full serial flow control. 

### Output from READ? command
Output from READ? command is a scientific notation.

I still doesn't know if DMM_read will return a normalized string or if maybe I add a specific function for also a raw output.

Output example: +1.00010310E+01 (10.00103v)

