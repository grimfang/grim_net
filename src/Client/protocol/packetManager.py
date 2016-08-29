#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

## Server Imports ##
from Client.protocol.opcodes import *

########################################################################


class PacketManager():
    
    def __init__(self, _core):

    	self.core = _core

    	self.opcodeMethods = {}

    def start(self):
    	self.opcodeMethods = {
    		MSG_NONE: self.BlankMSG,
            MSG_REGISTER: self.registerClient
    	}


    def handlePacket(self, _opcode, _data):
    	self.opcodeMethods[_opcode](_data)

    ## Commands

    def BlankMSG(self, _data):
    	print (_data, _client)

    def registerClient(self, _data):
        print(_data)
        self.core.createClientObject(_data)

