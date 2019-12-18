from random import randint
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

game = ['rock', 'paper', 'scissors']
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
SECRET = randint(0,2)

print(f'the secret is {SECRET}')

while True:
    print('System waits for a guess')
    GUESS = int(USER.recv(BUFFER).decode())
    print('System received ' + game[GUESS])
    if GUESS == SECRET:
        REPLY = 'It was a tie!'
    elif SECRET == 2 and GUESS == 0:
        REPLY = 'The Computer won'
    elif SECRET == 0 and GUESS == 2:
        REPLY = 'You won'
    elif SECRET > GUESS:
        REPLY = 'You lost'
    elif SECRET < GUESS:
        REPLY = 'You Won'
    USER.send(REPLY.encode())
    if REPLY == 'You Won':
        break

SYSTEM.close()