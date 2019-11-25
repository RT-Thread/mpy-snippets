"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class XAsyncSocketsPoolException(Exception) :
    ...

class XAsyncSocketsPool :
    def __init__(self) :
    	"""
    	__init__
    	
    	- None
    	"""
    	...

    def _incThreadsCount(self) :
    	"""
    	_incThreadsCount
    	
    	- None
    	"""
    	...

    def _decThreadsCount(self) :
    	"""
    	_decThreadsCount
    	
    	- None
    	"""
    	...

    def _addSocket(self, socket, asyncSocket) :
    	"""
    	_addSocket
    	
    	- socket
    	- asyncSocket
    	"""
    	...

    def _removeSocket(self, socket) :
    	"""
    	_removeSocket
    	
    	- socket
    	"""
    	...

    def _socketListAdd(self, socket, socketsList) :
    	"""
    	_socketListAdd
    	
    	- socket
    	- socketsList
    	"""
    	...

    def _socketListRemove(self, socket, socketsList) :
    	"""
    	_socketListRemove
    	
    	- socket
    	- socketsList
    	"""
    	...

    _CHECK_SEC_INTERVAL = ...

    def _processWaitEvents(self) :
    	"""
    	_processWaitEvents
    	
    	- None
    	"""
    	...

    def AddAsyncSocket(self, asyncSocket) :
    	"""
    	AddAsyncSocket
    	
    	- asyncSocket
    	"""
    	...

    def RemoveAsyncSocket(self, asyncSocket) :
    	"""
    	RemoveAsyncSocket
    	
    	- asyncSocket
    	"""
    	...

    def GetAllAsyncSockets(self) :
    	"""
    	GetAllAsyncSockets
    	
    	- None
    	"""
    	...

    def GetAsyncSocketByID(self, id) :
    	"""
    	GetAsyncSocketByID
    	
    	- id
    	"""
    	...

    def NotifyNextReadyForReading(self, asyncSocket, notify) :
    	"""
    	NotifyNextReadyForReading
    	
    	- asyncSocket
    	- notify
    	"""
    	...

    def NotifyNextReadyForWriting(self, asyncSocket, notify) :
    	"""
    	NotifyNextReadyForWriting
    	
    	- asyncSocket
    	- notify
    	"""
    	...

    def AsyncWaitEvents(self, threadsCount=0) :
    	"""
    	AsyncWaitEvents
    	
    	- threadsCount
    	"""
    	...

    def StopWaitEvents(self) :
    	"""
    	StopWaitEvents
    	
    	- None
    	"""
    	...

    @property
    def WaitEventsProcessing(self) :
    	"""
    	WaitEventsProcessing
    	
    	- None
    	"""
    	...

class XClosedReason() :
    Error        = ...
    ClosedByHost = ...
    ClosedByPeer = ...
    Timeout      = ...

class XAsyncSocketException(Exception) :
    ...

class XAsyncSocket :
    def __init__(self, asyncSocketsPool, socket, recvBufSlot=None, sendBufSlot=None) :
    	"""
    	__init__
    	
    	- asyncSocketsPool
    	- socket
    	- recvBufSlot
    	- sendBufSlot
    	"""
    	...

    def _setExpireTimeout(self, timeoutSec) :
    	"""
    	_setExpireTimeout
    	
    	- timeoutSec
    	"""
    	...

    def _removeExpireTimeout(self) :
    	"""
    	_removeExpireTimeout
    	
    	- None
    	"""
    	...

    def _close(self, closedReason=XClosedReason.Error, triggerOnClosed=True) :
    	"""
    	_close
    	
    	- closedReason
    	- triggerOnClosed
    	"""
    	...

    def GetAsyncSocketsPool(self) :
    	"""
    	GetAsyncSocketsPool
    	
    	- None
    	"""
    	...

    def GetSocketObj(self) :
    	"""
    	GetSocketObj
    	
    	- None
    	"""
    	...

    def Close(self) :
    	"""
    	Close
    	
    	- None
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	OnReadyForReading
    	
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	OnReadyForWriting
    	
    	- None
    	"""
    	...

    def OnExceptionalCondition(self) :
    	"""
    	OnExceptionalCondition
    	
    	- None
    	"""
    	...

    @property
    def SocketID(self) :
    	"""
    	SocketID
    	
    	- None
    	"""
    	...

    @property
    def ExpireTimeSec(self) :
    	"""
    	ExpireTimeSec
    	
    	- None
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

    @property
    def State(self) :
    	"""State
    	
    	- None
    	"""
    	...

    @State.setter
    def State(self, value) :
    	"""
    	State
    	
    	- value
    	"""
    	...

class XAsyncTCPServerException(Exception) :
    ...

class XAsyncTCPServer(XAsyncSocket) :
    @staticmethod
    def Create(asyncSocketsPool, srvAddr, srvBacklog=256, bufSlots=None) :
    	"""
    	Create
    	
    	- asyncSocketsPool
    	- srvAddr
    	- srvBacklog
    	- bufSlots
    	"""
    	...

    def __init__(self, asyncSocketsPool, srvSocket, srvAddr, bufSlots) :
    	"""
    	__init__
    	
    	- asyncSocketsPool
    	- srvSocket
    	- srvAddr
    	- bufSlots
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	OnReadyForReading

    	- None
    	"""
    	...

    @property
    def SrvAddr(self) :
    	"""
    	SrvAddr
    	
    	- None
    	"""
    	...

    @property
    def OnClientAccepted(self) :
    	"""
    	OnClientAccepted
    	
    	- None
    	"""
    	...

    @OnClientAccepted.setter
    def OnClientAccepted(self, value) :
    	"""
    	OnClientAccepted
    	
    	- value
    	"""
    	...

class XAsyncTCPClientException(Exception) :
    ...

class XAsyncTCPClient(XAsyncSocket) :
    @staticmethod
    def Create( asyncSocketsPool,
                srvAddr,
                connectTimeout = 5,
                recvBufLen     = 4096,
                sendBufLen     = 4096,
                connectAsync   = True ) :
        """
        Create
        
        - asyncSocketsPool
        - srvAddr
        - connectTimeout
        - recvBufLen
        - sendBufLen
        - connectAsync
        """
        ...

    def __init__(self, asyncSocketsPool, cliSocket, srvAddr, cliAddr, recvBufSlot, sendBufSlot) :
    	"""
    	__init__
    	
    	- asyncSocketsPool
    	- cliSocket
    	- srvAddr
    	- cliAddr
    	- recvBufSlot
    	- sendBufSlot
    	"""
    	...

    def Close(self) :
    	"""
    	Close
    	
    	- None
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	OnReadyForReading
    	
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	OnReadyForWriting
    	
    	- None
    	"""
    	...

    def AsyncRecvLine(self, lineEncoding='UTF-8', onLineRecv=None, onLineRecvArg=None, timeoutSec=None) :
    	"""
    	AsyncRecvLine
    	
    	- lineEncoding
    	- onLineRecv
    	- onLineRecvArg
    	- timeoutSec
    	"""
    	...

    def AsyncRecvData(self, size=None, onDataRecv=None, onDataRecvArg=None, timeoutSec=None) :
    	"""
    	AsyncRecvData
    	
    	- size
    	- onDataRecv
    	- onDataRecvArg
    	- timeoutSec
    	"""
    	...

    def AsyncSendData(self, data, onDataSent=None, onDataSentArg=None) :
    	"""
    	AsyncSendData
    	
    	- data
    	- onDataSent
    	- onDataRecvArg
    	"""
    	...

    def AsyncSendSendingBuffer(self, size=None, onDataSent=None, onDataSentArg=None) :
    	"""
    	AsyncSendSendingBuffer
    	
    	- size
    	- onDataSent
    	- onDataSentArg
    	"""
    	...

    def _doSSLHandshake(self) :
    	"""
    	_doSSLHandshake
    	
    	- None
    	"""
    	...

    def StartSSL( self,
                  keyfile     = None,
                  certfile    = None,
                  server_side = False,
                  cert_reqs   = 0,
                  ca_certs    = None ) :
        """
        StartSSL
        
        - keyfile
        - certfile
        - server_side
        - cert_reqs
        - ca_certs
        """
        ...

    def StartSSLContext(self, sslContext, serverSide=False) :
    	"""
    	StartSSLContext
    	
    	- sslContext
    	- serverSide
    	"""
    	...

    @property
    def SrvAddr(self) :
    	"""
    	SrvAddr
    	
    	- None
    	"""
    	...

    @property
    def CliAddr(self) :
    	"""
    	CliAddr
    	
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
    def SendingBuffer(self) :
    	"""
    	SendingBuffer
    	
    	- None
    	"""
    	...

    @property
    def OnFailsToConnect(self) :
    	"""
    	OnFailsToConnect
    	
    	- None
    	"""
    	...

    @OnFailsToConnect.setter
    def OnFailsToConnect(self, value) :
    	"""
    	OnFailsToConnect
    	
    	- value
    	"""
    	...

    @property
    def OnConnected(self) :
    	"""
    	OnConnected
    	
    	- None
    	"""
    	...

    @OnConnected.setter
    def OnConnected(self, value) :
    	"""
    	OnConnected
    	
    	- value
    	"""
    	...

class XAsyncUDPDatagramException(Exception) :
    ...

class XAsyncUDPDatagram(XAsyncSocket) :
    @staticmethod
    def Create(asyncSocketsPool, localAddr=None, recvBufLen=4096, broadcast=False) :
    	"""
    	Create
    	
    	- asyncSocketsPool
    	- localAddr
    	- recvBufLen
    	- broadcast
    	"""
    	...

    def __init__(self, asyncSocketsPool, udpSocket, recvBufSlot) :
    	"""
    	__init__
    	
    	- asyncSocketsPool
    	- udpSocket
    	- recvBufSlot
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	OnReadyForReading
    	
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	OnReadyForWriting
    	
    	- None
    	"""
    	...

    def AsyncSendDatagram(self, datagram, remoteAddr, onDataSent=None, onDataSentArg=None) :
    	"""
    	AsyncSendDatagram
    	
    	- datagram
    	- remoteAddr
    	- onDataSent
    	- onDataSentArg
    	"""
    	...

    @property
    def LocalAddr(self) :
    	"""
    	LocalAddr
    	
    	- None
    	"""
    	...

    @property
    def OnDataRecv(self) :
    	"""
    	OnDataRecv
    	
    	- None
    	"""
    	...

    @OnDataRecv.setter
    def OnDataRecv(self, value) :
    	"""
    	OnDataRecv
    	
    	- value
    	"""
    	...

    @property
    def OnFailsToSend(self) :
    	"""
    	OnFailsToSend
    	
    	- None
    	"""
    	...

    @OnFailsToSend.setter
    def OnFailsToSend(self, value) :
    	"""
    	OnFailsToSend
    	
    	- value
    	"""
    	...

class XBufferSlot :
    def __init__(self, size, keepAlloc=True) :
    	"""
    	__init__
    	
    	- size
    	- keepAlloc
    	"""
    	...

    @property
    def Available(self) :
    	"""
    	Available
    	
    	- None
    	"""
    	...

    @Available.setter
    def Available(self, value) :
    	"""
    	Available
    	
    	- value
    	"""
    	...

    @property
    def Size(self) :
    	"""
    	Size
    	
    	- None
    	"""
    	...

    @property
    def Buffer(self) :
    	"""
    	Buffer
    	
    	- None
    	"""
    	...

class XBufferSlots :
    def __init__(self, slotsCount, slotsSize, keepAlloc=True) :
    	"""
    	__init__
    	
    	- slotsCount
    	- slotsSize
    	- keepAlloc
    	"""
    	...

    def GetAvailableSlot(self) :
    	"""
    	GetAvailableSlot
    	
    	- None
    	"""
    	...

    @property
    def SlotsCount(self) :
    	"""
    	SlotsCount
    	
    	- None
    	"""
    	...

    @property
    def SlotsSize(self) :
    	"""
    	SlotsSize
    	
    	- None
    	"""
    	...

    @property
    def Slots(self) :
    	"""
    	Slots
    	
    	- None
    	"""
    	...

class XFiFoException(Exception) :
    ...

class XFiFo :
    def __init__(self) :
    	"""
    	__init__
    	
    	- None
    	"""
    	...

    def Put(self, obj) :
    	"""
    	Put
    	
    	- obj
    	"""
    	...

    def Get(self) :
    	"""
    	Get
    	
    	- None
    	"""
    	...

    def Clear(self) :
    	"""
    	Clear
    	
    	- None
    	"""
    	...

    @property
    def Empty(self) :
    	"""
    	Empty
    	
    	- None
    	"""
    	...
