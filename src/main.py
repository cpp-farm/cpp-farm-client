from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from config import config
import datetime
import json
from mqttClient import getClient 
import os
from log import setupLogging
import time

print('cpp-farm-client starting...')
print('config: %s' % json.dumps(config))

setupLogging()

myMQTTClient = getClient(
  certificatePath = config['certificatePath'],
  endPoint = config['endPoint'],
  privateKeyPath = config['privateKeyPath'],
  rootCAPath = config['rootCAPath'],
  thingId = config['thingId'],
)

time.sleep(2)
loopCount = 0

while 1:
  timestamp = int(round(time.time() * 1000))

  message = {}
  message['row'] = loopCount
  message['temperature'] = "12"
  message['timestamp'] = timestamp
  messageJson = json.dumps(message)

  myMQTTClient.publish(config['topic'], messageJson, 0)
  print('Published topic %s: %s\n' % (config['topic'], messageJson))
  loopCount += 1
  time.sleep(1)
