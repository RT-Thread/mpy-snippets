"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class UrlUtils :
    @staticmethod
    def Quote(s, safe='/') :
    	"""
    	- safe
    	"""
    	...

    @staticmethod
    def UrlEncode(s) :
    	"""
    	- None
    	"""
    	...

    @staticmethod
    def Unquote(s) :
    	"""
    	- s
    	"""
    	...

    @staticmethod
    def UnquotePlus(s) :
    	"""
    	- s
    	"""
    	...

    class Url :
        def __init__(self, url='') :
        	"""
        	- url
        	"""
        	...

        def __repr__(self) :
        	"""
        	- None
        	"""
        	...

        def IsHttps(self) :
        	"""
        	- None
        	"""
        	...

        @property
        def URL(self) :
        	"""
        	- None
        	"""
        	...

        @URL.setter
        def URL(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def Proto(self) :
        	"""
        	- None
        	"""
        	...

        @Proto.setter
        def Proto(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def Host(self) :
        	"""
        	- None
        	"""
        	...
        
        @Host.setter
        def Host(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def Port(self) :
        	"""
        	- None
        	"""
        	...

        @Port.setter
        def Port(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def Path(self) :
        	"""
        	- None
        	"""
        	...

        @Path.setter
        def Path(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def QueryString(self) :
        	"""
        	- None
        	"""
        	...

        @QueryString.setter
        def QueryString(self, value) :
        	"""
        	- value
        	"""
        	...

        @property
        def QueryParams(self) :
        	"""
        	- None
        	"""
        	...

        @QueryParams.setter
        def QueryParams(self, value) :
        	"""
        	- value
        	"""
        	...
