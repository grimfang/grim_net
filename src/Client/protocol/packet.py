#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##


### PANDA Imports ###
from panda3d.core import Datagram
from panda3d.core import DatagramIterator


from Client.protocol.opcodes import *


########################################################################


class Packet():

    def __init__(self, _packetManager):
        self.packetManager = _packetManager

    # Register Packet #
    def writeRegisterPacket(self, _data):
        # Build a packet
        pkt = Datagram()

        # Type of packet
        pkt.addUint8(MSG_REGISTER)
        pkt.addString(str(_data))
        return pkt

    def readRegisterPacket(self, _pkt):
        uuid = _pkt.getString()
        return uuid

    # 