"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class HttpResponse :
	_RESPONSE_CODES = ...
	_CODE_CONTENT_TMPL = ...

	def __init__(self, microWebSrv2, request) :
		"""
		__init__
		
		- microWebSrv2
		- request
		"""
		...

	def SetHeader(self, name, value) :
		"""
		SetHeader
		
		- name
		- value
		"""
		...

	def _onDataSent(self, xasCli, arg) :
		"""
		_onDataSent
		
		- xasCli
		- arg
		"""
		...

	def _onClosed(self, xasCli, closedReason) :
		"""
		_onClosed
		
		- xasCli
		- closedReason
		"""
		...

	def _makeBaseResponseHdr(self, code) :
		"""
		_makeBaseResponseHdr
		
		- code
		"""
		...

	def _makeResponseHdr(self, code) :
		"""
		_makeResponseHdr
		
		- code
		"""
		...

	def SwitchingProtocols(self, upgrade) :
		"""
		SwitchingProtocols
		
		- upgrade
		"""
		...

	def ReturnStream(self, code, stream) :
		"""
		ReturnStream
		
		- code
		- stream
		"""
		...

	def Return(self, code, content=None) :
		"""
		Return
		
		- code
		- content
		"""
		...

	def ReturnJSON(self, code, obj) :
		"""
		ReturnJSON
		
		- code
		- obj
		"""
		...

	def ReturnOk(self, content=None) :
		"""
		ReturnOk
		
		- content
		"""
		...

	def ReturnOkJSON(self, obj) :
		"""
		ReturnOkJSON
		
		- obj
		"""
		...

	def ReturnFile(self, filename, attachmentName=None) :
		"""
		ReturnFile
		
		- filename
		- attachmentName
		"""
		...

	def ReturnNotModified(self) :
		"""
		ReturnNotModified
		
		- None
		"""
		...

	def ReturnRedirect(self, location) :
		"""
		ReturnRedirect
		
		- location
		"""
		...

	def ReturnBadRequest(self) :
		"""
		ReturnBadRequest
		
		- None
		"""
		...

	def ReturnUnauthorized(self, typeName, realm=None) :
		"""
		ReturnUnauthorized
		
		- typeName
		- realm
		"""
		...

	def ReturnForbidden(self) :
		"""
		ReturnForbidden
		
		- None
		"""
		...

	def ReturnNotFound(self) :
		"""
		ReturnNotFound
		
		- None
		"""
		...

	def ReturnMethodNotAllowed(self) :
		"""
		ReturnMethodNotAllowed
		
		- None
		"""
		...

	def ReturnEntityTooLarge(self) :
		"""
		ReturnEntityTooLarge
		
		- None
		"""
		...

	def ReturnInternalServerError(self) :
		"""
		ReturnInternalServerError
		
		- None
		"""
		...

	def ReturnNotImplemented(self) :
		"""
		ReturnNotImplemented
		
		- None
		"""
		...

	def ReturnServiceUnavailable(self) :
		"""
		ReturnServiceUnavailable
		
		- None
		"""
		...

	def ReturnBasicAuthRequired(self) :
		"""
		ReturnBasicAuthRequired
		
		- None
		"""
		...

	def ReturnBearerAuthRequired(self) :
		"""
		ReturnBearerAuthRequired
		
		- None
		"""
		...

	@property
	def Request(self) :
		"""
		Request
		
		- None
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
	def AllowCaching(self) :
		"""
		AllowCaching
		
		- None
		"""
		...

	@AllowCaching.setter
	def AllowCaching(self, value) :
		"""
		AllowCaching
		
		- value
		"""
		...

	@property
	def ContentType(self) :
		"""
		ContentType
		
		- None
		"""
		...

	@ContentType.setter
	def ContentType(self, value) :
		"""
		ContentType
		
		- value
		"""
		...

	@property
	def ContentCharset(self) :
		"""
		ContentCharset
		
		- None
		"""
		...

	@ContentCharset.setter
	def ContentCharset(self, value) :
		"""
		ContentCharset
		
		- value
		"""
		...

	@property
	def ContentLength(self) :
		"""
		ContentLength
		
		- None
		"""
		...

	@ContentLength.setter
	def ContentLength(self, value) :
		"""
		ContentLength
		
		- value
		"""
		...

	@property
	def HeadersSent(self) :
		"""
		HeadersSent
		
		- None
		"""
		...

	@property
	def OnSent(self) :
		"""
		OnSent

		- None
		"""
		...

	@OnSent.setter
	def OnSent(self, value) :
		"""
		OnSent

		- value
		"""
		...
