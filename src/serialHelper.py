import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def getData():
  data = ser.readline()
  return data
