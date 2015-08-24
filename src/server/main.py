#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from config.config import Config

########################################################################


class Server(ShowBase):
    
    def __init__(self):

        args = str(sys.argv)

        # Load config
        config = Config()
        
        if "-window" in args:
            ShowBase.__init__(self)
        else:
            ShowBase(windowType = 'none')
            print config.MOTD


server = Server()
base.run()