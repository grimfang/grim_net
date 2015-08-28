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

    # Do some packing
    @classmethod
    def pack(cls, _opcode, _data):

    	pkt = NetDatagram()

    	# Opcode
    	pkt.addUint8(_opcode)

    	# Length
    	pkt.addUint8(len(_data))

    	# Read the data from the _data var and add types to the packet as needed
    	for d in range(len(_data)):

    		# Strings
    		if type(_data[d]) is str:
    			pkt.addString(_data[d])

    		# unsigned ints
    		elif type(_data[d]) is int and _data[d] > 0:
    			if _data[d] <= 255:
    				pkt.addUint8(_data[d])
    			elif _data[d] <= 65535:
    				pkt.addUint16(_data[d])
    			elif _data[d] <= 4294967295:
    				pkt.addUint32(_data[d])

    		# signed ints
    		elif type(_data[d]) is int:
    			if _data[d] >= -128 and _data[d] <= 127:
    				pkt.addInt8(_data[d])
    			elif _data[d] >= -32768 and _data[d] <= 32767:
    				pkt.addInt16(_data[d])
    			elif _data[d] >= -2147483648 and _data[d] <= 2147483647:
    				pkt.addInt32(_data[d])

    		# Bool
    		elif type(_data[d]) is bool:
    			pkt.addBool(_data[d])

    		# Float
    		elif type(_data[d]) is float:
    			pkt.addFloat32(_data[d])

        return pkt

    @classmethod
    def unpack(cls, _pkt):
        pass

    	

