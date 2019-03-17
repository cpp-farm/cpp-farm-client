import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
keyMap = ['lng', 'lat', 'tmp']

def getData():
  _data = ser.readline()
  data = _data.decode('UTF-8').rstrip()
  print('data received: %s' % data)
  
  parsed = parse(data)
  return parsed

def parse(str):
  split = str.split()
  formatted = {}

  for i in range(len(split)):
    formatted[keyMap[i]] = split[i]

  return formatted
