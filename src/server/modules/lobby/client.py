#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##


########################################################################


class Client():
    
    def __init__(self, _id, _connection, _netAddress):

    	self.id = _id
    	self.connection = _connection
    	self.netAddress = _netAddress

    	print "Client: ", self.id, " from:", self.connection, ' Connected'
    	print "NetAddress:", self.netAddress

