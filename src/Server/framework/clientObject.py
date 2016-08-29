#!/usr/bin/python

# Imports

# Panda3d related

# net_core related 

################################################
################################################
# Client object container

class ClientObject():

	def __init__(self, _uuid, _connection, _address):

		self.id = _uuid
		self.connection = _connection
		self.address = _address

		
