#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##


########################################################################


class Client():
    
    def __init__(self, _id, _address):

    	self.id = _id
    	self.address = _address

    	print "Client: ", self.id, " from:", self.address, ' Connected'

