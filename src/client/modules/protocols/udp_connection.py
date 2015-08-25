#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from panda3d.core import (
    QueuedConnectionManager,
    QueuedConnectionReader,
    ConnectionWriter,
    Datagram,
    NetDatagram,
    NetAddress,
    DatagramIterator)

from direct.task.Task import Task

## Client Imports ##
from modules.packets.opcodes import MSG_NONE, MSG_HELLO_WORLD

########################################################################


class UDPConnection():

    def __init__(self, _clientManager):
    	print "UDP Connection Loaded"
    	self.packetManager = _clientManager.packetManager
    	self.config = _clientManager.config

    def start(self):
        print "start UDP Connection"
    	self.setupUDP()
    	self.startUDPTasks()

    def stop(self):
        self.udpManager.closeConnection(self.udpSocket)

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
                self.packetManager.handlePacket(opcode, data)

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

    def sendHelloMsg(self):
        """
        Sends a hello world message to the server
        """
        address = NetAddress()
        address.setHost("127.0.0.1", self.config.UDPPORTSERVER)
        myPyDatagram = Datagram()
        myPyDatagram.addUint8(MSG_HELLO_WORLD)
        myPyDatagram.addString("Hello, world!")
        self.udpWriter.send(myPyDatagram, self.udpSocket, address)
