from readData import getData
import json
import time

loopCount = 0

def loop(
  myMQTTClient,
  topic,
):
  global loopCount

  while 1:
    data = getData()
    timestamp = int(round(time.time() * 1000))

    message = {}
    message['row'] = loopCount
    message['timestamp'] = timestamp
    message['data'] = data
    messageJson = json.dumps(message)

    myMQTTClient.publish(topic, messageJson, 0)

    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(1)
