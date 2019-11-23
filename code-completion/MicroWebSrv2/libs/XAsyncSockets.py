"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class XAsyncSocketsPoolException(Exception) :
    ...

class XAsyncSocketsPool :
    def __init__(self) :
    	"""
    	- None
    	"""
    	...

    def _incThreadsCount(self) :
    	"""
    	- None
    	"""
    	...

    def _decThreadsCount(self) :
    	"""
    	- None
    	"""
    	...

    def _addSocket(self, socket, asyncSocket) :
    	"""
    	- socket
    	- asyncSocket
    	"""
    	...

    def _removeSocket(self, socket) :
    	"""
    	- socket
    	"""
    	...

    def _socketListAdd(self, socket, socketsList) :
    	"""
    	- socket
    	- socketsList
    	"""
    	...

    def _socketListRemove(self, socket, socketsList) :
    	"""
    	- socket
    	- socketsList
    	"""
    	...

    _CHECK_SEC_INTERVAL = ...

    def _processWaitEvents(self) :
    	"""
    	- None
    	"""
    	...

    def AddAsyncSocket(self, asyncSocket) :
    	"""
    	- asyncSocket
    	"""
    	...

    def RemoveAsyncSocket(self, asyncSocket) :
    	"""
    	- asyncSocket
    	"""
    	...

    def GetAllAsyncSockets(self) :
    	"""
    	- None
    	"""
    	...

    def GetAsyncSocketByID(self, id) :
    	"""
    	- id
    	"""
    	...

    def NotifyNextReadyForReading(self, asyncSocket, notify) :
    	"""
    	- asyncSocket
    	- notify
    	"""
    	...

    def NotifyNextReadyForWriting(self, asyncSocket, notify) :
    	"""
    	- asyncSocket
    	- notify
    	"""
    	...

    def AsyncWaitEvents(self, threadsCount=0) :
    	"""
    	- threadsCount
    	"""
    	...

    def StopWaitEvents(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def WaitEventsProcessing(self) :
    	"""
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
    	- asyncSocketsPool
    	- socket
    	- recvBufSlot
    	- sendBufSlot
    	"""
    	...

    def _setExpireTimeout(self, timeoutSec) :
    	"""
    	- timeoutSec
    	"""
    	...

    def _removeExpireTimeout(self) :
    	"""
    	- None
    	"""
    	...

    def _close(self, closedReason=XClosedReason.Error, triggerOnClosed=True) :
    	"""
    	- closedReason
    	- triggerOnClosed
    	"""
    	...

    def GetAsyncSocketsPool(self) :
    	"""
    	- None
    	"""
    	...

    def GetSocketObj(self) :
    	"""
    	- None
    	"""
    	...

    def Close(self) :
    	"""
    	- None
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	- None
    	"""
    	...

    def OnExceptionalCondition(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def SocketID(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def ExpireTimeSec(self) :
    	"""
    	- None
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

    @property
    def State(self) :
    	"""
    	- None
    	"""
    	...

    @State.setter
    def State(self, value) :
    	"""
    	- value
    	"""
    	...

class XAsyncTCPServerException(Exception) :
    ...

class XAsyncTCPServer(XAsyncSocket) :
    @staticmethod
    def Create(asyncSocketsPool, srvAddr, srvBacklog=256, bufSlots=None) :
    	"""
    	- asyncSocketsPool
    	- srvAddr
    	- srvBacklog
    	- bufSlots
    	"""
    	...

    def __init__(self, asyncSocketsPool, srvSocket, srvAddr, bufSlots) :
    	"""
    	- asyncSocketsPool
    	- srvSocket
    	- srvAddr
    	- bufSlots
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def SrvAddr(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def OnClientAccepted(self) :
    	"""
    	- None
    	"""
    	...

    @OnClientAccepted.setter
    def OnClientAccepted(self, value) :
    	"""
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
    	- None
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	- None
    	"""
    	...

    def AsyncRecvLine(self, lineEncoding='UTF-8', onLineRecv=None, onLineRecvArg=None, timeoutSec=None) :
    	"""
    	- lineEncoding
    	- onLineRecv
    	- onLineRecvArg
    	- timeoutSec
    	"""
    	...

    def AsyncRecvData(self, size=None, onDataRecv=None, onDataRecvArg=None, timeoutSec=None) :
    	"""
    	- size
    	- onDataRecv
    	- onDataRecvArg
    	- timeoutSec
    	"""
    	...

    def AsyncSendData(self, data, onDataSent=None, onDataSentArg=None) :
    	"""
    	- data
    	- onDataSent
    	- onDataRecvArg
    	"""
    	...

    def AsyncSendSendingBuffer(self, size=None, onDataSent=None, onDataSentArg=None) :
    	"""
    	- size
    	- onDataSent
    	- onDataSentArg
    	"""
    	...

    def _doSSLHandshake(self) :
    	"""
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
        - keyfile
        - certfile
        - server_side
        - cert_reqs
        - ca_certs
        """
        ...

    def StartSSLContext(self, sslContext, serverSide=False) :
    	"""
    	- sslContext
    	- serverSide
    	"""
    	...

    @property
    def SrvAddr(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def CliAddr(self) :
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
    def SendingBuffer(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def OnFailsToConnect(self) :
    	"""
    	- None
    	"""
    	...

    @OnFailsToConnect.setter
    def OnFailsToConnect(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnConnected(self) :
    	"""
    	- None
    	"""
    	...

    @OnConnected.setter
    def OnConnected(self, value) :
    	"""
    	- value
    	"""
    	...

class XAsyncUDPDatagramException(Exception) :
    ...

class XAsyncUDPDatagram(XAsyncSocket) :
    @staticmethod
    def Create(asyncSocketsPool, localAddr=None, recvBufLen=4096, broadcast=False) :
    	"""
    	- asyncSocketsPool
    	- localAddr
    	- recvBufLen
    	- broadcast
    	"""
    	...

    def __init__(self, asyncSocketsPool, udpSocket, recvBufSlot) :
    	"""
    	- asyncSocketsPool
    	- udpSocket
    	- recvBufSlot
    	"""
    	...

    def OnReadyForReading(self) :
    	"""
    	- None
    	"""
    	...

    def OnReadyForWriting(self) :
    	"""
    	- None
    	"""
    	...

    def AsyncSendDatagram(self, datagram, remoteAddr, onDataSent=None, onDataSentArg=None) :
    	"""
    	- datagram
    	- remoteAddr
    	- onDataSent
    	- onDataSentArg
    	"""
    	...

    @property
    def LocalAddr(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def OnDataRecv(self) :
    	"""
    	- None
    	"""
    	...

    @OnDataRecv.setter
    def OnDataRecv(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def OnFailsToSend(self) :
    	"""
    	- None
    	"""
    	...

    @OnFailsToSend.setter
    def OnFailsToSend(self, value) :
    	"""
    	- value
    	"""
    	...

class XBufferSlot :
    def __init__(self, size, keepAlloc=True) :
    	"""
    	- size
    	- keepAlloc
    	"""
    	...

    @property
    def Available(self) :
    	"""
    	- None
    	"""
    	...

    @Available.setter
    def Available(self, value) :
    	"""
    	- value
    	"""
    	...

    @property
    def Size(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Buffer(self) :
    	"""
    	- None
    	"""
    	...

class XBufferSlots :
    def __init__(self, slotsCount, slotsSize, keepAlloc=True) :
    	"""
    	- slotsCount
    	- slotsSize
    	- keepAlloc
    	"""
    	...

    def GetAvailableSlot(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def SlotsCount(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def SlotsSize(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Slots(self) :
    	"""
    	- None
    	"""
    	...

class XFiFoException(Exception) :
    ...

class XFiFo :
    def __init__(self) :
    	"""
    	- None
    	"""
    	...

    def Put(self, obj) :
    	"""
    	- obj
    	"""
    	...

    def Get(self) :
    	"""
    	- None
    	"""
    	...

    def Clear(self) :
    	"""
    	- None
    	"""
    	...

    @property
    def Empty(self) :
    	"""
    	- None
    	"""
    	...
