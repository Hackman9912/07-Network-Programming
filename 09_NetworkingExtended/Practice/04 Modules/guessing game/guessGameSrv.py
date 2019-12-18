from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM
import hashlib


h = hashlib.sha256()
h.update(b'SuperUser')
has = h.hexdigest()
HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

SYSTEM_ADDRESS = (HOSTNAME, PORTNUMBER)
SYSTEM = Socket(AF_INET, SOCK_STREAM)
SYSTEM.bind(SYSTEM_ADDRESS)
SYSTEM.listen(1)

print('Waiting waits for USER to connect')
USER, USER_ADDRESS = SYSTEM.accept()
print('Waiting accepted connection request from ',\
    USER_ADDRESS)
SECRET = has
# SECRET = 'SuperUser'
print(f'the secret is {SECRET}')

while True:
    print('System waits for a guess')
    GUESS = USER.recv(BUFFER).decode()
    print('System received ' + GUESS)
    if GUESS != SECRET:
        REPLY = 'No Good Try Again'
        GUESS = None
    else:
        REPLY = 'found the secret'
    USER.send(REPLY.encode())
    if REPLY == 'found the secret':
        break

SYSTEM.close()
