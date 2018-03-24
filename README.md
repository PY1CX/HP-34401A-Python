# HP-34401A-Python
This is a simple driver (but with nice features) to read data from the HP 34401A multimeter.

## What this driver offers?

* A simple API with raw output in scientifc notation and float output
* You can plug more than one multimeter
* The serial is already configured and YES it works more stable with xonxoff instead of hardware flow control. It's a bug in the pySerial library
* Works in Python 2.7 and Python 3.X

## What's to be implemented in the future?

* Config the 34401A via the Python Script

## How to use this driver?

You need to import the DMM_34401a.py file with:

```import DMM_34401a as dmm```

Them you init your multimeter and store a handler, like the next line, the handler in this case is dmm0, and everytime you want to do anything with this multimeter you MUST use this "handler". Inside the DMM_init function you just need to pass the serial port you're going to use.

```dmm0 = dmm.DMM_init("/dev/ttyUSB0")```

Now you wanna read something from your multimeter, you got two options:

```DMM_float(handler) ```
```DMM_float(handler) ```

## Output from READ? command
The raw output from READ? command is a scientific notation.

I implemented two functions so you can choose between raw reading or a float value.
* RAW OUTPUT  : +1.00010310E+01
* FLOAT OUTPUT: 10.0010310

## Tricks with the HP 34401a serial comm
1. I spent a lot of time testing the serial port with the HP 34401a. Sometime this script will not work, go into the menu in your 34401a and set the baudrate again! 
2. Make sure you're not trying to get data faster than the multimeter does the acquisition ( 6 digit FAST, 6 digit SLOW, etc in the config of the multimeter)
3. I don't know why but there is some bug with the pySerial library. The driver works with xonxoff and also dsrdtr (but it's not stalbe enough), the problem is the 34401a uses full serial flow control. 

