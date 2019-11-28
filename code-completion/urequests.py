class Response:
	def __init__(self, raw):
		"""
		Initialize object

		- None
		"""
		...

	def close(self):
		"""
		Close

		- None
		"""
		...

	def content(self):
		"""
		Content
		
		- None
		"""
		...

	def text(self):
		"""
		Text

		- None
		"""
		...

	def json(self):
		"""
		Json

		- None
		"""
		...


def request(method, url, data=None, json=None, headers={}, stream=None, timeout=None):
	"""
	Request

	- method
	- url
	- data
	- json
	- headers
	- stream
	"""
	...


def head(url, **kw):
	"""
	Head

	- url
	- **kw
	"""
	...

def get(url, **kw):
	"""
	Get

	- url
	- **kw
	"""
	...

def post(url, **kw):
	"""
	Post

	- url
	- **kw
	"""
	...

def put(url, **kw):
	"""
	Put

	- url
	- **kw
	"""
	...

def patch(url, **kw):
	"""
	Patch

	- url
	- **kw
	"""
	...

def delete(url, **kw):
	"""
	Delete

	- url
	- **kw
	"""
	...
