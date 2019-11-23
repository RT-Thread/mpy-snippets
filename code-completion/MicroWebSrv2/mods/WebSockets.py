"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class WebSockets :
    _PROTOCOL_VERSION = ...
    _HANDSHAKE_SIGN   = ...


    def __init__(self) :
        self._onWebSocketProtocol = ...
        self._onWebSocketAccepted = ...

    def OnRequest(self, microWebSrv2, request) :
    	"""
    	- microWebSrv2
    	- request
    	"""
    	...

    @property
    def OnWebSocketProtocol(self) :
    	"""
    	- None
    	"""
    	...

    @OnWebSocketProtocol.setter
    def OnWebSocketProtocol(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnWebSocketAccepted(self) :
    	"""
    	- None
    	"""
    	...

    @OnWebSocketAccepted.setter
    def OnWebSocketAccepted(self, value) :
    	"""
    	- value
    	"""
    	...

class WebSocket :
    _OP_FRAME_CONT  = ...
    _OP_FRAME_TEXT  = ...
    _OP_FRAME_BIN   = ...
    _OP_FRAME_CLOSE = ...
    _OP_FRAME_PING  = ...
    _OP_FRAME_PONG  = ...
    
    _MSG_TYPE_TEXT  = ...
    _MSG_TYPE_BIN   = ...

    def __init__(self, wsMod, mws2, request) :
		"""
		- wsMod
		- mws2
		- request
		"""
		...

    def _recvData(self, onRecv, size=None) :
    	"""
    	- onRecv
    	- size
    	"""
    	...

    def _onXAsCliClosed(self, xasCli, closedReason) :
    	"""
    	- xasCli
    	- closedReason
    	"""
    	...

    def _waitFrame(self) :
    	"""
    	- None
    	"""
    	...
        
        def onHdrStartingRecv(xasCli, data, arg) :
			"""
			- xasCli
			- data
			- arg
			"""
			...

            def endOfHeader(maskingKey) :
            	"""
            	- maskingKey
            	"""
            	...

                def onPayloadDataRecv(xasCli, data, arg) :
                	"""
                	- xasCli
                	- data
                	- arg
                	"""
                	...

            def getMaskingKey() :
            	"""
            	- None
            	"""
            	...
                
    def _sendFrame(self, opcode, data=None, fin=True) :
    	"""
    	- opcode
    	- data
    	- fin
    	"""
    	...

    def _close(self, statusCode=None, reason=None, waitCloseFrame=False) :
    	"""
    	- statusCode
    	- reason
    	- waitCloseFrame
    	"""
    	...

    def SendTextMessage(self, msg) :
    	"""
    	- msg
    	"""
    	...

    def SendBinaryMessage(self, msg) :
    	"""
    	- msg
    	"""
    	...

    def Close(self) :
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
    def IsClosed(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def WaitFrameTimeoutSec(self) :
    	"""
    	- None
    	"""
    	...

    @WaitFrameTimeoutSec.setter
    def WaitFrameTimeoutSec(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def MaxRecvMessageLength(self) :
    	"""
    	- None
    	"""
    	...

    @MaxRecvMessageLength.setter
    def MaxRecvMessageLength(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnTextMessage(self) :
    	"""
    	- None
    	"""
    	...

    @OnTextMessage.setter
    def OnTextMessage(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnBinaryMessage(self) :
    	"""
    	- None
    	"""
    	...

    @OnBinaryMessage.setter
    def OnBinaryMessage(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnClosed(self) :
    	"""
    	- None
    	"""
    	...

    @OnClosed.setter
    def OnClosed(self, value) :
    	"""
    	- value
    	"""
    	...
