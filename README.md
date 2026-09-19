# ath9k_htc Radiotap TX_FLAGS Troubleshooting

### Observed Behavior
On Fedora 44 (7.2.5-200.fc44.x86_64), my AR9271 USB wifi adapter disregards the TX_FLAGS parameters corresponding
to a preset sequence number, and no expected ACK. Regardless of if these fields are present or not, injecting the same frame will result in an incrementing sequence number, and
unicast frames are still observed to re-transmit and attempt to be ACKed. The same programs run and transmit properly when used with another SoftMAC adapter (AWUS036ACM, using the r8169 driver) - so supposedly this is an ath9k_htc issue and not a larger mac80211 bug.


### Included files
Four pcap files, corresponding to a repeatedly injected unicast and broadcast frame. The files that end with "..._actual_captures.pcapng" are the injected frames
that were captured from a second wifi-adapter. The files ending with "..._reported.pcapng" were captured from the same ath9k_htc devices used to inject the frame.

Included as well are the Python scripts I used to isolate this. Run it as a regular user to open the to-be-injected frame in Wireshark, and run as sudo to repeatedly transmit frames. Edit the dev_name variable at the top of either file to match your wifi adapter's name.

As well, there's a dmesg from a fresh startup of the system, and my PC's kernel config file.

Thanks for your hard work!


