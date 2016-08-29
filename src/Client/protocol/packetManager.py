#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

## Server Imports ##
from Client.protocol.opcodes import *
from Client.protocol.packet import Packet

########################################################################


class PacketManager():
    
    def __init__(self, _core):
        self.core = _core
        
        self.packet = Packet(self)
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
        uuid = self.packet.readRegisterPacket(_data)
        self.core.createClientObject(uuid)

