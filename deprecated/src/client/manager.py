#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

## Server Imports ##
from config.config import Config
from modules.packets.packetManager import PacketManager
from modules.protocols.tcp_connection import TCPConnection
from modules.protocols.udp_connection import UDPConnection
from modules.gui.guiManager import GuiManager

########################################################################


class Manager():

    def __init__(self, _client):
        # Local ID
        self.localID = None

    	# Load Config
    	self.config = Config()

    	# Load Packet Manager
    	self.packetManager = PacketManager(self)

        # Load TCP Connection
        self.tcpConnection = TCPConnection(self)
        self.tcpConnection.start()

    	# Load UDP Connection
    	self.udpConnection = UDPConnection(self)
        self.udpConnection.start()

        # Load GUI Manager
        self.guiManager = GuiManager(self)

        #### START SUB MANAGERS Should only start when they are really needed ####
        self.packetManager.start()
    

