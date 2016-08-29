#!/usr/bin/python

# Imports
import sys

# Panda3d related
from direct.showbase.ShowBase import ShowBase

# net_core related 
from Server.config.configSetup import Config
from Server.core import Core
from Server.game import GameNetFramework

################################################
################################################
# Server Main

class Server(ShowBase):

	# Load and setup basic needed things
	def __init__(self):
		args = str(sys.argv)

		if "-window" in args:
			ShowBase.__init__(self)
		else:
			ShowBase.__init__(self, windowType = 'none')

		# Load config
		self.config = Config()

		# Set "global server vars"
		self.core = None
		self.gnframework = None
		self.clients = {}

		# Start the default server
		self.startDefaultServer()


		

	def startDefaultServer(self):
		# Stand alone
		#
		print ("Trying to start server... wait...")
		print ("Checking for config...")
		if self.config.hasConfig:
			print ("Config found : GOOD")
			self.start(self.config.MOTD)
		else:
			print ("Something is wrong...")
			print ("Running Make Config File ()...")
			self.MakeConfigFile()

			print ("Trying again...")

	def MakeConfigFile(self):
		self.config.WritePRCFile()

		## Call to get a server started ##
	def start(self,_motd):
		# Start the basics. Core>protocols, database<,
		self.core = Core(self)
		self.gnframework = GameNetFramework(self)

		self.core.start_all()

	def stop(self):
		pass


server = Server()
server.run()
