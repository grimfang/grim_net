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

    	print "something"

    # This packet should send the server needed info to register it self on the server
    # Things like the client name or so could be added to it
    def buildRegister(self, _data):

    	pkt = Datagram()
    	pkt.addUint8(MSG_REGISTER)

    	pkt.addString(_data)

    	return pkt