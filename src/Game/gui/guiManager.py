#!/usr/bin/python

# Imports
import sys

# Panda3d related
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectButton
from panda3d.core import TextNode

# net_core related 

################################################
################################################
# 

class GuiManager():

	def __init__(self, _game):
		self.game = _game

		self.bk_text = "In Development: Simple Menu"
		self.textObject = OnscreenText(text = self.bk_text, pos = (-0.95,-0.95), 
		scale = 0.05,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=0)

		# Add button
		self.b = DirectButton(text = ("Connect"), scale=.06, command=self.connect)
		self.b2 = DirectButton(text = ("Exit"),pos = (0.0, 0, -0.15), scale=.06, command=self.handleExit)

	def start(self):
		pass

	def stop(self):
		pass

	def connect(self):
		print("Try connecting")
		self.game.client.core.connect(self.game.client.config.SERVERIP, self.game.client.config.TCPPORT)

	def handleExit(self):
		sys.exit()