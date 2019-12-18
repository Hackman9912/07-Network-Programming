import socket
import argparse
import threading
def exit_crit(data, message, sock):
    if data.lower() == 'exit':
        sock.send(b'exit')
        sock.close()
        exit(message)

def get_message(client):
    while True:
        message = client.recv(1024)
        message = message.decode()
        print(message)
        exit_crit(message, 'Your chat buddy exited', client)

def send_message(message, client):
    while True:
        client.sendall(message.encode())
        exit_crit(message, 'You exited', client)

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
        message = input('Enter your message: ')
        t1 = threading.Thread(target = send_message, args = [message, sock])
        t2 = threading.Thread(target = get_message, args = [sock])
        t1.start()
        t2.start()
    except socket.error as e:
        print(f'Socket error: {str(e)}')
    except Exception as e:
        print(f'Other exception: {str(e)}')


if __name__ == "__main__":
    echo_client('localhost', 33000)