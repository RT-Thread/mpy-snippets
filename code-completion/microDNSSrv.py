"""
The MIT License (MIT)
Copyright © 2018 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

from   _thread import start_new_thread
from   re      import match
import socket
import gc

class MicroDNSSrv :
	def Create(self, domainsList) :
		"""
		Speed Creation

		- domainsList
		
		eg. domainsList = {
				"test.com"   : "1.1.1.1",
				"*test2.com" : "2.2.2.2",
				"*google*"   : "192.168.4.1",
				"*.toto.com" : "192.168.4.1",
				"www.site.*" : "192.168.4.1" }
		"""
		...

	def _tryStartThread(self, func, args=()) :
		"""
		_tryStartThread

		- func
		- args
		"""
		...

	def _ipV4StrToBytes(self, ipStr) :
		"""
		_ipV4StrToBytes

		- ipStr
		"""
		...

	def _getAskedDomainName(self, packet) :
		"""
		_getAskedDomainName

		- packet
		"""
		...

	def _getPacketAnswerA(self, packet, ipV4Bytes) :
		"""
		_getPacketAnswerA

		- packet
		- ipV4Bytes
		"""
		...

	def __init__(self) :
		"""
		Initialize object

		-None
		"""
		...

	def _serverProcess(self) :
		"""
		_serverProcess

		- None
		"""
		...

	def Start(self) :
		"""
		Start dns server

		- None
		"""
		...

	def Stop(self) :
		"""
		Stop dns server

		- None
		"""
		...

	def IsStarted(self) :
		"""
		Dns server start status

		- None
		"""
		...

	def SetDomainsList(self, domainsList) :
		"""
		Set domains list

		- domainsList
		"""
		...
