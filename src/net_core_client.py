#!/usr/bin/python

# Imports
import sys

# Panda3d related


# net_core related 
from Client.config.config import Config
from Client.core import Core

################################################
################################################
# Client Main

class Client():

	# Load and setup basic needed things
	def __init__(self, _game):
		self.game = _game
		

		self.core = None
		self.clientObject = None	

		# Config
		self.config = Config()

	def startDefaultClient(self):
		# 

		print ("Trying to start client... wait...")
		print ("Checking for config...")
		if self.config.hasConfig:
			print ("Config found : GOOD")
			self.start(self.config.SERVERIP, self.config.TCPPORT, self.config.UDPPORTSERVER)
		else:
			print ("Something is wrong...")
			print ("Running Make Config File ()...")
			self.MakeConfigFile()

			print ("Try running again...")
			sys.exit()

	def MakeConfigFile(self):
		self.config.WritePRCFile()

		## Call to get a server started ##
	def start(self, _host, _port, _serverudpport):
		# Start the basics for the client
		self.core = Core(self)

		self.core.start_all()


		# Temp testing
		self.core.connect(_host, _port)

	def stop(self):
		pass