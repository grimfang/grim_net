#!/usr/bin/python

# Imports


# Panda3d related


# net_core related 
from Server.protocol.TCP import TCP
from Server.protocol.packetManager import PacketManager
from Server.framework.clientObject import ClientObject
from Server.database.dbManager import DBManager

################################################
################################################
# 

class Core():
	#Handle all the core functions "low level stuff"

	def __init__(self, _server):
		self.server = _server

		# protocols
		self.tcp = None
		self.udp = None

		# Packet manager
		self.packetManager = None

		# Database Manager
		self.dbManager = None

	def start_all(self):
		self.load_protocol()
		self.load_packetManager()
		self.load_database()

	def load_protocol(self):
		self.tcp = TCP(self)
		self.tcp.start()

	def load_packetManager(self):
		self.packetManager = PacketManager(self)
		self.packetManager.start()

	def load_database(self):
		self.dbManager = DBManager(self)
		self.dbManager.start()


	## Handlers ##

	def handleNewConnection(self, _uuid, _connection, _address):
		# used with persistence
		self.createPlayerObject(_uuid, _connection, _address)
		self.dbManager.insertData(_uuid, _address)

	def createPlayerObject(self, _uuid, _connection, _address):
		print ("Created Client Object: ", _uuid, _connection, _address)
		self.server.clients[_uuid] = ClientObject(_uuid, _connection, _address)
		self.packetManager.registerClient(_uuid, _connection)