#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sys

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

## Server Imports ##
from shared.opcodes import *
from shared.packet import Packet
from server.modules.utils.util import generateUUID
from client import Client

########################################################################


class LobbyManager():
    
    def __init__(self, _serverManager):

    	self.serverManager = _serverManager
        self.clients = _serverManager.clients


    def handleJoinLobby(self, _data, _client):

        # Create UUID for the new client  / later we will check if client already has UUID (save games?)
        newId = generateUUID()

        # Create and store client object for the server, to handle client related things
        self.clients[newId] = Client(newId, _client)

        # Phase 1
        # tell the client to move to the lobby screen 
        pkt = Packet.pack(SMSG_MOVE_TO_LOBBY, [newId])
        self.serverManager.udpConnection.sendPacket(pkt, _client)

        # Phase 2
        # tell the client about the connected clients
        # already in the lobby
        print len(self.clients)

        if len(self.clients) > 1:
            listOfClients = []
            for c in self.clients:
                if c == newId:
                    pass
                else:
                    listOfClients.append(c)

            pkt = Packet.pack(SMSG_UPDATE_LOBBY_LIST, listOfClients)
            self.serverManager.udpConnection.sendPacket(pkt, _client)

            # Phase 3
            # tell other clients about this new client
            pkt = Packet.pack(SMSG_UPDATE_LOBBY_LIST, [newId])
            self.serverManager.udpConnection.sendBroadcast(pkt, newId)









