'''
Setup script for pydzcvr

@author:    Chip Boling
@copyright: 2015 Boling Consulting Solutions. All rights reserved.
@license:   Artistic License 2.0, http://opensource.org/licenses/Artistic-2.0
@contact:   support@bcsw.net
@deffield   updated: Updated
'''
from setuptools import setup
from setuptools import find_packages
from pydzcvr.version import __version__
import os

# Get version information. This file must use execfile and not be imported                                                 
execfile(os.path.join("pydzcvr", "version.py"))

setup(
    name='pydzcvr',
    version=__version__,
    author='BCSW',
    author_email='support@bcsw.net',
    maintainer='Chip Boling',
    maintainer_email="support@bcsw.net",
    url='https://github.com/cboling/pydzcvr/',
    platforms="any",
    packages=find_packages(exclude='samples'),
    license='Artistic License 2.0, http://opensource.org/licenses/Artistic-2.0',
    entry_points={'console_scripts' : ['pydzcvr=pydzcvr.pydzcvr:main',
                                      ]},
    description='OpenStack and SDN Internal Network Path Discovery Application',
    long_description=open('README.md').read(),
    test_suite='pydzcvr.tests.runalltests.suite',
    install_requires=[
        # Currently pygraphviz will be used as the drawing package.  An external
        # web interface/javascript package may be added later if not delivered
        # within this package (which is most likely at this point).
        "pygraphviz == 1.2",
        "SQLAlchemy == 0.9.7",
        "python-novaclient == 2.23.0",
        "python-neutronclient == 2.3.11",
        "python-openstackclient == 1.0.2",
    ],
)
