#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.gui.DirectGui import DirectButton

## Server Imports ##

########################################################################


class GuiMenu():

    def __init__(self, _guiManager):
        # Local ID
        self.guiManager = _guiManager

        self.createServer = self.createButton("Create Server", (-0.8, 0, 0.65), self.createServerCMD)
        self.joinServer = self.createButton("Join Server", (-0.8, 0, 0.55), self.joinServerCMD)
        self.options = self.createButton("Options", (-0.8, 0, 0.45), self.optionsCMD)
        self.exit = self.createButton("Exit", (-0.8, 0, 0.33), self.exitCMD)


    def createButton(self, _text, _pos=(0, 0, 0), _cmd=None):
        texture = loader.loadTexture("client/modules/gui/test.png")
        return DirectButton(text=_text, text_scale=(0.8, 0.8), scale=.07, 
                                frameTexture=texture, pos=_pos, pad=(.2, .2),
                                text_fg=(242, 242, 242, 1), command=_cmd)


    def show(self):
        self.createServer.show()
        self.joinServer.show()
        self.options.show()
        self.exit.show()

    def hide(self):
        self.createServer.hide()
        self.joinServer.hide()
        self.options.hide()
        self.exit.hide()


    ## MENU COMMANDS #
    def createServerCMD(self):
        pass

    def joinServerCMD(self):
        # Shortcut for now...
        self.guiManager.clientManager.tcpConnection.joinServerLobby('127.0.0.1', 6000)

    def optionsCMD(self):
        pass

    def exitCMD(self):
        sys.exit()