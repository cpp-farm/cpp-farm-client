from config import config
from mqttClient import getClient 
import json
from loop import loop
from log import setupLogging
import sys

print('cpp-farm-client starting...')
print('command line args: %s' % sys.argv)
print('config: %s' % json.dumps(config))

setupLogging()

mqttClient = getClient(
  certificatePath = config['certificatePath'],
  endPoint = config['endPoint'],
  privateKeyPath = config['privateKeyPath'],
  rootCAPath = config['rootCAPath'],
  thingId = config['thingId'],
)

loop(
  mqttClient,
  topic = config['topic'],
)
