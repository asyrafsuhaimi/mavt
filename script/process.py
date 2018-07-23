from scapy.all import *
from graphviz import Digraph
global packet4444
global packet69
list1=[] #packet69
list2=[] #packet4444
dot = Digraph(comment="Malware Attack Visualize")
dot  #doctest: +ELLIPSIS
dot.attr(size='6,6')
dot.node_attr.update(color='lightblue2', style='filled')

def writetcp(packet):
    wrpcap('/home/asyraf/Desktop/filtered4444.pcap',packet, append=True)

def writeudp(packet):
    wrpcap('/home/asyraf/Desktop/filtered69.pcap',packet, append=True)

def getList():
    print("TCP Packet 4444 filtered.")
    print("UDP Packet 69 filtered.")
    packet4444 = rdpcap('/home/asyraf/Desktop/filtered4444.pcap')
    packet69 = rdpcap('/home/asyraf/Desktop/filtered69.pcap')
    for packet in packet69:
        dest = packet.getlayer(IP).dst
        sour = packet.getlayer(IP).src
        if len(list1) == 0:
            list1.append([dest,sour])
        elif [dest,sour] not in list1:
            list1.append([dest,sour])
    for packet1 in packet4444:
        dest1 = packet1.getlayer(IP).dst
        sour1 = packet1.getlayer(IP).src
        if len(list2) == 0:
            list2.append([sour1,dest1])
        elif [sour1,dest1] not in list2:
            list2.append([sour1,dest1])
    filter1()

def filter1():
    for i in range(len(list2)):
        if(list2[i] in list1):
            print("Attack "+str(list2[i][0])+" "+str(list2[i][1]))
            dot.edge(str(list2[i][0]),str(list2[i][1]),label='attack')
        else:
            print("partial Attack "+str(list2[i][0])+" "+str(list2[i][1]))
            dot.edge(str(list2[i][0]),str(list2[i][1]),label='partial attack')
def initialize():
    print("Begin Analyzing and Filtering Network Packet")
    for packet in PcapReader('/home/asyraf/Desktop/dumpfile_sepat'):
        if(packet.haslayer(IP) and packet.haslayer(TCP) and packet[TCP].dport==4444):
            writetcp(packet)
        elif(packet.haslayer(IP) and packet.haslayer(UDP) and packet[UDP].dport==69):
            writeudp(packet)
        else:
            pass

initialize()
getList()
print(dot.source)
dot.render('test-output/malware_attack.gv', view=True) #doctest: +SKIP
