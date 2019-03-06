import boto3
import datetime
import os
import serial

logging_rate = 1 # Logging rate in minutes
data = 0

def send_data():
  index = 0
  time = ''
  latitude = ''
  longitude = ''
  time = time + data[index]

  while data[index] != 'T':
    index = index + 1
    time = time + data[index]

    print('Time:' + time + ',')
    index = index + 1

    while data[index] != 'N':
      index = index + 1
      latitude = latitude + data[index]

    print('Latitude:' + latitude + ',')

    # Skip two characters to remove the comma and space
    index = index + 2
    while data[index] != 'W':
      index = index + 1
      longitude = longitude + data[index]
    # client_socket.send('longitude:' + '%s' %longitude + ', temperature:25')
    print('Longitude:' + longitude + ',')
    print('Temperature: 25')

# Setup Serial Communication
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


dynamodb = boto3.resource(
  aws_access_key_id='AKIAIHPDN42GF4NTZUGQ',
  aws_secret_access_key='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',
  region_name='us-west-1',
  service_name='dynamodb'
)

table = dynamodb.Table('cpp-farm-003')

print(table.creation_date_time)

table.put_item(
  Item={
    'id': '3',
    'lat': 2,
    'lng': 3,
    'time': '2019-02-22',
  }
)

response = table.get_item(
  Key={
    'id': '2'
  }
)

item = response['Item']
print(item)
