from config import config
import json
from mqttClient import getClient 
from log import setupLogging
from loop import loop

print('cpp-farm-client starting...')
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
