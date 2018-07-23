from scapy.all import *

global srcAdd1
global dstAdd1
global srcAdd3
global dstAdd3

dumpfile=rdpcap('/home/asyraf/Desktop/dumpfile_arowana')
print "Finish reading dumpfile"
def filter1():
 global srcAdd2
 global dstAdd2
 for packet in dumpfile:
  if(packet.haslayer(IP)):
   if(packet.haslayer(TCP)):
    if(packet[TCP].dport==4444):
     if(srcAdd1==packet.getlayer(IP).src and dstAdd1==packet.getlayer(IP).dst):
      srcAdd2=packet.getlayer(IP).src
      dstAdd2=packet.getlayer(IP).dst
      return;

def filter2():
 for packet in dumpfile:
  if(packet.haslayer(IP)):
   if(packet.haslayer(UDP)):
    if(packet[UDP].dport==69):
     if(srcAdd2==packet.getlayer(IP).src and dstAdd2==packet.getlayer(IP).dst):
      srcAdd3=packet.getlayer(IP).src
      dstAdd3=packet.getlayer(IP).dst
      print "Attacker is "+dstAdd3+" and the victim is "+srcAdd3
      return;

for packet in dumpfile:
 if(packet.haslayer(IP)):
  if(packet.haslayer(TCP)):		
   if(packet[TCP].dport==135):
    srcAdd1=packet.getlayer(IP).src
    dstAdd1=packet.getlayer(IP).dst
    filter1()
    filter2()


		


