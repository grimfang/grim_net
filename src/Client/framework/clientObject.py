#!/usr/bin/python

# Imports

# Panda3d related

# net_core related 

################################################
################################################
# Client object container

class ClientObject():

	def __init__(self, _uuid):

		self.id = _uuid
		self.state = 0 #0-first connected, 1-registered, 2-lobby, 3-game