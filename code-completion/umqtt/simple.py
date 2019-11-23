class MQTTException(Exception):
	"""
	"""
	...

class MQTTClient:
	def __init__(self, client_id, server, port=0, user=None, password=None, keeyalive=0, ssl=False, ssl_params={}):
		"""
		Create a mqtt client object.

		- client_id:
		- server:
		- port:
		- user:
		- password:
		- keeyalive:
		- ssl:
		- ssl_params:
		"""
		...

	def connect(self, clean_session=True):
		"""
		Connect to mqtt server.

		- clean_session:
		"""
		...

	def set_callback(self, f):
		"""
		"""
		...

	def set_last_will(self, topic, msg, retain=False, qos=0):
		"""
		- topic:
		- msg:
		- retain:
		- qos:
		"""
		...

	def disconnect(self):
		"""
		Disconnect from mqtt server.
		"""
		...

	def ping(self):
		"""
		Send ping to mqtt server.
		"""
		...

	def publish(self, topic, msg, retain=False, qos=0):
		"""
		- topic:
		- msg:
		- retain:
		- qos:
		"""
		...

	def subscribe(self, topic, qos=0):
		"""
		- topic:
		- qos:
		"""
		...

	def wait_msg(self):
		"""
		Wait for message, socket blocked
		"""
		...

	def check_msg(self):
		"""
		Check message, socket none blocked
		"""
		...
