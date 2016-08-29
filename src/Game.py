#!/usr/bin/python

# Imports
import sys

# Panda3d related
from direct.showbase.ShowBase import ShowBase

# net_core related 
from net_core_client import Client
from Game.gui.guiManager import GuiManager

################################################
################################################
# Game Main

class Game(ShowBase):

	def __init__(self):

		ShowBase.__init__(self)


		#Start the net client
		self.client = Client(self)
		self.client.startDefaultClient()

		# Start gui
		self.guiManager = GuiManager(self)


game = Game()
game.run()