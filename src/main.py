from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import datetime
import json
import os
from log import setupLogging
import time

setupLogging()

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
KEYS_PATH = os.path.join(ROOT_PATH, 'keys')
print('ROOT_PATH: %s\nKEYS_PATH: %s' % (ROOT_PATH, KEYS_PATH))

CERTIFICATE_PATH = os.path.join(KEYS_PATH, 'dfa63f42f6-certificate.pem.crt')
PRIVATE_KEY_PATH = os.path.join(KEYS_PATH, 'dfa63f42f6-private.pem.key')
ROOT_CA_PATH = os.path.join(KEYS_PATH, 'AmazonRootCA1.pem')

ENDPOINT = 'a1twx4zqllhsb2-ats.iot.us-west-2.amazonaws.com'
THING_ID = 'thing1'
TOPIC = 'cpp/sensor'

print('CERTIFICATE_PATH: %s\nPRIVATE_KEY_PATH: %s\nROOT_CA_PATH: %s' % (CERTIFICATE_PATH, PRIVATE_KEY_PATH, ROOT_CA_PATH))
print('ENDPOINT: %s\nTHING_ID: %s\nTOPIC: %s' % (ENDPOINT, THING_ID, TOPIC))

myMQTTClient = AWSIoTMQTTClient(THING_ID)
myMQTTClient.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERTIFICATE_PATH)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)

myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5) 

myMQTTClient.connect()
time.sleep(2)
loopCount = 0

while True:
  timestamp = int(round(time.time() * 1000))

  message = {}
  message['row'] = loopCount
  message['temperature'] = "12"
  message['timestamp'] = timestamp
  messageJson = json.dumps(message)

  myMQTTClient.publish(TOPIC, messageJson, 0)
  print('Published topic %s: %s\n' % (TOPIC, messageJson))
  loopCount += 1
  time.sleep(1)
