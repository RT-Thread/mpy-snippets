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
    	- microWebSrv2
    	- xasCli
    	"""
    	...

    def _recvLine(self, onRecv) :
    	"""
    	- onRecv
    	"""
    	...

    def _waitForRecvRequest(self) :
    	"""
    	- None
    	"""
    	...

    def _onFirstLineRecv(self, xasCli, line, arg) :
    	"""
    	- xasCli
    	- line
    	- arg
    	"""
    	...

    def _onHeaderLineRecv(self, xasCli, line, arg) :
    	"""
    	- xasCli
    	- line
    	- arg
    	"""
    	...

    def _processRequest(self) :
    	"""
    	- None
    	"""
    	...

    def _processRequestModules(self) :
    	"""
    	- None
    	"""
    	...

    def _processRequestRoutes(self) :
    	"""
    	- None
    	"""
    	...

    def _routeRequest(self) :
    	"""
    	- None
    	"""
    	...

    def GetPostedURLEncodedForm(self) :
    	"""
    	- None
    	"""
    	...

    def GetPostedJSONObject(self) :
    	"""
    	- None
    	"""
    	...

    def GetHeader(self, name) :
    	"""
    	- name
    	"""
    	...

    def CheckBasicAuth(self, username, password) :
    	"""
    	- username
    	- password
    	"""
    	...

    def CheckBearerAuth(self, token) :
    	"""
    	- token
    	"""
    	...

    @property
    def UserAddress(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def IsSSL(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def HttpVer(self) :
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
    def Path(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def QueryString(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def QueryParams(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Host(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Accept(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def AcceptEncodings(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def AcceptLanguages(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Cookies(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def CacheControl(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Referer(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def ContentType(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def ContentLength(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def UserAgent(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Authorization(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Origin(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def IsKeepAlive(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def IsUpgrade(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Upgrade(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Content(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Response(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def XAsyncTCPClient(self) :
    	"""
    	- None
    	"""
    	...
