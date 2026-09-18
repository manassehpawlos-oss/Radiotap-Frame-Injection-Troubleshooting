from scapy.all import *
import sys
import os

#variable to toggle whether the frame is opened in wireshark, or whether transmissions happen.
transmit = True

try:
    sleep_period = int(sys.argv[1])
except:
    print("Using default timing value of 1s")
    sleep_period = 1

radiotap = RadioTap(bytes.fromhex("000014000e8a000002046c09a000000000003800"))


class Dot11EltRates(Packet):
    """ Our own definition for the supported rates field """
    name = "802.11 Rates Information Element"
    # Our Test STA supports the rates 6, 9, 12, 18, 24, 36, 48 and 54 Mbps
    supported_rates = [0x0c, 0x12, 0x18, 0x24, 0x30, 0x48, 0x60, 0x6c]
    fields_desc = [ByteField("ID", 1), ByteField("len", len(supported_rates))]
    for index, rate in enumerate(supported_rates):
        fields_desc.append(ByteField("supported_rate{0}".format(index + 1),
                                     rate))

dot11 = Dot11(
    addr1="00:a0:57:98:76:54",
    addr2="00:a0:57:12:34:56",
    addr3="00:a0:57:98:76:54") / Dot11AssoReq(
        cap=0x1100, listen_interval=0x00a) / Dot11Elt(
            ID=0, info="MY_BSSID")
assembled_frame = radiotap/dot11/Dot11EltRates()

if os.getuid() == 0:
    print("Beginning scan.")
    time.sleep(1)
    while True:
        sendp(assembled_frame, iface="wlan0mon")
        time.sleep(sleep_period)
else:
    print("Program not run as sudo, will open Wireshark instead")
    wireshark(assembled_frame)