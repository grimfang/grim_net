#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import time

### PANDA Imports ###

## Server Imports ##

########################################################################


class GameManager():

    def __init__(self, _serverManager):
        # Holder for clients
        self.serverManager = _serverManager

        # Loop break?
        self.gameRunning = False

    def start(self):
        self.gameMainLoop()

    def stop(self):
        pass # remove task


    # make this a task and get rid of the 1st while
    def gameMainLoop(self):

        timeRate = 1000 / 60
        lastTime = 0
        
        '''
        while( true )
            check for client commands
            sanity check client commands
            run AI
            move all entities
            resolve collisions
            sanity check world data
            send updates about the game to the clients
            handle client disconnects
        end
        '''

        while (self.gameRunning):
            time = time.time()

            self.gameSimulationTick(time, lastTime)
            self.gameNetworkUpdateTick()

    # This should run at 60Hz
    def gameSimulationTick(self, _time, _lastTime):
        while(_time > _lastTime):
                
                _lastTime += _timeRate

    # This should run at anything between 10Hz - 15Hz
    def gameNetworkUpdateTick(self):
        pass

