#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *
from packet import Packet

########################################################################


class PacketManager():
    
    def __init__(self, _serverManager):

    	self.serverManager = _serverManager

    	self.packet = Packet(self)
    	# Opcodes from clients
    	self.opcodeMethods = {}

    def start(self):
    	self.opcodeMethods = {
    		MSG_REGISTER: self.serverManager.loginManager.handleRegister
    	}


    def handlePacket(self, _opcode, _data, _client):
    	self.opcodeMethods[_opcode](_data, _client)



