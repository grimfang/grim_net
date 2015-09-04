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
from shared.opcodes import MSG_NONE

########################################################################


class TCPConnection():

    def __init__(self, _clientManager):
    	print "TCP Connection Loaded"
        self.serverManager = _clientManager
    	self.packetManager = _clientManager.packetManager
    	self.config = _clientManager.config


    def start(self):
    	self.setupTCP()
    	self.startTCPTasks()


    def setupTCP(self):
    	self.tcpManager = QueuedConnectionManager()
        self.tcpReader = QueuedConnectionReader(self.tcpManager, 0)
        self.tcpWriter = ConnectionWriter(self.tcpManager, 0)

    def startTCPTasks(self):
    	taskMgr.add(self.tcpReaderTask, "tcpReaderTask", -10)
    	print "TCP Reader Started"


    def tcpReaderTask(self, task):
        """
        Handle any data from clients by sending it to the Handlers.
        """
        while 1:
            (datagram, data, opcode) = self.tcpNonBlockingRead(self.tcpReader)
            if opcode is MSG_NONE:
                # Do nothing or use it as some 'keep_alive' thing.
                break
            else:
                # Handle it
                self.packetManager.handlePacket(opcode, data, datagram.getAddress())

        return Task.cont


    # TCP NonBlockingRead??
    def tcpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection udpReader
        """
        if self.tcpReader.dataAvailable():
            datagram = NetDatagram()
            if self.tcpReader.getData(datagram):
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


    def makeConnection(self, _ip):
        self.tcpConnection = self.tcpManager.openTCPClientConnection(_ip, self.config.TCPPORT, 1000)

        if self.tcpConnection != None:
            pass
            # Add connection to reader