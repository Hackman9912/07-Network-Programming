import socket
import sys
import os
import argparse
import time

data_payload = 2048
backlog = 5

def exit_crit(data, message):
    if data.lower() == 'exit':
        exit(message)

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
    client, address = sock.accept()
    while True:
        try:
            print('Waiting to receive message from the other person')
            data = client.recv(data_payload)
            data = data.decode()
            if data:
                print(data)
                exit_crit(data, 'Your chat buddy exited')
                data = input('Enter your message (exit to exit): ')
                client.send(data.encode())
                exit_crit(data, 'You exited')

        except KeyboardInterrupt:
            print("Closing the server!")
            sock.close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--host', action = 'store', dest = 'host', required = False, default = 'localhost')
    parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = False, default = 15664)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    echo_server(host, port)