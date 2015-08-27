#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Datagram
from panda3d.core import NetDatagram

## Server Imports ##
from shared.opcodes import *

########################################################################

# This class methods will return the needed packet.
class Packet():
    
    def __init__(self, _packetManager):

    	self.packetManager = _packetManager


    def buildRegisterACK(self, _data):

    	pkt = NetDatagram()
    	pkt.addUint8(MSG_REGISTER_ACK)
    	pkt.addString(_data)

    	return pkt

    def buildRegisterBroadcast(self, _data):

    	pkt = Datagram()
    	pkt.addUint8(MSG_REGISTER_BROADCAST)
    	pkt.addString(_data)

    	return pkt


    def buildPacket(self, _opcode, _data):
    	pkt = NetDatagram()

    	pkt.addUint8(_opcode)

    	# Read the data from the _data var and add types to the packet as needed
    	for d in range(len(_data)):
    		if type(_data[d]) is str:
    			print "AddString"
    			pkt.addString(_data[d])

    		elif type(_data[d]) is int:
    			print "AddInt"


    	return pkt
    	

