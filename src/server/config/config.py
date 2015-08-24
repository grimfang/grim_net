#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import ConfigParser

########################################################################


class Config():
    
    def __init__(self):

        config = ConfigParser.RawConfigParser()
        config.read('./server.cfg')

        self.MOTD = config.get('MOTD', 'motd')
        self.HOSTNAME = config.get('NETWORK', 'hostname')
        self.TCPPORT = config.getint('NETWORK', 'tcp_port')
        self.BACKLOG = config.getint('NETWORK', 'backlog')
        self.UDPPORT = config.getint('NETWORK', 'udp_port')
        
        #self.writeNewCfgFile()


    def writeNewCfgFile(self, _data=[]):

        config = ConfigParser.RawConfigParser()

        config.add_section('MOTD')
        config.set('MOTD', 'motd', 'Default')

        config.add_section('NETWORK')
        config.set('NETWORK', 'hostname', '127.0.0.1')
        config.set('NETWORK', 'tcp_port', '6000')
        config.set('NETWORK', 'backlog', '10')
        config.set('NETWORK', 'udp_port', '6001')

        with open('../server.cfg', 'wb') as cfg:
            config.write(cfg)



# Writing & Testing
#s = Config()
