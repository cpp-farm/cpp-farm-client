#import bluetooth
import datetime
import serial
import os
#import RPi.GPIO as GPIO
#LED = 21

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, 0)

#Setup Variables
logging_rate = 1    #Logging rate in minutes
data = 0


#Define functions

#Send data
def send_data():
    index = 0
    time = ''
    latitude = ''
    longitude = ''
    time = time+data[index]
    while data[index] !='T':
        index = index + 1
        time = time + data[index]
    print('Time:' + time + ',')
    index = index + 1
    while data[index] != 'N':
        index = index + 1
        latitude = latitude + data[index]
    print('Latitude:' + latitude + ',')
    #Skip two characters to remove the comma and space
    index = index + 2
    while data[index] != 'W':
        index = index + 1
        longitude = longitude + data[index]
    #client_socket.send('longitude:' + '%s' %longitude + ', temperature:25')
    print('Longitude:' + longitude + ',')
    print('Temperature: 25')

#Setup Serial Communication
ser = serial.Serial('/dev/ttyACM0', 9600)

current_time = datetime.datetime.now()
last_minute = current_time.minute
last_second = current_time.second

while 1:
    #Compare current_time minute to last_minute.  If it is a new minute, send the timestamp and temperature
    current_time = datetime.datetime.now()

    #Read Serial Data
    data=ser.readline()
    if((current_time.second != last_second)):
    #if((current_time.minute != last_minute)):
        send_data()
        last_minute = current_time.minute
        last_second = current_time.second
        