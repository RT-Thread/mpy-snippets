"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class WebSockets :
    _PROTOCOL_VERSION = ...
    _HANDSHAKE_SIGN   = ...


    def __init__(self) :
    	"""
    	__init__

    	- None
    	"""
    	...

    def OnRequest(self, microWebSrv2, request) :
    	"""
    	OnRequest
    	
    	- microWebSrv2
    	- request
    	"""
    	...

    @property
    def OnWebSocketProtocol(self) :
    	"""
    	OnWebSocketProtocol
    	
    	- None
    	"""
    	...

    @OnWebSocketProtocol.setter
    def OnWebSocketProtocol(self, value) :
    	"""
    	OnWebSocketProtocol
    	
    	- value
    	"""
    	...

    @property
    def OnWebSocketAccepted(self) :
    	"""
    	OnWebSocketAccepted
    	
    	- None
    	"""
    	...

    @OnWebSocketAccepted.setter
    def OnWebSocketAccepted(self, value) :
    	"""
    	OnWebSocketAccepted
    	
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
		__init__
		
		- wsMod
		- mws2
		- request
		"""
		...

    def _recvData(self, onRecv, size=None) :
    	"""
    	_recvData
    	
    	- onRecv
    	- size
    	"""
    	...

    def _onXAsCliClosed(self, xasCli, closedReason) :
    	"""
    	_onXAsCliClosed
    	
    	- xasCli
    	- closedReason
    	"""
    	...

    def _waitFrame(self) :
    	"""
    	_waitFrame
    	
    	- None
    	"""
    	...
        
        def onHdrStartingRecv(xasCli, data, arg) :
			"""
			onHdrStartingRecv
			
			- xasCli
			- data
			- arg
			"""
			...

            def endOfHeader(maskingKey) :
            	"""
            	endOfHeader
            	
            	- maskingKey
            	"""
            	...

                def onPayloadDataRecv(xasCli, data, arg) :
                	"""
                	onPayloadDataRecv
                	
                	- xasCli
                	- data
                	- arg
                	"""
                	...

            def getMaskingKey() :
            	"""
            	getMaskingKey
            	
            	- None
            	"""
            	...
                
    def _sendFrame(self, opcode, data=None, fin=True) :
    	"""
    	_sendFrame
    	
    	- opcode
    	- data
    	- fin
    	"""
    	...

    def _close(self, statusCode=None, reason=None, waitCloseFrame=False) :
    	"""
    	_close
    	
    	- statusCode
    	- reason
    	- waitCloseFrame
    	"""
    	...

    def SendTextMessage(self, msg) :
    	"""
    	SendTextMessage
    	
    	- msg
    	"""
    	...

    def SendBinaryMessage(self, msg) :
    	"""
    	SendBinaryMessage
    	
    	- msg
    	"""
    	...

    def Close(self) :
    	"""
    	Close
    	
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
    def IsClosed(self) :
    	"""
    	IsClosed
    	
    	- None
    	"""
    	...

    @property
    def WaitFrameTimeoutSec(self) :
    	"""
    	WaitFrameTimeoutSec
    	
    	- None
    	"""
    	...

    @WaitFrameTimeoutSec.setter
    def WaitFrameTimeoutSec(self, value) :
    	"""
    	WaitFrameTimeoutSec
    	
    	- value
    	"""
    	...

    @property
    def MaxRecvMessageLength(self) :
    	"""
    	MaxRecvMessageLength
    	
    	- None
    	"""
    	...

    @MaxRecvMessageLength.setter
    def MaxRecvMessageLength(self, value) :
    	"""
    	MaxRecvMessageLength
    	
    	- value
    	"""
    	...

    @property
    def OnTextMessage(self) :
    	"""
    	OnTextMessage
    	
    	- None
    	"""
    	...

    @OnTextMessage.setter
    def OnTextMessage(self, value) :
    	"""
    	OnTextMessage
    	
    	- value
    	"""
    	...

    @property
    def OnBinaryMessage(self) :
    	"""
    	OnBinaryMessage
    	
    	- None
    	"""
    	...

    @OnBinaryMessage.setter
    def OnBinaryMessage(self, value) :
    	"""
    	OnBinaryMessage
    	
    	- value
    	"""
    	...

    @property
    def OnClosed(self) :
    	"""
    	OnClosed
    	
    	- None
    	"""
    	...

    @OnClosed.setter
    def OnClosed(self, value) :
    	"""
    	OnClosed
    	
    	- value
    	"""
    	...
