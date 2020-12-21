#!/usr/bin/env python
# coding: utf-8

# AmRRON, EJ-01

import sys
from js8ini import *

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

    print("Your INFO field is currently set to: "+info())
    print("Would you like to set a PIR status? (y/n)")
    ans=sys.stdin.readline().strip()
    if(ans=="Y" or ans=="y"):
        print("What is the status of PIR1? (R/Y/G/U)")
        ans=sys.stdin.readline().strip().upper()[0:1]
        if(ans=="R" or ans=="Y" or ans=="G" or ans=="U"):
            print("Please set your INFO field to:")
            print(grid()[0:4]+";PIR1="+ans)
        else:
            print("Invalid value for PIR1.")
