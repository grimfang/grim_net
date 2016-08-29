#!/usr/bin/python

# Imports
import sys

# Panda3d related
from direct.showbase.ShowBase import ShowBase

# net_core related 
from net_core_client import Client

################################################
################################################
# Game Main

class Game(ShowBase):

	def __init__(self):

		ShowBase.__init__(self)


		#Start the net client
		self.client = Client(self)
		self.client.startDefaultClient()


game = Game()
game.run()