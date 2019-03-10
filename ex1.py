from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json

AllowedActions = ['both', 'publish', 'subscribe']

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# Read in command-line parameters
# parser = argparse.ArgumentParser()
# parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
# parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
# parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
# parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")
# parser.add_argument("-p", "--port", action="store", dest="port", type=int, help="Port number override")
# parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket", default=False,
#                     help="Use MQTT over WebSocket")
# parser.add_argument("-id", "--clientId", action="store", dest="clientId", default="basicPubSub",
#                     help="Targeted client id")
# parser.add_argument("-t", "--topic", action="store", dest="topic", default="sdk/test/Python", help="Targeted topic")
# parser.add_argument("-m", "--mode", action="store", dest="mode", default="both",
#                     help="Operation modes: %s"%str(AllowedActions))
# parser.add_argument("-M", "--message", action="store", dest="message", default="Hello World!",
#                     help="Message to publish")

# args = parser.parse_args()
# host = args.host
host = 'a1twx4zqllhsb2-ats.iot.us-west-2.amazonaws.com'

keyRootPath = '/Users/mistock1706/work/cpp-farm/keys'
rootCAPath = keyRootPath + '/root-ca.pem'
certificatePath = keyRootPath + '/8fefac97de-certificate.pem.crt'
privateKeyPath = keyRootPath  + '/8fefac97de-private.pem.key'
port = 8883
clientId = 'arn:aws:iot:us-west-2:451858119430:thing/CppFarm'
topic = 'my/greenhouse'

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
# if args.mode == 'both' or args.mode == 'subscribe':
#     myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
while True:
  message = {}
  message['message'] = args.message
  message['sequence'] = loopCount
  messageJson = json.dumps(message)
  myAWSIoTMQTTClient.publish(topic, messageJson, 1)

  print('Published topic %s: %s\n' % (topic, messageJson))
  loopCount += 1
  time.sleep(1)
