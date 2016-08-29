#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

## Server Imports ##
from Server.protocol.opcodes import *

########################################################################


class PacketManager():
    
    def __init__(self, _core):

    	self.core = _core

    	self.opcodeMethods = {}

    def start(self):
    	self.opcodeMethods = {
    		MSG_NONE: self.BlankMSG
    	}


    def handlePacket(self, _opcode, _data, _client):
    	self.opcodeMethods[_opcode](_data, _client)

    def BlankMSG(self, _data, _client):
    	print (_data, _client)

