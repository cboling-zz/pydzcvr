'''
Python API interface into Neutron Networking client

@author:    Chip Boling
@copyright: 2015 Boling Consulting Solutions. All rights reserved.
@license:   Artistic License 2.0, http://opensource.org/licenses/Artistic-2.0
@contact:   support@bcsw.net
@deffield   updated: Updated

@see: http://docs.openstack.org/developer/python-neutronclient/
'''

import sys
import neutronclient.v2_0.client as netClient

def _getNeutronClient(authUrl, username, password, project, version=None):
    """
    Get the neutron client for a particular installation and project
    
    :Parameters:
        authUrl (string) URL
        
    :Returns:
        client
    :ReturnType:
        neutronclient
    """

    credentials = { 'username'    : username,
                    'password'    : password,
                    'auth_url'    : authUrl,
                    'tenant_name' : project, 
                  }

    try:
        return netClient.Client(**credentials)

    except netClient.exceptions, e:
        sys.stderr.write("neutron._getNeutronClient: " + repr(e) + "\n")

    except Exception, e:
        sys.stderr.write("neutron._getNeutronClient (other exception): " + repr(e) + "\n")

    return None, "n/a"
            

def discoverAll():
    # First see if we can get a nova client API interfaces
    
    url      = 'http://bcsw-os-controller:35357/v2.0'     # TODO make into class/dict and pass in list of projects
    username = 'admin'
    password = 'password'
    project  = 'admin'

    client = _getNeutronClient(url, username, password, project)
    
    if client:
        client.format = 'json'
        networks = client.list_networks()
        print "Found %d networks for tenant %s" % (networks.count, project)

    else:
        print 'Did not find a valid nova-client API'
    