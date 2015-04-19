'''


@author:    Chip Boling
@copyright: 2015 Boling Consulting Solutions. All rights reserved.
@license:   Artistic License 2.0, http://opensource.org/licenses/Artistic-2.0
@contact:   support@bcsw.net
@deffield   updated: Updated
'''

import keystone
import neutron

def discoverAllNodes():
    '''
    Discover all nodes in the network that are available through 
    OpenStack APIs
    
    TODO: This will change radically, for now, just do some hardcoded calls
          to various interfaces and see what is available.  Evenutally this
          will be consolidated once patterns emerge.
    '''
        
    # TODO: Call into any needed APIs
    
    print 'TODO: Openstack: Discovery'
    
    # Get the tenant list
    
    
    neutron.discoverAll()
    #nova.discoverAll()
    
    pass