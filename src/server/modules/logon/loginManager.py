#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *
from server.modules.utils.util import generateUUID
from client import Client

########################################################################


class LoginManager():
    
    def __init__(self, _serverManager):

    	self.serverManager = _serverManager

    
    def handleRegister(self, _data, _client):
    	print "MSG in Packet:", _data.getString()
    	cid = generateUUID()
    	addr = _client

    	self.serverManager.clients[cid] = Client(cid, addr)

    	
