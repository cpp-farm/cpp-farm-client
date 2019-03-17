from serialHelper import getData
import json
import time

loopCount = 0

def loop(
  myMQTTClient,
  topic,
):
  global loopCount

  while 1:
    timestamp = int(round(time.time() * 1000))

    message = {}
    message['row'] = loopCount
    message['temperature'] = "12"
    message['timestamp'] = timestamp
    messageJson = json.dumps(message)

    myMQTTClient.publish(topic, messageJson, 0)

    data = getData()
    print('data: %s' % data)

    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(1)
