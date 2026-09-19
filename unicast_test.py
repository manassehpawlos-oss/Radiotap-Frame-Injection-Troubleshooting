import sys
import os
import sleep

from scapy.all import *

#INDICATE DEV NAME HERE!
dev_name = "wlp0s20u2"

try:
    sleep_period = int(sys.argv[1])
except:
    print("Using default timing value of 1ms")
    sleep_period = 1
    
TA = "AA:AA:AA:AA:AA:AA"
SA = "BB:BB:BB:BB:BB:BB"
seqnum=500

radiotap = RadioTap(bytes.fromhex("000014000e8a000002046c09a000000000003800"))
data_frame = Dot11(addr1 = TA, addr2 = SA, SC=500*16, type=2)
ccmp = Dot11CCMP(bytes.fromhex("46c759cde0ef4a2dafff57c9d73b937a35306ca7dbfd479589cf8b34e68da79eefcacc51aa9085f6b011056872c19b767e04cb8f2ac1e0fde6526163746fe5a61988f81df1804b391b4f8bfbe8b9512431f38763938d83"))
assembled_frame = radiotap/data_frame/ccmp


if os.getuid() == 0:
    print("Beginning scan.")
    time.sleep(1)
    while True:
        sendp(assembled_frame, iface=dev_name)
        time.sleep(sleep_period/1000)
else:
    print("Program not run as sudo, will open Wireshark instead")
    wireshark(assembled_frame)


