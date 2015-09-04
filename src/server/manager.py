#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from config.config import Config
from modules.packets.packetManager import PacketManager
from modules.protocols.tcp_connection import TCPConnection
from modules.protocols.udp_connection import UDPConnection
from modules.lobby.lobbyManager import LobbyManager

########################################################################


class Manager():

    def __init__(self, _server):
        # Holder for clients
        self.clients = {}

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

        # Load Lobby Manager
        self.lobbyManager = LobbyManager(self)


        ## LOAD OPCODES ## START SUB MANAGERS ##
        self.packetManager.start()
        
