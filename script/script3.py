from scapy.all import *

global srcAdd1
global dstAdd1
global srcAdd2
srcAdd2=None
global dstAdd2
srcAdd2=None
global srcAdd3
srcAdd3=None
global dstAdd3
dstAdd3=None
global i
i=0


for packet in PcapReader('/home/asyraf/Desktop/13.pcap'):

 if(packet.haslayer(IP)):
  if(packet.haslayer(TCP)):		
   if(packet[TCP].dport==135):
    srcAdd1=packet.getlayer(IP).src
    dstAdd1=packet.getlayer(IP).dst
 if(packet.haslayer(IP)):
  if(packet.haslayer(TCP)):
   if(packet[TCP].dport==4444):
    srcAdd21=packet.getlayer(IP).src
    dstAdd21=packet.getlayer(IP).dst
    if(srcAdd2 != srcAdd21 and dstAdd3 != dstAdd21):
     srcAdd2=srcAdd21
     dstAdd2=dstAdd21
     print "Attemp connection from "+srcAdd2+" to "+dstAdd2+" using TCP 4444"
     print "Found at packet no(1) : ",i
    elif(srcAdd2 != srcAdd21 and dstAdd3 == dstAdd21):
     srcAdd2=srcAdd21
     dstAdd2=dstAdd21
     print "Attemp connection from "+srcAdd2+" to "+dstAdd2+" using TCP 4444"
     print "Found at packet no(2) : ",i
    elif(srcAdd2 == srcAdd21 and dstAdd2 != dstAdd21):
     srcAdd2=srcAdd21
     dstAdd2=dstAdd21
     print "Attemp connection from "+srcAdd2+" to "+dstAdd2+" using TCP 4444"
     print "Found at packet no(3): ",i
 if(packet.haslayer(IP)):
  if(packet.haslayer(UDP)):
   if(packet[UDP].dport==69):
    srcAdd31=packet.getlayer(IP).src
    dstAdd31=packet.getlayer(IP).dst
    if(srcAdd3 != srcAdd31 and dstAdd3 != dstAdd31):
     srcAdd3=srcAdd31
     dstAdd3=dstAdd31
     print " *Attacker is "+dstAdd3+" and the victim is "+srcAdd3
     print " *Found at packet no(1) : ",i
    elif(srcAdd3 != srcAdd31 and dstAdd3 == dstAdd31):
     srcAdd3=srcAdd31
     dstAdd3=dstAdd31
     print " *Attacker is "+dstAdd3+" and the victim is "+srcAdd3
     print " *Found at packet no(2) : ",i
    elif(srcAdd3 == srcAdd31 and dstAdd3 != dstAdd31):
     srcAdd3=srcAdd31
     dstAdd3=dstAdd31
     print " *Attacker is "+dstAdd3+" and the victim is "+srcAdd3
     print " *Found at packet no(3): ",i
  i=i+1







		


