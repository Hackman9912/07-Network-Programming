import socket
import argparse
import threading

data_payload = 2048
backlog = 5

def exit_crit(data, message):
    if data.lower() == 'exit':
        exit(message)

def get_message(client):
    while True:
        data = client.recv(data_payload)
        data = data.decode()
        print(data)
        exit_crit(data, 'Your chat buddy exited')

def send_message(message, client):
    while True:
        client.sendall(message.encode())
        exit_crit(message, 'You exited')
def echo_server(host, port):
    '''A simple echo server'''
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print('Starting up echo server on %s port %s' % server_address)
    sock.bind(server_address)
    # listen to clients, backlog argument specifies the max number of queued connections
    sock.listen(backlog)
    sock, server_address = sock.accept()
    try:
        t1 = threading.Thread(target = get_message, args = [sock])
        message = input('Enter your message: ')
        t2 = threading.Thread(target = send_message, args = [message, sock])  
        t1.start()
        t2.start()        
    except KeyboardInterrupt:
        print("Closing the server!")
        sock.close()
    
if __name__ == "__main__":
    echo_server('localhost', 15665)