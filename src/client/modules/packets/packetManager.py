#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *
from packet import Packet

########################################################################


class PacketManager():
    
    def __init__(self, _clientManager):
    	self.clientManager = _clientManager
    	self.packet = Packet(self)

    	# Opcodes from server
    	self.opcodeMethods = {}


    def start(self):
    	self.udpSocket = self.clientManager.udpConnection.udpSocket
    	self.hostAddress = self.clientManager.udpConnection.hostAddress

    	self.opcodeMethods = {
    		MSG_REGISTER_ACK: self.test
    	}

    def handlePacket(self, _opcode, _data):
    	self.opcodeMethods[_opcode](_data)


    def sendRegister(self, _data):
    	pkt = self.packet.buildRegister(_data)
    	self.clientManager.udpConnection.udpWriter.send(pkt, self.udpSocket, self.hostAddress)

    def test(self, _data):
    	print _data



