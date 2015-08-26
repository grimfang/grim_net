#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##

########################################################################


class Client():

	def __init__(self, _id, _addr):
		self.id = _id
		self.address = _addr

		print "Client Created with ID: ", self.id, " at address: ", self.address
    
    
