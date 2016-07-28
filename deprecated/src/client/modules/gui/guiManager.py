#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from direct.gui.DirectGui import DirectButton

## Server Imports ##
from guiMenu import GuiMenu

########################################################################


class GuiManager():

    def __init__(self, _clientManager):
        # Local ID
        self.clientManager = _clientManager

        # Create the menu * testing
        self.menu = GuiMenu(self)
        


    

