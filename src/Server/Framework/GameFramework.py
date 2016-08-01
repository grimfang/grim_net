#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##


### PANDA Imports ###


## Server Imports ##


########################################################################


class GameFramework():

    def __init__(self, _server):

        self.server = _server

        self.clients = {}

    def createNewClient(self, _uuid, _connection, _ipAddress):
    	self.clients[_uuid] = {}
    	self.clients[_uuid]['connection'] = _connection
    	self.clients[_uuid]['ipAddress'] = _ipAddress

        