#importing libraries
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.util import irange



class leafNspine(Topo):

	def __init__ (self,s,l,h):
     
         #variables
		leaflist = []
		spinelist = []
                hostlist = []
 
		#initializing topology
		Topo.__init__(self)
     
		# adding the spine switch
		for i in irange(0, s-1):
			spineswitch = self.addSwitch('s%s' %(i))
			spinelist.append(spineswitch)
          

		# adding the leaf switch
		for p in irange(0, l-1):
			leafswitch = self.addSwitch('l%s' %(p))
			leaflist.append(leafswitch)
			# adding the host
			for j in irange(0, h-1):
				hostnode = self.addHost('l%sh%s' %(p,j))
				hostlist.append(hostnode)
				self.addLink(leafswitch,hostnode)  #linking and host and leaf switches

		#linking spine and leaf switches
		for i in irange (0, s-1):
			for j in irange (0, l-1):
				self.addLink(spinelist[i], leaflist[j])
            

topos = { "leafNspine" :  leafNspine  }
