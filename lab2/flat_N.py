#!/usr/bin/python

"""
This setup the topology in lab3-part1
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

N = 6
class Topology(Topo):
    
    
    def __init__(self):
        "Create Topology."
        
        # Initialize topology
        Topo.__init__(self)
        
        
        #### There is a rule of naming the hosts and switch, so please follow the rules like "h1", "h2" or "s1", "s2" for hosts and switches!!!!
      
        # Add hosts

        hosts = []
        for i in range(N*N/2):
            hosts.append(self.addHost('h{}'.format(i+1)))
           
                  
        # Add switches
        switches_1 = []
        switches_2 = []
        for i in range(N/2):
            switches_1.append(self.addSwitch('s{}'.format(i+1)))
 
           
        for i in range(N):
            switches_2.append(self.addSwitch('s{}'.format(N/2+ i + 1)))
           
        for s in range(N/2):
            for i in range(N):
                self.addLink(switches_1[s], switches_2[i])
                
        for h in range(len(hosts)):
            self.addLink(hosts[h], switches_2[h//(N/2)])
           
        
        
        

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