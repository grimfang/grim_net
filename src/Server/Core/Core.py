#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##


### PANDA Imports ###


## Server Imports ##
import Server.Utils.Util
from Network.Protocols.TCP import TCP


########################################################################

# Core master (low level)
class Core():

    def __init__(self, _server):

        self.server = _server

        # Load TCP Protocol
        self.tcp = TCP(self)

        # Load UDP Protocol
       