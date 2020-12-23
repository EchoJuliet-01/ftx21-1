#!/usr/bin/env python
# coding: utf-8

# AmRRON, EJ-01

import sys
import time
from js8ini import *
from js8net import *

# Main program.
if __name__ == '__main__':
    # Figure out where the JS8Call config file lives on this system.
    if(len(sys.argv)>1 and sys.argv[1]=="-c"):
        state=load_js8_ini(sys.argv[2])
    else:
        state=load_js8_ini()
    
    if(state[0]):
        print("Config file: "+state[1])
    else:
        print("Unable to load configuration file: "+state[1])
        sys.exit(1)

    api=False
    my_grid=False
    my_info=False

    if(tcp_enabled() and tcp_conns()>0 and accept_tcp_requests()):
        start_net(tcp_addr(),tcp_port())
        time.sleep(1)
        my_grid=get_grid()
        my_info=get_info()
        if(len(my_grid)>=4):
            print("Your JS8Call API appears to be enabled and your grid square is set to: "+my_grid)
            api=True

    if(not(my_grid)):
        my_grid=ini_grid()
    if(not(my_info)):
        my_info=ini_info()

    print("Your INFO field is currently set to: "+my_info)
    if(len(my_grid)<4):
        print("Your grid square does not appear to be set. Please set and try again.")
        sys.exit(1)
    print("Would you like to create a PIR status? (y/n)")
    ans=sys.stdin.readline().strip()
    if(ans=="Y" or ans=="y"):
        print("What is the status of PIR1? (R/Y/G/U)")
        ans=sys.stdin.readline().strip().upper()[0:1]
        if(ans=="R" or ans=="Y" or ans=="G" or ans=="U"):
            if(api):
                print("Would you like to set your INFO field via the API? (y/n)")
                qans=sys.stdin.readline().strip().upper()[0:1]
                if(qans=="Y"):
                    set_info(my_grid[0:4]+";PIR1="+ans)
                    print("INFO field has been set to \""+get_info()+"\".\n\nDue to a bug in JS8Call, this will not be reflected in the JS8Call GUI and the value will revert to the old value when JS8Call is restarted, but if you send your INFO field, the correct value will be sent over the air.")
            else:
                print("Please set your INFO field to:")
                print(my_grid[0:4]+";PIR1="+ans)
        else:
            print("Invalid value for PIR1.")
