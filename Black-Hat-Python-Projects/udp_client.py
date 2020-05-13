import socket
from termcolor import colored,cprint

welcome_msg = colored('UDP Client','red',attrs=['reverse','blink'])
print(welcome_msg)

target = input('Enter the hostname:port = ').split(':')
target_host = target[0]
target_port = int(target[1])

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.sendto(b"ABCD",(target_host,target_port))

#recieve some data

data, addr = client.recvfrom(4096)

print(data)

