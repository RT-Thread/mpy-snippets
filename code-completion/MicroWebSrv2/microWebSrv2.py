"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

from .             import *
from .httpRequest  import HttpRequest
from os            import stat
from sys           import implementation
from _thread       import stack_size

class MicroWebSrv2Exception(Exception) :
	...

class MicroWebSrv2 :
    _DEFAULT_PAGES = ...
    _MIME_TYPES = ...
    _HTML_ESCAPE_CHARS = ...
    _STAT_MODE_DIR = ...

    DEBUG        = ...
    INFO         = ...
    WARNING      = ...
    ERROR        = ...
    MSG_TYPE_STR = ...

    _modules = ...

    def __init__(self) :
    	"""
    	__init__
    	
    	- None
    	"""
    	...

    @staticmethod
    def _physPathExists(physPath) :
    	"""
    	_physPathExists
    	
    	- physPath
    	"""
    	...

    @staticmethod
    def _physPathIsDir(physPath) :
    	"""
    	_physPathIsDir
    	
    	- physPath
    	"""
    	...

    @staticmethod
    def LoadModule(modName) :
    	"""
    	LoadModule
    	
    	- modName
    	"""
    	...

    @staticmethod
    def HTMLEscape(s) :
    	"""
    	HTMLEscape
    	
    	- s
    	"""
    	...

    @staticmethod
    def AddDefaultPage(filename) :
    	"""
    	AddDefaultPage
    	
    	- filename
    	"""
    	...

    @staticmethod
    def AddMimeType(ext, mimeType) :
    	"""
    	AddMimeType
    	
    	- ext
    	- mimeType
    	"""
    	...

    @staticmethod
    def GetMimeTypeFromFilename(filename) :
    	"""
    	GetMimeTypeFromFilename
    	
    	- filename
    	"""
    	...

    def StartInPool(self, asyncSocketsPool) :
    	"""
    	StartInPool
    	
    	- asyncSocketsPool
    	"""
    	...

    def StartManaged(self, parllProcCount=1, procStackSize=0) :
    	"""
    	StartManaged
    	
    	- parllProcCount
    	- procStackSize
    	"""
    	...

    def Stop(self) :
    	"""
    	Stop
    	
    	- None
    	"""
    	...

    def Log(self, msg, msgType) :
    	"""
    	Log
    	
    	- msg
    	- msgType
    	"""
    	...

    def ResolvePhysicalPath(self, urlPath) :
    	"""
    	ResolvePhysicalPath
    	
    	- urlPath
    	"""
    	...

    def _onSrvClientAccepted(self, xAsyncTCPServer, xAsyncTCPClient) :
    	"""
    	_onSrvClientAccepted
    	
    	- xAsyncTCPServer
    	- xAsyncTCPClient
    	"""
    	...

    def _onSrvClosed(self, xAsyncTCPServer, closedReason) :
    	"""
    	_onSrvClosed
    	
    	- xAsyncTCPServer
    	- closedReason
    	"""
    	...

    def _validateChangeConf(self, name='Configuration') :
    	"""
    	_validateChangeConf
    	
    	- name
    	"""
    	...

    def EnableSSL(self, certFile, keyFile, caFile=None) :
    	"""
		EnableSSL
		
    	- certFile
    	- keyFile
    	- caFile
    	"""
    	...

    def DisableSSL(self) :
    	"""
    	DisableSSL
    	
    	- None
    	"""
    	...

    def SetEmbeddedConfig(self) :
    	"""
    	SetEmbeddedConfig
    	
    	- None
    	"""
    	...

    def SetLightConfig(self) :
    	"""
    	SetLightConfig
    	
    	- None
    	"""
    	...

    def SetNormalConfig(self) :
    	"""
    	SetNormalConfig
    	
    	- None
    	"""
    	...

    def SetLargeConfig(self) :
    	"""
    	SetLargeConfig
    	
    	- None
    	"""
    	...

    @property
    def IsRunning(self) :
    	"""
    	IsRunning
    	
    	- None
    	"""
    	...

    @property
    def ConnQueueCapacity(self) :
    	"""
    	ConnQueueCapacity
    	
    	- None
    	"""
    	...

    @ConnQueueCapacity.setter
    def ConnQueueCapacity(self, value) :
    	"""
    	ConnQueueCapacity
    	
    	- value
    	"""
    	...

    @property
    def BufferSlotsCount(self) :
    	"""
    	BufferSlotsCount
    	
    	- None
    	"""
    	...

    @BufferSlotsCount.setter
    def BufferSlotsCount(self, value) :
    	"""
    	BufferSlotsCount
    	
    	- value
    	"""
    	...

    @property
    def BufferSlotSize(self) :
    	"""
    	BufferSlotSize
    	
    	- None
    	"""
    	...

    @BufferSlotSize.setter
    def BufferSlotSize(self, value) :
    	"""
    	BufferSlotSize
    	
    	- value
    	"""
    	...

    @property
    def KeepAllocBufferSlots(self) :
    	"""
    	KeepAllocBufferSlots
    	
    	- None
    	"""
    	...

    @KeepAllocBufferSlots.setter
    def KeepAllocBufferSlots(self, value) :
    	"""
    	KeepAllocBufferSlots
    	
    	- value
    	"""
    	...

    @property
    def MaxRequestContentLength(self) :
    	"""
    	MaxRequestContentLength
    	
    	- None
    	"""
    	...

    @MaxRequestContentLength.setter
    def MaxRequestContentLength(self, value) :
    	"""
    	MaxRequestContentLength
    	
    	- value
    	"""
    	...

    @property
    def BindAddress(self) :
    	"""
    	BindAddress
    	
    	- None
    	"""
    	...

    @BindAddress.setter
    def BindAddress(self, value) :
    	"""
    	BindAddress
    	
    	- value
    	"""
    	...

    @property
    def IsSSLEnabled(self) :
    	"""
    	IsSSLEnabled
    	
    	- None
    	"""
    	...

    @property
    def RootPath(self) :
    	"""
    	RootPath
    	
    	- None
    	"""
    	...

    @RootPath.setter
    def RootPath(self, value) :
    	"""
    	RootPath
    	
    	- value
    	"""
    	...

    @property
    def RequestsTimeoutSec(self) :
    	"""
    	RequestsTimeoutSec
    	
    	- None
    	"""
    	...

    @RequestsTimeoutSec.setter
    def RequestsTimeoutSec(self, value) :
    	"""
    	RequestsTimeoutSec
    	
    	- value
    	"""
    	...

    @property
    def NotFoundURL(self) :
    	"""
    	NotFoundURL
    	
    	- None
    	"""
    	...

    @NotFoundURL.setter
    def NotFoundURL(self, value) :
    	"""
    	NotFoundURL
    	
    	- value
    	"""
    	...

    @property
    def OnLogging(self) :
    	"""
    	OnLogging
    	
    	- None
    	"""
    	...

    @OnLogging.setter
    def OnLogging(self, value) :
    	"""
    	OnLogging
    	
    	- value
    	"""
    	...
