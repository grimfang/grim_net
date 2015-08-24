#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import os
from panda3d.core import (
    ConfigVariableInt,
    ConfigVariableString,
    ConfigPageManager,
    OFileStream,
    loadPrcFile,
    Filename
)

########################################################################

prcFile = os.path.join("..", "server.prc")

class Config():

    def __init__(self):
        # if exist load the config file
        if os.path.exists(prcFile):
            loadPrcFile(Filename.fromOsSpecific(prcFile))
        # set the variables using the config files content or set a default value
        self.MOTD = ConfigVariableString('motd', 'Welcome to grim-net!').getValue()
        self.HOSTNAME = ConfigVariableString('hostname', '127.0.0.1').getValue()
        self.TCPPORT = ConfigVariableInt('tcp_port', '6000').getValue()
        self.BACKLOG = ConfigVariableInt('backlog', '10').getValue()
        self.UDPPORT = ConfigVariableInt('udp_port', '6001').getValue()

    def WritePRCFile(self):
        page = None
        customConfigVariables = ["", "motd", "hostname", "tcp_port", "backlog", "udp_port"]
        if os.path.exists(prcFile):
            # load the existing config file
            page = loadPrcFile(Filename.fromOsSpecific(prcFile))
            removeDecls = []
            for dec in range(page.getNumDeclarations()):
                # Check if our variables are given.
                # NOTE: This check has to be done to not loose our base or other
                #       manual config changes by the user
                if page.getVariableName(dec) in customConfigVariables:
                    decl = page.modifyDeclaration(dec)
                    removeDecls.append(decl)
            for dec in removeDecls:
                page.deleteDeclaration(dec)
        else:
            # create a new config file
            cpMgr = ConfigPageManager.getGlobalPtr()
            page = cpMgr.makeExplicitPage("Grim Net Pandaconfig")

        # config declarations
        page.makeDeclaration("motd", str(self.MOTD))
        page.makeDeclaration("hostname", str(self.HOSTNAME))
        page.makeDeclaration("tcp_port", str(self.TCPPORT))
        page.makeDeclaration("backlog", str(self.BACKLOG))
        page.makeDeclaration("udp_port", str(self.UDPPORT))

        # create a stream to the specified config file
        configfile = OFileStream(prcFile)
        # and now write it out
        page.write(configfile)
        # close the stream
        configfile.close()


#s = Config()
#s.WritePRCFile()
# Writing & Testing
#s = Config()
