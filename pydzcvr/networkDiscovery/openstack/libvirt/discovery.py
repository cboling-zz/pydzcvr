'''


@author:    Chip Boling
@copyright: 2015 Boling Consulting Solutions. All rights reserved.
@license:   Artistic License 2.0, http://opensource.org/licenses/Artistic-2.0
@contact:   support@bcsw.net
@deffield   updated: Updated


Libvirt allows you to access hypervisors running on remote machines through authenticated
and encrypted connections.  On the remote machine, libvirtd should be running in general. 
See the section on configuring libvirtd for more information at https://libvirt.org/remote.html#Remote_libvirtd_configuration

For test purposes, use ssh to connect libvirtd such as: ::
  sudo virsh --readonly --connect qemu+ssh://stack@kiwi-os-compute-01/system list



'''

import libvirt
import sys
import pprint

def discoverAllNodes():
    '''
    Discover VM instances (via libvirt)
    
    TODO: This will change radically, for now, just do some hardcoded calls
          to various interfaces and see what is available.  Evenutally this
          will be consolidated once patterns emerge.
          
    TODO: Make each of the discovery calls below optional based on whether or
          not they have the required APIs installed
    '''
    # use https://libvirt.org/uri.html  for remote access 
    
    '''
    Remote URIs have the general form ("[...]" meaning an optional part):
    driver[+transport]://[username@][hostname][:port]/[path][?extraparameters]
    '''
    uri = 'qemu+ssh://stack@kiwi-os-compute-01/system'
    
    conn = libvirt.openReadOnly(uri)
    if conn == None:
        print 'Failed to open connection to the hypervisor'
        return
    
    try:
        # Get a list of all VM instances

        domains = conn.listAllDomains()

        # Walk each instance and dump its XML
               
        for instance in domains:
            name           = instance.name()
            xmlDescription = instance.XMLDesc()
        
            # Look for <devices.interfaces>  will have a type (probably 'bridge')
            # and under it, the target connection will be 'target/<something>
            # such as:
            #
            # <domain type='qemu' id='2'>
            #  <name>instance-0000002b</name>
            #  ...
            #  <devices>
            #    ...
            #    <interface type='bridge'>
            #      <mac address='fa:16:3e:38:f7:16'/>
            #      <source bridge='br-int'/>
            #      <virtualport type='openvswitch'>
            #        <parameters interfaceid='e32ca2e5-24e7-473d-a9dd-c3ab7ff38097'/>
            #      </virtualport>
            #      <target dev='tape32ca2e5-24'/>
            #      <model type='virtio'/>
            #      <driver name='qemu'/>
            #      <alias name='net0'/>
            #      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
            #    </interface>
            #  ...
            #
            #  for dev in $(virsh dumpxml $instance |
            #    xmllint --xpath '//interface/target/@dev' -); do
            #    dev=${dev#dev=\"}
            #    dev=${dev%\"}
            #    echo "$instance $dev" >> edges
            #  done
        
            pp = pprint.PrettyPrinter(indent=2)
            pp.pprint(xmlDesc)

def discoverInterfaces():
    
    # TODO: Actually, may need to try a variety of uri combinations
    
    uri = 'qemu+ssh://stack@kiwi-os-compute-01/system'
    
    conn = libvirt.openReadOnly(uri)
    if conn == None:
        print 'Failed to open connection to the hypervisor'
        return
    
    try:
        networks = conn.listAllNetworks()
        interfaces = conn.listAllInterfaces()
        domains = conn.listAllDomains()
        
        dom0 = conn.lookupByName("Domain-0")
    except:
        print 'Failed to find the main domain'
        sys.exit(1)
    
    print "Domain 0: id %d running %s" % (dom0.ID(), dom0.OSType())
    print dom0.info()
    
    pass