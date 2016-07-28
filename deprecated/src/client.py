#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Client Imports ##
from client.manager import Manager

########################################################################

class Client(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load Manager
        self.manager = Manager(self)



client = Client()
client.run()
