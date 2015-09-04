#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from panda3d.core import QueuedConnectionManager

## Server Imports ##
from config.config import Config
from modules.packets.packetManager import PacketManager
from modules.protocols.tcp_connection import TCPConnection
from modules.protocols.udp_connection import UDPConnection

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


        ## START SUB MANAGERS ##
        self.packetManager.start()

        # Connect to server
        self.tcpConnection.joinServerLobby('127.0.0.1', 6000)

