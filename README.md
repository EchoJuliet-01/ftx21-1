# FTX21-1 Utilities

# Summary

There are two applications included: config_check.py and info.py. The first application checks your JS8Call configuration for compliance with the FTX21-1 exercise recommendations, and alerts you to anything you have set contrary to those guidelines. It makes no changes to your system, it merely informs you as to your status. The second application assists you in setting your INFO field in JS8Call to a value compliant with the exercise requirements. The second application detects whether or not your JS8Call API is configured, and if it is, asks you whether or not you'd like the utility to set your INFO field on your behalf. If you decline, or if your API is not enabled, the utility simply prints your INFO information that you may copy/paste into JS8Call yourself. Note that there is a bug in JS8Call where it will not display the updated INFO field in the GUI. It will work correctly for sending your INFO data, but the current INFO data will not be reflected on your screen. This is a known bug in JS8Call, and a bug report has been filed.

## Compatibility

This software has been written to be compatible with both Python2 and Python3. It has been tested on Linux (both Raspberry Pi and x86_64), Mac/OSX, Windows 10, and Windows 10 with Cygwin. Both Mac/OSX and modern Linux distros come with Python2 pre-installed, and the software will work as-is. Windows will require the installation of Python (either v2 or v3) for this code to function. Installation of Python is beyond the scope of this document, but visiting the python.org website should provide everything you need. If you don't know whether to install Python2 or Python3, here's a rule of thumb: most older existing software was written for Python2, so if you have a specific need to run something older, install Python2. But the future is all Python3, and nearly all legacy Python2 code is being refactored for Python3. If you have no need to run anything older that specifically requires v2, install v3.

## Libraries

There are two libraries included with this software (js8ini.py and js8net.py). These libraries are not intended to be run as stand-alone programs; they provide additional functionality to the two applications. No other libraries outside of the core python functionality are required to use this software. The code in these libraries was factored out to make future software with differing requirements quick and easy to implement.

# Examples

### Linux
```
nobody@mother:~/ftx21-1$ ./config_check.py
Config file: /home/nobody/.config/JS8Call.ini
Your callsign is: N0CLU
Your grid is: EL69
SPOTting to PSKReporter is properly disabled for this exercise.
APRS reporting is properly disabled for this exercise.
@AMRFTX is present in Callsign Groups.
Your system is configured to write logs.
Your INFO field is currently set to: "IC-7300 @ 10W, G5RV @ 25FT"
nobody@mother:~/ftx21-1$
```
### Mac/OSX
```
nobody@MBP ftx21-1 % ./config_check.py
Config file: /Users/nobody/Library/Preferences/JS8Call.ini
Your callsign is: N0CLU
Your grid is: EL69
SPOTting to PSKReporter is properly disabled for this exercise.
APRS reporting is properly disabled for this exercise.
@AMRFTX is present in Callsign Groups.
Your system is configured to write logs.
Your INFO field is currently set to: "IC-7300 @ 10W, G5RV @ 25FT"
nobody@MBP ftx21-1 %
```
### Windows
```
C:\Users\Nobody\ftx21-1>python config_check.py
Config file: C:\Users\Nobody/AppData/Local/JS8Call/JS8Call.ini
Your callsign is: N0CLU
Your grid is: EL69
SPOTting to PSKReporter is properly disabled for this exercise.
APRS reporting is properly disabled for this exercise.
@AMRFTX is present in Callsign Groups.
Your system is configured to write logs.
Your INFO field is currently set to: "IC-7300 @ 10W, G5RV @ 25FT"
C:\Users\Nobody\ftx21-1>
```

EJ-01
