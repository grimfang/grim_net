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
from modules.logon.loginManager import LoginManager

########################################################################


class Manager():

    def __init__(self, _server):
        # Holder for clients
        self.clients = {}

    	# Load Config
    	self.config = Config()

    	# Load Packet Manager
    	self.packetManager = PacketManager(self)

    	# Load UDP Connection
    	self.udpConnection = UDPConnection(self)
        self.udpConnection.start()

        # Load Login Manager
        self.loginManager = LoginManager(self)


        ## LOAD OPCODES ## START SUB MANAGERS ##
        self.packetManager.start()
        
