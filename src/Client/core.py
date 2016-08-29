#!/usr/bin/python

# Imports


# Panda3d related


# net_core related 
from Client.protocol.TCP import TCP

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

	def start_all(self):
		self.load_protocol()

	def load_protocol(self):
		self.tcp = TCP(self)
		self.tcp.start()

	def connect(self, _host, _port):
		self.tcp.connectToServer(_host, _port)