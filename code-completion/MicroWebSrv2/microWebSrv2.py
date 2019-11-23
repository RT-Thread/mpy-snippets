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
    	- None
    	"""
    	...

    @staticmethod
    def _physPathExists(physPath) :
    	"""
    	- physPath
    	"""
    	...

    @staticmethod
    def _physPathIsDir(physPath) :
    	"""
    	- physPath
    	"""
    	...

    @staticmethod
    def LoadModule(modName) :
    	"""
    	- modName
    	"""
    	...

    @staticmethod
    def HTMLEscape(s) :
    	"""
    	- s
    	"""
    	...

    @staticmethod
    def AddDefaultPage(filename) :
    	"""
    	- filename
    	"""
    	...

    @staticmethod
    def AddMimeType(ext, mimeType) :
    	"""
    	- ext
    	- mimeType
    	"""
    	...

    @staticmethod
    def GetMimeTypeFromFilename(filename) :
    	"""
    	- filename
    	"""
    	...

    def StartInPool(self, asyncSocketsPool) :
    	"""
    	- asyncSocketsPool
    	"""
    	...

    def StartManaged(self, parllProcCount=1, procStackSize=0) :
    	"""
    	- parllProcCount
    	- procStackSize
    	"""
    	...

    def Stop(self) :
    	"""
    	- None
    	"""
    	...

    def Log(self, msg, msgType) :
    	"""
    	- msg
    	- msgType
    	"""
    	...

    def ResolvePhysicalPath(self, urlPath) :
    	"""
    	- urlPath
    	"""
    	...

    def _onSrvClientAccepted(self, xAsyncTCPServer, xAsyncTCPClient) :
    	"""
    	- xAsyncTCPServer
    	- xAsyncTCPClient
    	"""
    	...

    def _onSrvClosed(self, xAsyncTCPServer, closedReason) :
    	"""
    	- xAsyncTCPServer
    	- closedReason
    	"""
    	...

    def _validateChangeConf(self, name='Configuration') :
    	"""
    	- name
    	"""
    	...

    def EnableSSL(self, certFile, keyFile, caFile=None) :
    	"""
    	- certFile
    	- keyFile
    	- caFile
    	"""
    	...

    def DisableSSL(self) :
    	"""
    	- None
    	"""
    	...

    def SetEmbeddedConfig(self) :
    	"""
    	- None
    	"""
    	...

    def SetLightConfig(self) :
    	"""
    	- None
    	"""
    	...

    def SetNormalConfig(self) :
    	"""
    	- None
    	"""
    	...

    def SetLargeConfig(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def IsRunning(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def ConnQueueCapacity(self) :
    	"""
    	- None
    	"""
    	...

    @ConnQueueCapacity.setter
    def ConnQueueCapacity(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def BufferSlotsCount(self) :
    	"""
    	- None
    	"""
    	...

    @BufferSlotsCount.setter
    def BufferSlotsCount(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def BufferSlotSize(self) :
    	"""
    	- None
    	"""
    	...

    @BufferSlotSize.setter
    def BufferSlotSize(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def KeepAllocBufferSlots(self) :
    	"""
    	- None
    	"""
    	...

    @KeepAllocBufferSlots.setter
    def KeepAllocBufferSlots(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def MaxRequestContentLength(self) :
    	"""
    	- None
    	"""
    	...

    @MaxRequestContentLength.setter
    def MaxRequestContentLength(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def BindAddress(self) :
    	"""
    	- None
    	"""
    	...

    @BindAddress.setter
    def BindAddress(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def IsSSLEnabled(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def RootPath(self) :
    	"""
    	- None
    	"""
    	...

    @RootPath.setter
    def RootPath(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def RequestsTimeoutSec(self) :
    	"""
    	- None
    	"""
    	...

    @RequestsTimeoutSec.setter
    def RequestsTimeoutSec(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def NotFoundURL(self) :
    	"""
    	- None
    	"""
    	...

    @NotFoundURL.setter
    def NotFoundURL(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnLogging(self) :
    	"""
    	- None
    	"""
    	...

    @OnLogging.setter
    def OnLogging(self, value) :
    	"""
    	- value
    	"""
    	...
