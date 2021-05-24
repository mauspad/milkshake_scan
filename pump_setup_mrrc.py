#Import stuff
from psychopy import visual, core, event 
import serial, time

#Set pump diameter
diameter=26.59
mls=.5
rate=15

#Open first serial port
ser = serial.Serial(port='COM3', baudrate=19200, bytesize=8) ###PORT IS DIFFERENT BETWEEN MOCK AND MRRC GUSTOMETER###

#PySerial recommends a wait after port is opened
#Relatedly: The time.sleep waits later on are for the pump-- it can't read as fast as comp can send
time.sleep(1) 

#Check which port was really used
print(ser.name)

for pump in range(0,4):
    print(pump)
    
    #Set pump diameter
    ser.write(("%ddia%d\r" % (pump, diameter)).encode())
    time.sleep(0.2)
    
    #set up the 4 phases of infusion
    #In the first phase we quickly infuse what was withdrawn -- these values don't change
    ser.write(("%dphn01\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%dfunrat\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%drat15mm" % pump).encode())
    time.sleep(0.2)
    ser.write(("%dvol.3\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%ddirinf\r" % pump).encode())
    time.sleep(0.2)
    
    #In the second phase with infuse what out participant is actually getting -- set these values above
    ser.write(("%dphn02\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%dfunrat\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%drat%dmm" % (pump, rate)).encode())
    time.sleep(0.2)
    ser.write(("%dvol%d\r" % (pump, mls)).encode())
    time.sleep(0.2)
    ser.write(("%ddirinf\r" % pump).encode())
    
    #In the third phase we withdraw some solution
    time.sleep(0.2)
    ser.write(("%dphn03\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%dfunrat\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%drat15mm" % pump).encode())
    time.sleep(0.2)
    ser.write(("%dvol.3\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%ddirwdr\r" % pump).encode())
    time.sleep(0.2)
    
    #In the fourth phase we stop
    ser.write(("%dphn04\r" % pump).encode())
    time.sleep(0.2)
    ser.write(("%funstp\r" % pump).encode())
    time.sleep(0.2)
    
    #this is the command that triggers pumps!
    #ser.write(("%drun\r" % pump).encode())
ser.close()