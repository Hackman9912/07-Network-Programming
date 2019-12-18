import socket
import sys
import argparse

def echo_client(host, port):
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
        data = b'test'
        print('''Enter the name of the service you want\nto see the port number for!
            ''')
        message = input(': ')
        print(f'Sending: {message}')
        sock.sendall(message.encode())
        # Look for the response
        while data.decode() != "":
            data = sock.recv(64)
            print(f'The port for {message} is {data.decode()}')
    except socket.error as e:
        print(f'Socket error: {str(e)}')
    except Exception as e:
        print(f'Other exception: {str(e)}')
    finally:
        print('Closing the connection to the server.')
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--host', action = 'store', dest = 'host', required = False, default = 'localhost')
    parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = False, default = 15662)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    echo_client(host, port)