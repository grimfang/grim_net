#!/usr/bin/python

# Imports


# Panda3d related


# net_core related 
from Client.protocol.TCP import TCP
from Client.protocol.packetManager import PacketManager
from Client.framework.clientObject import ClientObject

################################################
################################################
# 

class Core():
	#Handle all the core functions "low level stuff"

	def __init__(self, _client):
		self.client = _client

		# protocols
		self.tcp = None
		self.udp = None

		# Packet Manager
		self.packetManager = None

	def start_all(self):
		self.load_protocol()
		self.load_packetManager()

	def load_protocol(self):
		self.tcp = TCP(self)
		self.tcp.start()

	def load_packetManager(self):
		self.packetManager = PacketManager(self)
		self.packetManager.start()

	def connect(self, _host, _port):
		self.tcp.connectToServer(_host, _port)

	def createClientObject(self, _data):
		self.client.clientObject = ClientObject(_data)