from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os
from log import setupLogging

setupLogging()

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
KEYS_PATH = os.path.join(ROOT_PATH, 'keys')
print('ROOT_PATH: %s\nKEYS_PATH: %s' % (ROOT_PATH, KEYS_PATH))

CERTIFICATE_PATH = os.path.join(KEYS_PATH, 'dfa63f42f6-certificate.pem.crt')
PRIVATE_KEY_PATH = os.path.join(KEYS_PATH, 'dfa63f42f6-private.pem.key')
ROOT_CA_PATH = os.path.join(KEYS_PATH, 'AmazonRootCA1.pem')

ENDPOINT = 'a1twx4zqllhsb2-ats.iot.us-west-2.amazonaws.com'
THING_ID = 'thing1'

print('CERTIFICATE_PATH: %s\nPRIVATE_KEY_PATH: %s\nROOT_CA_PATH: %s' % (CERTIFICATE_PATH, PRIVATE_KEY_PATH, ROOT_CA_PATH))
print('ENDPOINT: %s\nTHING_ID: %s' % (ENDPOINT, THING_ID))

myMQTTClient = AWSIoTMQTTClient(THING_ID)
myMQTTClient.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERTIFICATE_PATH)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)

myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5) 

myMQTTClient.connect()

# message = {}
# message['message'] = "1"
# message['sequence'] = "2"
# messageJson = json.dumps(message)

# myMQTTClient.publish("power", messageJson, 0)
