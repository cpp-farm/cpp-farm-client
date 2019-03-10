import datetime
import serial
import os
import dht11
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

logging_rate = 1  # Logging rate in minutes
data = 0

def create_payload(temperature):
  index = 0
  time = ''
  latitude = ''
  longitude = ''
  time = time+data[index]
  while data[index] != 'T':
      index = index + 1
      time = time + data[index]
  index = index + 1
  while data[index] != 'N':
      index = index + 1
      latitude = latitude + data[index]

  # Skip two characters to remove the comma and space
  index = index + 2
  while data[index] != 'W':
      index = index + 1
      longitude = longitude + data[index]

  payload = {"Time": "' + time + '", "Latitude": "' + latitude + '",
              "Longitude": "' + longitude '", "Temperature": "' + temperature '"}
  print('payload: %s' % (payload))

  return payload

ser = serial.Serial('/dev/ttyACM0', 9600)

current_time = datetime.datetime.now()
last_minute = current_time.minute
last_second = current_time.second
loopCount = 0

while 1:
  print('count: %s' % (loopCount))
  # Compare current_time minute to last_minute.  If it is a new minute, send the timestamp and temperature
  current_time = datetime.datetime.now()

  # Get temperature data
  instance = dht11.DHT11(pin=4)  # BCM GPIO04
  result = instance.read()

  # Read Serial Data
  data = ser.readline()

  if ((current_time.second != last_second)):
    print('data in line: %s' % (data))
    # payload = create_payload(str(result.temperature))
    # last_minute = current_time.minute
    # last_second = current_time.second
