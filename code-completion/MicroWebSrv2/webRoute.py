
"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

def WebRoute(method=None, routePath=None, name=None) :
	"""
	WebRoute
	
	- method
	- routhPath
	- name
	"""
	...

def RegisterRoute(handler, method, routePath, name=None) :
	"""
	RegisterRoute
	
	- handler
	- method
	- routhPath
	- name
	"""
	...

def ResolveRoute(method, path) :
	"""
	ResolveRoute
	
	- method
	- path
	"""
	...

def PathFromRoute(routeName, routeArgs={ }) :
	"""
	PathFromRoute
	
	- routeName
	- routeArgs
	"""
	...

class RouteResult :
    def __init__(self, regRoute, args=None) :
    	"""
    	__init__
    	
    	- regRoute
    	- args
    	"""
    	...

    def __repr__(self) :
    	"""
    	__repr__
    	
    	- None
    	"""
    	...

    @property
    def Handler(self) :
    	"""
    	Handler
    	
    	- None
    	"""
    	...

    @property
    def Method(self) :
    	"""
    	Method
    	
    	- None
    	"""
    	...

    @property
    def RoutePath(self) :
    	"""
    	RoutePath
    	
    	- None
    	"""
    	...

    @property
    def Name(self) :
    	"""
    	Name
    	
    	- None
    	"""
    	...

    @property
    def Args(self) :
    	"""
    	Args
    	
    	- None
    	"""
    	...

GET     = ...
HEAD    = ...
POST    = ...
PUT     = ...
DELETE  = ...
OPTIONS = ...
PATCH   = ...

_registeredRoutes = ...


class _registeredRoute :
    def __init__(self, handler, method, routePath, name, regex, argNames) :
    	"""
    	__init__
    	
    	- handler
    	- method
    	- routePath
    	- name
    	- regex
    	- argNames
    	"""
    	...
