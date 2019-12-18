from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

SYSTEM = (HOSTNAME, PORTNUMBER)
USER = Socket(AF_INET, SOCK_STREAM)
USER.connect(SYSTEM)
print('User, prepare, to log. in?')
keepplaying = 1
while keepplaying:
    GUESS = input('Enter 0 for rock, 1 for paper, or 2 for scissors: ')
    USER.send(GUESS.encode())
    ANSWER = USER.recv(BUFFER).decode()
    print('>', ANSWER)
    keepplaying = int(input('To quit please press 0, to play again press 1: '))

USER.close()