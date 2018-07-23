from scapy.all import *


global srcAdd1
global dstAdd1
global srcAdd2
global dstAdd2
global srcAdd3
global dstAdd3
global i
i=0
global j
j=1

for packet in PcapReader('/home/asyraf/Desktop/dumpfile_sepat'):
 if(packet.haslayer(IP)):
  if(packet.haslayer(TCP)):		
   if(packet[TCP].dport==135):
    srcAdd1=packet.getlayer(IP).src
    dstAdd1=packet.getlayer(IP).dst
 if(packet.haslayer(IP)):
  if(packet.haslayer(TCP)):
   if(packet[TCP].dport==4444):
    srcAdd2=packet.getlayer(IP).src
    dstAdd2=packet.getlayer(IP).dst
 if(packet.haslayer(IP)):
  if(packet.haslayer(UDP)):
   if(packet[UDP].dport==69):
    srcAdd3=packet.getlayer(IP).src
    dstAdd3=packet.getlayer(IP).dst
    print "Attacker is "+dstAdd3+" and the victim is "+srcAdd3





		


