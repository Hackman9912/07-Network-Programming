from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM
import hashlib
h = hashlib.sha256()
HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

SYSTEM = (HOSTNAME, PORTNUMBER)
USER = Socket(AF_INET, SOCK_STREAM)
USER.connect(SYSTEM)
print('User, prepare, to log. in?')
while True:
    h.update(input('Give password: ').encode())
    has = h.hexdigest()
    GUESS = has
    USER.send(GUESS.encode())
    ANSWER = USER.recv(BUFFER).decode()
    print('>', ANSWER)
    h = hashlib.sha256()
    if ANSWER == 'found the secret':
        break

USER.close()