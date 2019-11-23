
"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

def WebRoute(method=None, routePath=None, name=None) :
	"""
	- method
	- routhPath
	- name
	"""
	...

def RegisterRoute(handler, method, routePath, name=None) :
	"""
	- handler
	- method
	- routhPath
	- name
	"""
	...

def ResolveRoute(method, path) :
	"""
	- method
	- path
	"""
	...

def PathFromRoute(routeName, routeArgs={ }) :
	"""
	- routeName
	- routeArgs
	"""
	...

class RouteResult :
    def __init__(self, regRoute, args=None) :
    	"""
    	- regRoute
    	- args
    	"""
    	...

    def __repr__(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Handler(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Method(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def RoutePath(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Name(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Args(self) :
    	"""
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
    	- handler
    	- method
    	- routePath
    	- name
    	- regex
    	- argNames
    	"""
    	...
