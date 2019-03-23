import serial

serialPort = 9600
keyMap = ['lng', 'lat', 'tmp']

def DataReader(
  serial = True,
):
  print('Data Reader is created with serial: %s' % serial)

  ser = None
  if serial == True:
    print('Serial is set True, reading at port: %s' % serialPort)
    ser = serial.Serial('/dev/ttyACM0', serialPort)

  def getData():
    global ser
    data = None

    if serial == True:
      _data = ser.readline()
      data = _data.decode('UTF-8').rstrip()
    else:
      data = '34.024581N -118.288116W 14C'

    print('data received: %s' % data)
    parsed = parse(data)
    return parsed  

  return {
    'getData': getData
  }

def parse(str):
  split = str.split()
  formatted = {}

  for i in range(len(split)):
    formatted[keyMap[i]] = split[i]

  return formatted
