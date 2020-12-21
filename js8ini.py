#!/usr/bin/env python
# coding: utf-8

# AmRRON, EJ-01

import platform
import re
import os.path
from os import path
from os.path import expanduser

config={}

def load_js8_ini(ini_file=False):
    global config
    # Figure out where the JS8Call config file lives on this system.
    if(ini_file):
        # If the user specified a file name, use it.
        fname=ini_file
    elif(platform.system()=="Windows"):
        # If this is a non-Cygwin Windows system, this is the default
        # config location.
        fname=expanduser("~/AppData/Local/JS8Call/JS8Call.ini")
    elif("CYGWIN" in platform.system()):
        # If they're using CygWin, we're going to have to make some
        # assumptions (like their home dir is on Drive C:, for
        # example). If it's not, we'll fail to find the config file
        # below and exit, and the user will have to specify their
        # config file manually.
        user=expanduser("~").split("/")[2]
        fname="/cygdrive/c/Users/"+user+"/AppData/Local/JS8Call/JS8Call.ini"
    elif(platform.system()=="Darwin"):
        # If this is a Mac is the default config location.
        fname=expanduser("~/Library/Preferences/JS8Call.ini")
    else:
        # If it's anything else (ie, Linux), the default config file
        # is here.
        fname=expanduser("~/.config/JS8Call.ini")
    
    # Validate that the config file is present.
    if(not(path.exists(fname))):
        return([False,fname])
    
    # Suck in the contents of the config file.
    file=open(fname)
    lines=file.readlines()
    file.close()
    
    # Process the contents of the config file.
    config={}
    section=False
    for line in lines:
        line=line.strip()
        if(re.search("^\[.*\]$",line)):
            config[line]={}
            section=line
        else:
            if(re.search("=",line)):
                stuff=line.split("=",2)
                config[section][stuff[0]]=stuff[1]
    return([True,fname])

# Get configured Call Sign.
def call():
    return(config['[Configuration]']["MyCall"])

# True of SPOT is enabled.
def spot():
    if("UploadSpots" in config['[Common]'].keys()):
        if(config['[Common]']["UploadSpots"]=="true"):
            return(True)
        else:
            return(False)
    elif("PSKReporter" in config['[Configuration]'].keys()):
        if(config['[Configuration]']["PSKReporter"]=="true"):
            return(True)
        else:
            return(False)
    else:
        print("This can't happen.")
        return(False)

# True if APRS spotting is enabled.
def aprs_spot():
    if(config['[Configuration]']["SpotToAPRS"]=="true"):
        return(True)
    else:
        return(False)

# Return the configured Grid Square.
def ini_grid():
    return(config['[Configuration]']["MyGrid"])

# Return a list of configured Call Groups.
def groups():
    return(list(map(lambda n: n.strip().replace("@@","@"),config['[Configuration]']["MyGroups"].split(","))))

# Return the currently configured INFO field.
def ini_info():
    return(config['[Configuration]']["MyInfo"])

# Return the currently configured STATUS field.
def status():
    return(config['[Configuration]']["MyStatus"])

# Return the currently configured QTH.
def qth():
    return(config['[Configuration]']["MyQTH"])

# Return the currently configured STATION info.
def station():
    return(config['[Configuration]']["MyStation"])

# True if the TCP API is enabled.
def tcp_enabled():
    if(config['[Configuration]']["TCPEnabled"]=="true"):
        return(True)
    else:
        return(False)

# Return the number of allowed TCP connections.
def tcp_conns():
    return(int(config['[Configuration]']["TCPMaxConnections"]))

# Return the currently configured address the API will respond on.
def tcp_addr():
    return(config['[Configuration]']["TCPServer"])

# Return the currently configured TCP port.
def tcp_port():
    return(int(config['[Configuration]']["TCPServerPort"]))

# True if heartbeats are allowed outside of the heartbeat sub-band.
def hb_sub():
    if(config['[Common]']["SubModeHB"]=="true"):
        return(True)
    else:
        return(False)

# True if heartbeat acks are allowed outside of the heartbeat
# sub-band.
def hb_sub_ack():
    if(config['[Common]']["SubModeHBAck"]=="true"):
        return(True)
    else:
        return(False)

# Offset in hz within the band (ie, added to dial freq).
def tx_freq():
    return(int(config['[Common]']["TxFreq"]))

# True if the system is configured to write log files.
def write_logs():
    if(config['[Configuration]']["WriteLogs"]=="true"):
        return(True)
    else:
        return(False)

# True if the system is allowed to beacon anywhere.
def beacon_anywhere():
    if(config['[Configuration]']["BeaconAnywhere"]=="true"):
        return(True)
    else:
        return(False)

# True if the system is configured to automatically reply.
def autoreplyonatstartup():
    if(config['[Configuration]']["AutoreplyOnAtStartup"]=="true"):
        return(True)
    else:
        return(False)

# True if the system is configured to accept TCP connections.
def accept_tcp_requests():
    if(config['[Configuration]']["AcceptTCPRequests"]=="true"):
        return(True)
    else:
        return(False)

# True if the system allows INFO, STATUS, GRID, etc changes via API.
def auto_grid():
    if(config['[Configuration]']["AutoGrid"]=="true"):
        return(True)
    else:
        return(False)

# Dial frequency of the radio in hz.
def dial_freq():
    return(config['[Common]']["DialFreq"])

if __name__ == '__main__':
    print("This is a library and is not intended for stand-alone execution.")
