import logging

def setupLogging():
  logger = logging.getLogger("AWSIoTPythonSDK.core")
  logger.setLevel(logging.DEBUG)
  streamHandler = logging.StreamHandler()
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  streamHandler.setFormatter(formatter)
  logger.addHandler(streamHandler)
