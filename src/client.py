#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Client Imports ##

########################################################################

class Client(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)



client = Client()
client.run()
