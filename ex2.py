# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging

# CERTIFICATE_PATH = '/Users/mistock1706/work/cpp-farm/keys/dfa63f42f6-certificate.pem.crt'
CERTIFICATE_PATH = '/Users/mistock1706/work/cpp-farm/keys/t1.cert.pem'

ENDPOINT = 'a1twx4zqllhsb2-ats.iot.us-west-2.amazonaws.com'

# PRIVATE_KEY_PATH = '/Users/mistock1706/work/cpp-farm/keys/dfa63f42f6-private.pem.key'
PRIVATE_KEY_PATH = '/Users/mistock1706/work/cpp-farm/keys/t1.private.key'

# ROOT_CA_PATH = '/Users/mistock1706/work/cpp-farm/keys/AmazonRootCA1.pem'
ROOT_CA_PATH = '/Users/mistock1706/work/cpp-farm/keys/root-CA.crt'

# THING_ID = 'arn:aws:iot:us-west-2:451858119430:thing/CppFarm'
THING_ID = 'thing1'

logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient(THING_ID)
myMQTTClient.configureCredentials(ROOT_CA_PATH, PRIVATE_KEY_PATH, CERTIFICATE_PATH)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)

# # For Websocket connection
# # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# # Configurations
# # For TLS mutual authentication
# myMQTTClient.configureEndpoint(ENDPOINT, 8883)
# # For Websocket
# # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
# # For TLS mutual authentication with TLS ALPN extension
# # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)

# # For Websocket, we only need to configure the root CA
# # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
# myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
# myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
# myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
# myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()

message = {}
message['message'] = "1"
message['sequence'] = "2"
messageJson = json.dumps(message)

myMQTTClient.publish("power", messageJson, 0)
