#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

## Server Imports ##
from Server.protocol.opcodes import *
from Server.protocol.packet import Packet

########################################################################


class PacketManager():
    
    def __init__(self, _core):
        self.core = _core

        self.packet = Packet(self)

        self.opcodeMethods = {}

    def start(self):
        self.opcodeMethods = {
            MSG_NONE: self.BlankMSG
        }


    def handlePacket(self, _opcode, _data, _client):
        self.opcodeMethods[_opcode](_data, _client)


    ## Commands ##

    # Recv
    def BlankMSG(self, _data, _client):
        print (_data, _client)

    # Send
    def registerClient(self, _data, _client):
        pkt = self.packet.writeRegisterPacket(_data)
        self.core.tcp.sendPacket(pkt, _client)


