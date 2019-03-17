import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

config = {
  'certificatePath': os.path.join(ROOT_PATH, 'keys', 'dfa63f42f6-certificate.pem.crt'),
  'endPoint': 'a1twx4zqllhsb2-ats.iot.us-west-2.amazonaws.com',
  'keysPath': os.path.join(ROOT_PATH, 'keys'),
  'privateKeyPath': os.path.join(ROOT_PATH, 'keys', 'dfa63f42f6-private.pem.key'),
  'rootCAPath': os.path.join(ROOT_PATH, 'keys', 'AmazonRootCA1.pem'),
  'rootPath': ROOT_PATH,
  'thingId': 'thing1',
  'topic': 'cpp/sensor',
}
