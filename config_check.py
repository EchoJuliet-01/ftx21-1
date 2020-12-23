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

    print("Your callsign is: "+call())
    if(ini_grid()):
        if(len(ini_grid())<4):
            print("Your grid is set, but must be at least four characters. Please update GRID. (Settings -> General -> Station -> Station Details -> \"My Maidenhead Grid Locator\")")
        else:
            print("Your grid is: "+ini_grid())
    else:
        print("Your grid must be set in order to port PIR1 status. (Settings -> General -> Station -> Station Details -> \"My Maidenhead Grid Locator\")")
    if(spot()):
        print("You are configured to report SPOTs to PSKReporter. Please disable. (Settings -> Reporting -> Network Services -> \"Enable spotting to reporting networks\")")
    else:
        print("SPOTting to PSKReporter is properly disabled for this exercise.")
    if(aprs_spot()):
        print("You are configured to report APRS. Please disable. (Settings -> Reporting -> Network Services -> \"Enable spotting @APRSIS messages to the APRS-IS network\")")
    else:
        print("APRS reporting is properly disabled for this exercise.")
    if("@AMRFTX" in groups()):
        print("@AMRFTX is present in Callsign Groups.")
    else:
        print("@AMRFTX is missing from Callsign Groups. Please add. (Settings -> General -> Station Details -> Callsign Groups)")
    if(write_logs()):
        print("Your system is configured to write logs.")
    else:
        printf("Your system is not configured to write logs. If you're an Aggregation Station, you should fix this. If you're not, writing logs is optional. (Settings -> General -> Behavior -> Write log files)")
    print("Your INFO field is currently set to: "+ini_info())
