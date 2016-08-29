#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import sqlite3

### PANDA Imports ###

## Server Imports ##


########################################################################


class DBManager():
    
    def __init__(self, _core):
        self.core = _core

        # DB
        self.hasDB = False
        self.dbconn = None


    def start(self):
        self.createDBFile("server_test")
        #self.createDefaultTable()


    def createDBFile(self, _name):
        if self.dbconn == None:
            self.dbconn = sqlite3.connect(_name +".db")
            self.hasDB = True


    def createDefaultTable(self):
        self.dbconn.execute('''CREATE TABLE CLIENTS
            (ID INT PRIMARY KEY     NOT NULL,
            UUID           TEXT    NOT NULL,
            ADDRESS     INT     NOT NULL);''')

    def insertData(self, _uuid, _address):
        self.dbconn.execute("INSERT INTO CLIENTS (UUID, ADDRESS) VALUES (str(_uuid), int(_address))");
        self.dbconn.commit()





