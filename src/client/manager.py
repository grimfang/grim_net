#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from panda3d.core import QueuedConnectionManager

## Server Imports ##
from config.config import Config
from modules.packets.packetManager import PacketManager
from modules.protocols.udp_connection import UDPConnection

########################################################################


class Manager():

    def __init__(self, _client):

    	# Load Config
    	self.config = Config()

    	# Load Packet Manager
    	self.packetManager = PacketManager(self)

    	# Load UDP Connection
    	self.udpConnection = UDPConnection(self)
        self.udpConnection.start()


        ## START SUB MANAGERS ##
        self.packetManager.start()


        # Send Register MSG
        self.packetManager.sendRegister("HEllo World")
