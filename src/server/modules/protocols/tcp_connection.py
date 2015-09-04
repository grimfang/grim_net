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

    def __init__(self, _serverManager):
    	print "TCP Connection Loaded"
        self.serverManager = _serverManager
    	self.packetManager = _serverManager.packetManager
    	self.config = _serverManager.config


    def start(self):
    	self.setupTCP()
    	self.startTCPTasks()


    def setupTCP(self):
    	self.tcpManager = QueuedConnectionManager()
        self.tcpReader = QueuedConnectionReader(self.tcpManager, 0)
        self.tcpWriter = ConnectionWriter(self.tcpManager, 0)
        self.tcpListener = QueuedConnectionListener(self.tcpManager, 0)

        self.tcpSocket = self.tcpManager.openTCPServerRendezvous(self.config.TCPPORT, self.config.BACKLOG)
        self.tcpListener.addConnection(self.tcpSocket)


    def startTCPTasks(self):
        taskMgr.add(self.tcpListenerTask, "tcpListenerTask", 0)
        print "TCP Listener Started"
    	taskMgr.add(self.tcpReaderTask, "tcpReaderTask", -10)
    	print "TCP Reader Started"

    # TCP Listener Task
    def tcpListenerTask(self, task):
        """
        Accept new incoming connection from clients, related to TCP
        """
        # Handle new connection
        if self.tcpListener.newConnectionAvailable():
            rendezvous = PointerToConnection()
            netAddress = NetAddress()
            newConnection = PointerToConnection()
            
            if self.tcpListener.getNewConnection(rendezvous, netAddress, newConnection):
                newConnection = newConnection.p()
                
                # Tell the reader about the new TCP connection
                self.tcpReader.addConnection(newConnection)
                self.server.activeConnections.append(newConnection)
                    
                print "Server: New Connection from -", str(netAddress.getIpString())
            else:
                print "Server: Connection Failed from -", str(netAddress.getIpString())    
                    
            
        return Task.cont


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


    def sendPacket(self, _pkt, _addr):
        self.tcpWriter.send(_pkt, self.udpSocket, _addr)


    def sendBroadcast(self, _pkt, _skipif=None):
        for client in self.serverManager.clients:
            if _skipif == client:
                pass
            else:
                addr = self.serverManager.clients[client].address
                self.udpWriter.send(_pkt, self.udpSocket, addr)
