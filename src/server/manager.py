#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from config.config import Config
from modules.packets.packetManager import PacketManager
from modules.protocols.udp_connection import UDPConnection

########################################################################


class Manager():

    def __init__(self, _server):

    	# Load Config
    	self.config = Config()

    	# Load Packet Manager
    	self.packetManager = PacketManager(self)

    	# Load UDP Connection
    	self.udpConnection = UDPConnection(self)
        self.udpConnection.start()
