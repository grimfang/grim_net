#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Datagram

## Server Imports ##
from shared.opcodes import *

########################################################################

# This class methods will return the needed packet.
class Packet():
    
    def __init__(self, _packetManager):

    	self.packetManager = _packetManager


    def buildRegisterACK(self, _data):

    	pkt = Datagram()
    	pkt.addUint8(MSG_REGISTER_ACK)
    	pkt.addString(_data)

    	return pkt