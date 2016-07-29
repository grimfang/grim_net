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

########################################################################


class TCP():

    def __init__(self, _master):
    	print "TCP Protocol Init"
        self.master = _master
    	self.config = self.master.config


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
        taskMgr.add(self.tcpDisconnectionHandler, "tcpDisconnectionHandler", 20)
        print "TCP Disconnection Handler Started"

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
                #self.serverManager.lobbyManager.handleJoinLobby(newConnection, netAddress)
                    
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
                #self.packetManager.handlePacket(opcode, data, datagram.getAddress())

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


    # TCP Disconnection Handler
    def tcpDisconnectionHandler(self, task):
        # Check for resets
        if self.tcpManager.resetConnectionAvailable():
            resetConnection = PointerToConnection()
            self.tcpManager.getResetConnection(resetConnection)
            
            for client in self.serverManager.clients:
                if self.serverManager.clients[client].connection == resetConnection.p():
                    del self.serverManager.clients[client]
                    self.tcpReader.removeConnection(resetConnection.p())
                    print "Removed Connection:", resetConnection.p()
                    print 'Current Clients:', self.serverManager.clients
                    break

        return Task.cont


    def sendPacket(self, _pkt, _connection):
        self.tcpWriter.send(_pkt, _connection)


    def sendBroadcast(self, _pkt, _skipif=None):
        for client in self.serverManager.clients:
            if _skipif == client:
                pass
            else:
                conn = self.serverManager.clients[client].connection
                self.tcpWriter.send(_pkt, conn)
