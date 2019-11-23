"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class UrlUtils :
    @staticmethod
    def Quote(s, safe='/') :
    	"""
    	Quote
    	
    	- safe
    	"""
    	...

    @staticmethod
    def UrlEncode(s) :
    	"""
    	UrlEncode
    	
    	- None
    	"""
    	...

    @staticmethod
    def Unquote(s) :
    	"""
    	Unquote
    	
    	- s
    	"""
    	...

    @staticmethod
    def UnquotePlus(s) :
    	"""
    	UnquotePlus
    	
    	- s
    	"""
    	...

    class Url :
        def __init__(self, url='') :
        	"""
        	__init__
        	
        	- url
        	"""
        	...

        def __repr__(self) :
        	"""
        	__repr__
        	
        	- None
        	"""
        	...

        def IsHttps(self) :
        	"""
        	IsHttps
        	
        	- None
        	"""
        	...

        @property
        def URL(self) :
        	"""
        	URL
        	
        	- None
        	"""
        	...

        @URL.setter
        def URL(self, value) :
        	"""
        	URL
        	
        	- value
        	"""
        	...

        @property
        def Proto(self) :
        	"""
        	Proto
        	
        	- None
        	"""
        	...

        @Proto.setter
        def Proto(self, value) :
        	"""
        	Proto
        	
        	- value
        	"""
        	...

        @property
        def Host(self) :
        	"""
        	Host
        	
        	- None
        	"""
        	...
        
        @Host.setter
        def Host(self, value) :
        	"""
        	Host
        	
        	- value
        	"""
        	...

        @property
        def Port(self) :
        	"""
        	Port
        	
        	- None
        	"""
        	...

        @Port.setter
        def Port(self, value) :
        	"""
        	Port
        	
        	- value
        	"""
        	...

        @property
        def Path(self) :
        	"""
        	Path
        	
        	- None
        	"""
        	...

        @Path.setter
        def Path(self, value) :
        	"""
        	Path
        	
        	- value
        	"""
        	...

        @property
        def QueryString(self) :
        	"""
        	QueryString
        	
        	- None
        	"""
        	...

        @QueryString.setter
        def QueryString(self, value) :
        	"""
        	QueryString
        	
        	- value
        	"""
        	...

        @property
        def QueryParams(self) :
        	"""
        	QueryParams
        	
        	- None
        	"""
        	...

        @QueryParams.setter
        def QueryParams(self, value) :
        	"""
        	QueryParams
        	
        	- value
        	"""
        	...
