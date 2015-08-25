#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader
from panda3d.core import QueuedConnectionListener
from panda3d.core import ConnectionWriter
from panda3d.core import PointerToConnection, NetAddress, NetDatagram
from panda3d.core import Datagram
from panda3d.core import DatagramIterator

from direct.task.Task import Task

## Server Imports ##
from modules.packets.opcodes import MSG_NONE

########################################################################


class UDPConnection():

    def __init__(self, _serverManager):
    	print "UDP Connection Loaded"
    	self.packetManager = _serverManager.packetManager
    	self.config = _serverManager.config


    def start(self):
    	self.setupUDP()
    	self.startUDPTasks()


    def setupUDP(self):
    	self.udpManager = QueuedConnectionManager()
        self.udpReader = QueuedConnectionReader(self.udpManager, 0)
        self.udpWriter = ConnectionWriter(self.udpManager, 0)
        self.udpSocket = self.udpManager.openUDPConnection(self.config.UDPPORT)

        self.udpReader.addConnection(self.udpSocket)


    def startUDPTasks(self):
    	taskMgr.add(self.udpReaderTask, "udpReaderTask", -10)
    	print "UDP Reader Started"


    def udpReaderTask(self, task):
        """
        Handle any data from clients by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode) = self.udpNonBlockingRead(self.udpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break
            else:
                # Handle it
                self.packetManager.handlePacket(opcode, data, datagram.getConnection())

        return Task.cont


    # UDP NonBlockingRead??
    def udpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection udpReader
        """
        if self.udpReader.dataAvailable():
            datagram = NetDatagram()
            if self.udpReader.getData(datagram):
                data = DatagramIterator(datagram)
                opcode = data.getUint8()

            else:
                data = None
                opcode = MSG_NONE

        else:
            datagram = None
            data = None
            opcode = MSG_NONE

        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode)
