#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *

########################################################################


class PacketManager():
    
    def __init__(self, _serverManager):

    	pass


    def handlePacket(self, _opcode, _data):
    	print _opcode, _data



