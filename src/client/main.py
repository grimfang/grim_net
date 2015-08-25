#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from manager import Manager

########################################################################

class Client(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load Manager
        self.manager = Manager(self)


        # Print MOTD *testing
        #print self.manager.config.MOTD

        # Test send
        self.manager.udpConnection.sendHelloMsg()


client = Client()
client.run()
