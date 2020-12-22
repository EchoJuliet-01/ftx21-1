#!/usr/bin/env python
# coding: utf-8

# AmRRON, EJ-01

import sys
import socket
import json
import time
import threading
from threading import Thread
from queue import Queue

# These are our global objects (and locks for them).
global tx_queue
global tx_lock
global s
global grid
global info

s=False
grid=False
info=False
tx_queue=Queue()
tx_lock=threading.Lock()

# Add a message to the message queue.
def queue_message(message):
    global tx_queue
    global tx_lock
    with tx_lock:
        tx_queue.put(message)

# This thread watches the transmit queue and sends data to JS8
# whenever it appears in the queue.
def tx_thread(name):
    global tx_queue
    global tx_lock
    # Run forever. Delay 0.25 seconds between each send, because
    # sending too quickly jacks up comms with JS8. There's a python
    # version check here, because Python3 broke the lovely single-byte
    # chars that Python2 had.
    while(True):
        thing=json.dumps(tx_queue.get())
        with tx_lock:
            if(sys.version_info>(3,0)):
                s.sendall(bytes(thing+"\r\n",'utf-8'))
            else:
                s.sendall(thing+"\r\n")
        time.sleep(0.25)

# Due to the way JS8Call sends data to an API client (ie, it just
# sends random JSON data whenever it pleases), we'll receive all
# messages in a thread so it'll all work in the background.
def rx_thread(name):
    global grid
    global info
    n=0
    left=''
    # Run forever.
    while(True):
        try:
            # Get a chunk of text and, if it ends with a \n, process
            # it. If it doesn't, stash it and loop, and tack any
            # leftovers from last go-round on the front of what was
            # received. In theory, we shouldn't ever exceed the 4096
            # bytes, and this won't matter, but just in case...
            raw=(left+s.recv(4096).decode("utf-8")).split('\n')
            if(raw[-1:][0]==''):
                raw=raw[0:-1]
            for stuff in raw:
                if(stuff[-1:]=="}"):
                    thing=json.loads(stuff)
                    if(thing['type']=="STATION.GRID"):
                        grid=thing['value']
                    elif(thing['type']=="STATION.INFO"):
                        info=thing['value']
                else:
                    left=left+stuff
        except socket.timeout:
            # Ignore for now. Do something smarter later. TODO: Be smarter here.
            n=n+1

# Ask JS8Call for my configured GRID square.
def get_grid():
    global grid
    grid=False
    queue_message({'params':{},'type':'STATION.GET_GRID','value':''})
    while(not(grid)):
        time.sleep(0.1)
    return(grid)

# Set a new GRID square in JS8Call.
def set_grid(new_grid):
    queue_message({'params':{},'type':'STATION.SET_GRID','value':new_grid})
    return(get_grid())

# Ask JS8Call for my configured INFO field.
def get_info():
    global info
    info=False
    queue_message({'params':{},'type':'STATION.GET_INFO','value':''})
    while(not(info)):
        time.sleep(0.1)
    return(info)

# Set a new INFO info in JS8Call.
def set_info(new_info):
    queue_message({'params':{},'type':'STATION.SET_INFO','value':new_info})
    return(get_info())

def start_net(host,port):
    global s

    # Open a socket to JS8Call.
    s=socket.socket()
    s.connect((host,port))
    s.settimeout(1)

    # Start the RX thread. We make this a daemon thread so that it
    # will automatically die when the main thread dies. Kind of dirty,
    # but there's no risk of data loss, and the OS will automatically
    # take care of the socket clean-up when the process exits. There's
    # two flavors here, to handle Python2 and Python3.
    if(sys.version_info>(3,0)):
        thread1=Thread(target=rx_thread,args=("RX Thread",),daemon=True)
    else:
        thread1=Thread(target=rx_thread,args=("RX Thread",))
        thread1.daemon=True
    thread1.start()
    # Start the TX thread. Also a daemon thread.
    if(sys.version_info>(3,0)):
        thread2=Thread(target=tx_thread,args=("TX Thread",),daemon=True)
    else:
        thread2=Thread(target=tx_thread,args=("TX Thread",))
        thread2.daemon=True
    thread2.start()

if __name__ == '__main__':
    print("This is a library and is not intended for stand-alone execution.")
