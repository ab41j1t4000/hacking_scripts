import socket
from termcolor import colored,cprint

welcome_msg = colored('Welcome to my first Black Hat Python Project','red',attrs=['reverse','blink'])
print(welcome_msg)
print('Format {hostname}:{port}')
target = input('Enter the target: ').split(':')
target_host = target[0]
target_port = int(target[1])

#create socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

request = 'GET / HTTP/1.1\nHost: {}\n\n'.format(target_host).encode('utf-8')
#send some data
client.send(request)

#recieve some data
response = client.recv(1024)

cprint(response,'green')





