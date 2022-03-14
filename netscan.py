# ARP scanner that requires input of the interface to listen on and the network range to scan.
# Example: python3 netscan.py eth0 10.1.1.0/24

from scapy.all import *

interface = {sys.argv[1]}
ip_range = {sys.argv[2]}
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac) / ARP(pdst=ip_range)

ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
