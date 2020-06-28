#!/usr/bin/python

import optparse
import socket
from termcolor import cprint, colored
from threading import *
screenLock = Semaphore(value=1)
def connScan(host,port):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((host,int(port)))
        request = 'GET / HTTP/1.1\nHost: {}\n'.format(host)
        connSkt.send(request.encode('utf-8'))
        results = connSkt.recv(1024)
        screenLock.acquire()
        print(colored('[+]','blue'),'Port {} is '.format(port),colored('open','green'))
        print('\n\n',str(results))
    except:
        screenLock.acquire()
        #print(str(e))
       # print(colored('[-]','blue'),'Port {} is '.format(port),colored('closed','red'))

    finally:
        screenLock.release()
        connSkt.close()
def portScan(host,ports):
    try:
        targetIP = socket.gethostbyname(host)
    except Exception as e:
        print(str(e))
        #print(colored('[-] Cannot resolve {}: Unknown host'.format(host),'red'))
        return
    try:
        name = socket.gethostbyaddr(host)
        print('Scan results for : '+name[0])
    except:
        print('Scan results for : '+targetIP)
    socket.setdefaulttimeout(1)
    try:
       for port in range(int(ports[0]),int(ports[1])+1):
            t = Thread(target=connScan, args=(host,port))
            t.start()
    except:
        connScan(host,ports[0])
def main():

    parser = optparse.OptionParser(usage='usage: ./PortScanner.py -H / --host <target host> -p / --port <target port(s)>')

    parser.add_option('-H','--host',dest='host',type='string',help='specify target host')

    parser.add_option('-n','--range',dest='ports',type='string',help='specify target port(s), -n[initial]-[final]')
    options, args = parser.parse_args()

    host = options.host
    tports = str(options.ports).split('-')
    if (host == None) | (tports[0] == None):
        print(parser.usage)
        exit(0)
    portScan(host,tports)
if __name__ == '__main__':
    main()
