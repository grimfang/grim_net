#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *

########################################################################


class PacketManager():
    
    def __init__(self, _serverManager):

    	self.serverManager = _serverManager

    	self.opcodeMethods = {}

    def start(self):
    	self.opcodeMethods = {
    		CMSG_JOIN_LOBBY: self.serverManager.lobbyManager.handleJoinLobby
    	}


    def handlePacket(self, _opcode, _data, _client):
    	self.opcodeMethods[_opcode](_data, _client)



