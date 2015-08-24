#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from manager import Manager

########################################################################


class Server(ShowBase):

    def __init__(self):

        args = str(sys.argv)

        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase.__init__(self, windowType = 'none')

        # Load Manager
        self.manager = Manager(self)


        # Print MOTD *testing
        print self.manager.config.MOTD


server = Server()
server.run()
