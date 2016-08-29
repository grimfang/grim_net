#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##


### PANDA Imports ###
from panda3d.core import Datagram


from Server.protocol.opcodes import *


########################################################################


class Packet():

    def __init__(self, _packetManager):

    	self.packetManager = _packetManager

    def writeRegisterPacket(self, _data):
    	# Build a packet
    	pkt = Datagram()

    	# Type of packet
    	pkt.addUint8(MSG_REGISTER)

    	pkt.addString(str(_data))

    	return pkt

    def readPacket(self, _pkt):
    	pass