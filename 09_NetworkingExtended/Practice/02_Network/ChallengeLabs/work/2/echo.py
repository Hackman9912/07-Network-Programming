import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
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
    while True:
        print('Waiting to receive message from client')
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print(f'Data: {data}')
            client.send(data)
            print(f'Sent {len(data)} bytes back to {address}.')
        client.close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
"""-------------------------------------------------------------------------------------- """
import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    '''A simple echo client'''
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to the server
    server_address = (host, port)
    print('Connecting to %s port %s' % server_address)
    sock.connect(server_address)

    # send data
    try:
        # Send data
        message = 'Test message. This will be echoed'
        print(f'Sending: {message}')
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f'Received: {data}')
    except socket.error as e:
        print(f'Socket error: {str(e)}')
    except Exception as e:
        print(f'Other exception: {str(e)}')
    finally:
        print('Closing the connection to the server.')
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)