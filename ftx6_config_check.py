#!/usr/bin/env python3
# coding: utf-8

# AmRRON, EJ-01

import platform
import re
import sys
import os.path
from os import path
from os.path import expanduser

# Figure out where the JS8Call config file lives on this system.
if(len(sys.argv)>1 and sys.argv[1]=="-c"):
    fname=sys.argv[2]
elif(platform.system()=="Windows"):
    fname=expanduser("~/AppData/Local/JS8Call/JS8Call.ini")
elif("CYGWIN" in platform.system()):
    # If they're using CygWin, we're going to have to make some
    # assumptions (like their home dir is on Drive C:, for
    # example). If it's not, we'll fail to find the config file below
    # and exit, and the user will have to specify their config file
    # manually.
    user=expanduser("~").split("/")[2]
    fname="/cygdrive/c/"+user+"/AppData/Local/JS8Call/JS8Call.ini"
else:
    fname=expanduser("~/.config/JS8Call.ini")

# Validate that the config file is present.
if(path.exists(fname)):
    print("Configuration is being read from: "+fname)
else:
    print("Configuration file not found: "+fname)
    sys.exit(1)    

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

# Extract config info we might find useful.
call=config['[Configuration]']["MyCall"]
spot=config['[Common]']["UploadSpots"]
aprs_spot=config['[Configuration]']["SpotToAPRS"]
grid=config['[Configuration]']["MyGrid"]
groups=list(map(lambda n: n.strip().replace("@@","@"),config['[Configuration]']["MyGroups"].split(",")))
info=config['[Configuration]']["MyInfo"]
status=config['[Configuration]']["MyStatus"]
qth=config['[Configuration]']["MyQTH"]
station=config['[Configuration]']["MyStation"]
tcp_enabled=config['[Configuration]']["TCPEnabled"]
tcp_conns=int(config['[Configuration]']["TCPMaxConnections"])
tcp_addr=config['[Configuration]']["TCPServer"]
tcp_port=int(config['[Configuration]']["TCPServerPort"])
hb_sub=config['[Common]']["SubModeHB"]
tx_freq=int(config['[Common]']["TxFreq"])
write_logs=config['[Configuration]']["WriteLogs"]
beacon_anywhere=config['[Configuration]']["BeaconAnywhere"]
autoreplyonatstartup=config['[Configuration]']["AutoreplyOnAtStartup"]
accept_tcp_requests=config['[Configuration]']["AcceptTCPRequests"]
auto_grid=config['[Configuration]']["AutoGrid"]
dial_freq=config['[Common]']["DialFreq"]

# Main program.
if __name__ == '__main__':
    print("Your callsign is: "+call)
    if(grid):
        if(len(grid)<4):
            print("Your grid is set, but must be at least four characters. Please update GRID.")
        else:
            print("Your grid is: "+grid)
    else:
        print("Your grid must be set in order to port PIR1 status.")
    if(spot):
        print("You are configured to report SPOTs to PSKReporter. Please disable.")
    else:
        print("SPOTting to PSKReporter is properly disabled for this exercise.")
    if(aprs_spot):
        print("You are configured to report APRS. Please disable.")
    else:
        print("APRS reporting is properly disabled for this exercise.")
    if("@AMRFTX" in groups):
        print("@AMRFTX is present in Callsign Groups.")
    else:
        print("@AMRFTX is missing from Callsign Groups. Please add.")
    if(write_logs):
        print("Your system is configured to write logs.")
    else:
        printf("Your system is not configured to write logs. If you're an Aggregation Station, you should fix this. If you're not, writing logs is optional.")
    print("Your INFO field is currently set to: "+info)
    print("Would you like to set a PIR status? (y/n)")
    ans=sys.stdin.readline().strip()
    if(ans=="Y" or ans=="y"):
        print("What is the status of PIR1? (R/Y/G/U)")
        ans=sys.stdin.readline().strip().upper()[0:1]
        if(ans=="R" or ans=="Y" or ans=="G" or ans=="U"):
            print("Please set your INFO field to:")
            print(grid[0:4]+";PIR1="+ans)
        else:
            print("Invalid value for PIR1.")

#Darwin
#Linux
#CYGWIN_NT-10.0-19042
