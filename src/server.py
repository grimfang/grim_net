#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from Server.Config.Config import Config
from Server.Core.Master import Master

########################################################################


class Server(ShowBase):

    def __init__(self):

        args = str(sys.argv)

        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase.__init__(self, windowType = 'none')


        # Load config
        self.config = Config()

        # Start Master
        self.master = Master(self)

        # Start Game Framework
        

server = Server()
server.run()
