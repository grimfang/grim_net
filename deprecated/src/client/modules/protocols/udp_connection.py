#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
from random import randint

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
from shared.opcodes import MSG_NONE

########################################################################


class UDPConnection():

    def __init__(self, _clientManager):
    	print "UDP Connection Loaded"
        self.clientManager = _clientManager
    	self.packetManager = _clientManager.packetManager
    	self.config = _clientManager.config

    def start(self):
        print "Start UDP Connection"
    	self.setupUDP()
    	self.startUDPTasks()
        self.setHost()

    def setHost(self):
        # Add option to change host address if needed, aka custom ip
        self.hostAddress = NetAddress()
        self.hostAddress.setHost(self.config.SERVERIP, self.config.UDPPORTSERVER)

    def stop(self):
        self.udpManager.closeConnection(self.udpSocket)

    ### JUST FOR TESTING ON SAME PC
    def genPort(self):
        port = randint(6005, 8000)
        print "Generated port:", port

        return port
    ###############################

    def setupUDP(self):
    	self.udpManager = QueuedConnectionManager()
        self.udpReader = QueuedConnectionReader(self.udpManager, 0)
        self.udpWriter = ConnectionWriter(self.udpManager, 0)
        self.udpSocket = self.udpManager.openUDPConnection(self.genPort())

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


    def sendPacket(self, _pkt):
        self.udpWriter.send(_pkt, self.udpSocket, self.hostAddress)
