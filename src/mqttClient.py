from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

myMQTTClient = None

def getClient(
  certificatePath,
  endPoint,
  privateKeyPath,
  rootCAPath,
  thingId,
):
  global myMQTTClient

  if myMQTTClient is None:
    _myMQTTClient = AWSIoTMQTTClient(thingId)
    _myMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
    _myMQTTClient.configureEndpoint(endPoint, 8883)

    _myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    _myMQTTClient.configureOfflinePublishQueueing(-1)
    _myMQTTClient.configureDrainingFrequency(2)
    _myMQTTClient.configureConnectDisconnectTimeout(10)
    _myMQTTClient.configureMQTTOperationTimeout(5)   

    _myMQTTClient.connect()
    myMQTTClient = _myMQTTClient 

    time.sleep(2)
    return myMQTTClient

  else:
    return myMQTTClient
