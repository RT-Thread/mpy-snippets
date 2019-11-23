"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class HttpResponse :
    _RESPONSE_CODES = ...

    _CODE_CONTENT_TMPL = ...

    def __init__(self, microWebSrv2, request) :
    	"""
    	- microWebSrv2
    	- request
    	"""
    	...

    def SetHeader(self, name, value) :
    	"""
    	- name
    	- value
    	"""
    	...

    def _onDataSent(self, xasCli, arg) :
    	"""
    	- xasCli
    	- arg
    	"""
    	...

    def _onClosed(self, xasCli, closedReason) :
    	"""
    	- xasCli
    	- closedReason
    	"""
    	...

    def _makeBaseResponseHdr(self, code) :
    	"""
    	- code
    	"""
    	...

    def _makeResponseHdr(self, code) :
    	"""
    	- code
    	"""
    	...

    def SwitchingProtocols(self, upgrade) :
    	"""
    	- upgrade
    	"""
    	...

    def ReturnStream(self, code, stream) :
    	"""
    	- code
    	- stream
    	"""
    	...

    def Return(self, code, content=None) :
    	"""
    	- code
    	- content
    	"""
    	...

    def ReturnJSON(self, code, obj) :
    	"""
    	- code
    	- obj
    	"""
    	...

    def ReturnOk(self, content=None) :
    	"""
    	- content
    	"""
    	...

    def ReturnOkJSON(self, obj) :
    	"""
    	- obj
    	"""
    	...

    def ReturnFile(self, filename, attachmentName=None) :
    	"""
    	- filename
    	- attachmentName
    	"""
    	...

    def ReturnNotModified(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnRedirect(self, location) :
    	"""
    	- location
    	"""
    	...

    def ReturnBadRequest(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnUnauthorized(self, typeName, realm=None) :
    	"""
    	- typeName
    	- realm
    	"""
    	...

    def ReturnForbidden(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnNotFound(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnMethodNotAllowed(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnEntityTooLarge(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnInternalServerError(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnNotImplemented(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnServiceUnavailable(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnBasicAuthRequired(self) :
    	"""
    	- None
    	"""
    	...

    def ReturnBearerAuthRequired(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Request(self) :
    	"""
    	- None
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
    def AllowCaching(self) :
    	"""
    	- None
    	"""
    	...

    @AllowCaching.setter
    def AllowCaching(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def ContentType(self) :
    	"""
    	- None
    	"""
    	...

    @ContentType.setter
    def ContentType(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def ContentCharset(self) :
    	"""
    	- None
    	"""
    	...

    @ContentCharset.setter
    def ContentCharset(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def ContentLength(self) :
    	"""
    	- None
    	"""
    	...

    @ContentLength.setter
    def ContentLength(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def HeadersSent(self) :
    	"""
    	- None
    	"""
    	...
