import socket
import sys
import argparse
import time
def exit_crit(data, message, sock):
    if data.lower() == 'exit':
        sock.send(b'exit')
        sock.close()
        exit(message)

def echo_client(host, port):
    '''A simple echo client'''
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to the server
    server_address = (host, port)
    print('Connecting to %s port %s' % server_address)
    sock.connect(server_address)
    # send data
    while True:
        try:
            # Send data
            message = input('Enter your message (exit to exit): ')
            sock.sendall(message.encode())
            exit_crit(message, "You quit.", sock)
            # Look for the response
            message = sock.recv(1024)
            message = message.decode()
            print(message)
            exit_crit(message, 'Your buddy quit.', sock)
        except socket.error as e:
            print(f'Socket error: {str(e)}')
        except Exception as e:
            print(f'Other exception: {str(e)}')
        # finally:
        #     print('Closing the connection to the server.')
        #     sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Socket Server Example')
    parser.add_argument('--host', action = 'store', dest = 'host', required = False, default = 'localhost')
    parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = False, default = 15664)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    echo_client(host, port)