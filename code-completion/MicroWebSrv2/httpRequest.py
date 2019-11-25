"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

from   .              import *
from   .httpResponse  import HttpResponse

class HttpRequest :
    MAX_RECV_HEADER_LINES = ...

    def __init__(self, microWebSrv2, xasCli) :
    	"""
    	__init__
    	
    	- microWebSrv2
    	- xasCli
    	"""
    	...

    def _recvLine(self, onRecv) :
    	"""
    	_recvLine
    	
    	- onRecv
    	"""
    	...

    def _waitForRecvRequest(self) :
    	"""
    	_waitForRecvRequest
    	
    	- None
    	"""
    	...

    def _onFirstLineRecv(self, xasCli, line, arg) :
    	"""
    	_onFirstLineRecv
    	
    	- xasCli
    	- line
    	- arg
    	"""
    	...

    def _onHeaderLineRecv(self, xasCli, line, arg) :
    	"""
    	_onHeaderLineRecv
    	
    	- xasCli
    	- line
    	- arg
    	"""
    	...

    def _processRequest(self) :
    	"""
    	_processRequest
    	
    	- None
    	"""
    	...

    def _processRequestModules(self) :
    	"""
    	_processRequestModules
    	
    	- None
    	"""
    	...

    def _processRequestRoutes(self) :
    	"""
    	_processRequestRoutes
    	
    	- None
    	"""
    	...

    def _routeRequest(self) :
    	"""
    	_routeRequest
    	
    	- None
    	"""
    	...

    def GetPostedURLEncodedForm(self) :
    	"""
    	GetPostedURLEncodedForm
    	
    	- None
    	"""
    	...

    def GetPostedJSONObject(self) :
    	"""
    	GetPostedJSONObject
    	
    	- None
    	"""
    	...

    def GetHeader(self, name) :
    	"""
    	GetHeader
    	
    	- name
    	"""
    	...

    def CheckBasicAuth(self, username, password) :
    	"""
    	CheckBasicAuth
    	
    	- username
    	- password
    	"""
    	...

    def CheckBearerAuth(self, token) :
    	"""
    	CheckBearerAuth
    	
    	- token
    	"""
    	...

    @property
    def UserAddress(self) :
    	"""
    	UserAddress
    	
    	- None
    	"""
    	...

    @property
    def IsSSL(self) :
    	"""
    	IsSSL
    	
    	- None
    	"""
    	...

    @property
    def HttpVer(self) :
    	"""
    	HttpVer
    	
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
    def Path(self) :
    	"""
    	Path
    	
    	- None
    	"""
    	...

    @property
    def QueryString(self) :
    	"""
    	QueryString
    	
    	- None
    	"""
    	...

    @property
    def QueryParams(self) :
    	"""
    	QueryParams
    	
    	- None
    	"""
    	...

    @property
    def Host(self) :
    	"""
    	Host
    	
    	- None
    	"""
    	...

    @property
    def Accept(self) :
    	"""
    	Accept
    	
    	- None
    	"""
    	...

    @property
    def AcceptEncodings(self) :
    	"""
    	AcceptEncodings
    	
    	- None
    	"""
    	...

    @property
    def AcceptLanguages(self) :
    	"""
    	AcceptLanguages
    	
    	- None
    	"""
    	...

    @property
    def Cookies(self) :
    	"""
    	Cookies
    	
    	- None
    	"""
    	...

    @property
    def CacheControl(self) :
    	"""
    	CacheControl
    	
    	- None
    	"""
    	...

    @property
    def Referer(self) :
    	"""
    	Referer
    	
    	- None
    	"""
    	...

    @property
    def ContentType(self) :
    	"""
    	ContentType
    	
    	- None
    	"""
    	...

    @property
    def ContentLength(self) :
    	"""
    	ContentLength
    	
    	- None
    	"""
    	...

    @property
    def UserAgent(self) :
    	"""
    	UserAgent
    	
    	- None
    	"""
    	...

    @property
    def Authorization(self) :
    	"""
    	Authorization
    	
    	- None
    	"""
    	...

    @property
    def Origin(self) :
    	"""
    	Origin
    	
    	- None
    	"""
    	...

    @property
    def IsKeepAlive(self) :
    	"""
    	IsKeepAlive
    	
    	- None
    	"""
    	...

    @property
    def IsUpgrade(self) :
    	"""
    	IsUpgrade
    	
    	- None
    	"""
    	...

    @property
    def Upgrade(self) :
    	"""
    	Upgrade
    	
    	- None
    	"""
    	...

    @property
    def Content(self) :
    	"""
    	Content
    	
    	- None
    	"""
    	...

    @property
    def Response(self) :
    	"""
    	Response
    	
    	- None
    	"""
    	...

    @property
    def XAsyncTCPClient(self) :
    	"""
    	XAsyncTCPClient
    	
    	- None
    	"""
    	...
