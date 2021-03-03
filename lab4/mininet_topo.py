#!/usr/bin/python

"""
This setup the topology in lab4
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.link import Link, Intf, TCLink
import os 
from time import sleep
import sys

class Topology(Topo):
    
    
    def __init__(self):
        "Create Topology."
        
        # Initialize topology
        Topo.__init__(self)
        
        
        #### There is a rule of naming the hosts and switch, so please follow the rules like "h1", "h2" or "s1", "s2" for hosts and switches!!!!
      
        # Add hosts
        host1 = self.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
        host2 = self.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
        host3 = self.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
        host4 = self.addHost('h4', ip='10.0.0.4', mac='00:00:00:00:00:04')
        
        
        
        # Add switches
        swA = self.addSwitch('s1')
        swB = self.addSwitch('s2')
        swC = self.addSwitch('s3')
        swD = self.addSwitch('s4')
        
        
        # Add links
        self.addLink(host1, swA, 1, 1)
        self.addLink(host2, swB, 1, 1)
        self.addLink(host3, swC, 1, 1)
        self.addLink(host4, swD, 1, 1)
        self.addLink(swA, swB, 2, 2)
        self.addLink(swB, swC, 3, 2)
        self.addLink(swC, swD, 3, 2)
        self.addLink(swD, swA, 3, 3)
              
        
        

# This is for "mn --custom"
topos = { 'mytopo': ( lambda: Topology() ) }




# This is for "python *.py"
if __name__ == '__main__':
    setLogLevel( 'info' )
            
    topo = Topology()
    net = Mininet(topo=topo, controller=lambda name: RemoteController( name, ip='127.0.0.1' ),link=TCLink)       # The TCLink is a special setting for setting the bandwidth in the future.
    
    # 1. Start mininet
    net.start()
    
    
    # Wait for links setup (sometimes, it takes some time to setup, so wait for a while before mininet starts)
    print "\nWaiting for links to setup . . . .",
    sys.stdout.flush()
    for time_idx in range(3):
        print ".",
        sys.stdout.flush()
        sleep(1)
    
        
    # 2. Start the CLI commands
    info( '\n*** Running CLI\n' )
    CLI( net )
    
    
    # 3. Stop mininet properly
    net.stop()


    ### If you did not close the mininet, please run "mn -c" to clean up and re-run the mininet 