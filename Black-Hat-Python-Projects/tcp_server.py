import socket
import threading
from termcolor import colored,cprint

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)

print(colored('[*]','red'),colored('Listening on {}:{}...'.format(bind_ip,bind_port),'blue'))

#client-handling thread

def handle_client(client_socket):
    #print what client sends
    request = client_socket.recv(1024)
    print(colored('[*]','red'),colored('Recieverd: {}'.format(request),'green'))

    client_socket.send(b'ACK!')
    client_socket.close()

while True:
    client,addr = server.accept()
    print(colored('[*]','red'),colored('Accepted connection from {}:{}'.format(addr[0],addr[1]),'green'))
    client_handler = threading .Thread(target=handle_client,args=(client,))
    client_handler.start()






