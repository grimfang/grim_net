#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader
from panda3d.core import QueuedConnectionListener
from panda3d.core import ConnectionWriter
from panda3d.core import PointerToConnection, NetAddress, NetDatagram
from panda3d.core import Datagram
from panda3d.core import DatagramIterator

from direct.task.Task import Task
from utils import Queue
#from Server.protocol.opcodes import MSG_NONE
#from Server.Util import generateUUID

########################################################################


class SocketTCP(ShowBase):

    def __init__(self, _parent=None):
        ShowBase.__init__(self, windowType = 'none')
        print ("TCP Protocol Startup...")
        #self.parent = _parent

        #self.config = self.parent.server.config
        # tmp config
        self.tcpport = 6000
        self.backlog = 10
        self.hostname = '127.0.0.1'

        self.sendPacketQueue = None


    def startAll(self):
        self.setupTCP()
        self.startTCPTasks()


    def setupTCP(self):
        self.tcpManager = QueuedConnectionManager()
        self.tcpReader = QueuedConnectionReader(self.tcpManager, 0)
        self.tcpWriter = ConnectionWriter(self.tcpManager, 0)
        self.tcpListener = QueuedConnectionListener(self.tcpManager, 0)

        self.tcpSocket = self.tcpManager.openTCPServerRendezvous(self.tcpport, self.backlog)
        self.tcpListener.addConnection(self.tcpSocket)
        print ("Started Server on: ", self.hostname, self.tcpport)


    def startTCPTasks(self):
        taskMgr.add(self.tcpListenerTask, "tcpListenerTask", 0)
        print ("TCP Listener Started")
        taskMgr.add(self.tcpReaderTask, "tcpReaderTask", -10)
        print ("TCP Reader Started")
        taskMgr.add(self.tcpDisconnectionHandler, "tcpDisconnectionHandler", 20)
        print ("TCP Disconnection Handler Started")
        taskMgr.add(self.tcpQueuedSendHandlerTask, "tcpQueuedSendhandlerTask", -11)
        print ("TCP Queued Send Handler Started")

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

                #self.core.createPlayerObject(generateUUID(),newConnection, netAddress)
                    
                print ("Server: " + str(generateUUID), str(netAddress.getIpString()))
            else:
                print ("Server: Connection Failed from -", str(netAddress.getIpString()))    
                    
            
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
                #self.core.packetManager.handlePacket(opcode, data, datagram.getAddress())
                print("Set Packet Handler to handle packets!")
                
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
            print(str(resetConnection.p()))
            #for client in self.core.server.clients:
            #    if self.core.server.clients[client].connection == resetConnection.p():
            #        del self.core.server.clients[client]
            #        self.tcpReader.removeConnection(resetConnection.p())
            #        print ("Removed Connection:", resetConnection.p())
            #        print ('Current Clients:', self.core.server.clients)
            #        break

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

    def addPacketToSendQueue(self, _data):
        # _data should contain packet and connection
        pass

    def addPacketToBroadcastQueue(self, _pkt, _connectionList):
        # _data should contain the pkt data and _connectionList should be the valid connections for that broadcast
        # Could have a grouping system that put clients together and broadcasts go per group
        pass

    def tcpQueuedSendHandlerTask(self, task):
        
        if not self.sendPacketQueue.isEmpty():
            self.addPacketToSendQueue(self.sendPacketQueue.removeFromQue())
        
        return Task.cont






socketTcp = SocketTCP()
socketTcp.run()