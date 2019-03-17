from serialize import getData
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
    print('parsed data: %s' % data)

    timestamp = int(round(time.time() * 1000))

    message = {}
    message['row'] = loopCount
    message['timestamp'] = timestamp
    message['data'] = data
    messageJson = json.dumps(message)

    myMQTTClient.publish(topic, messageJson, 0)
    loopCount += 1

    print('Published topic %s: %s\n' % (topic, messageJson))
    time.sleep(1)
