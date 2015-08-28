#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *
from shared.packet import Packet

########################################################################


class PacketManager():
    
    def __init__(self, _clientManager):
    	self.clientManager = _clientManager

    	# Opcodes from server
    	self.opcodeMethods = {}


    def start(self):
    	self.opcodeMethods = {
    		SMSG_MOVE_TO_LOBBY: self.setID,
            SMSG_UPDATE_LOBBY_LIST: self.test
    	}

    def handlePacket(self, _opcode, _data):
    	self.opcodeMethods[_opcode](_data)


    def sendRegister(self, _data):
    	pkt = Packet.pack(CMSG_JOIN_LOBBY, _data)
    	self.clientManager.udpConnection.sendPacket(pkt)



    ### HANDLE SIMPLE STUFF HERE ###
    def setID(self, _data):
        length = _data.getUint8()
        print "length:", length
    	#self.clientManager.localID = _data.getString()
        #print "Local ID:", self.clientManager.localID
        listStrings = []
        for x in range(length):
            listStrings.append(_data.getString())

        print listStrings

    def test(self, _data):
        print _data



