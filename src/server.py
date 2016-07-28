#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##

########################################################################


class Server(ShowBase):

    def __init__(self):

        args = str(sys.argv)

        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase.__init__(self, windowType = 'none')

server = Server()
server.run()
