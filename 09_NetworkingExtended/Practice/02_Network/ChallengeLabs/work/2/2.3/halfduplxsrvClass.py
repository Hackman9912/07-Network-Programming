import socket
from socket import AF_INET, SOCK_STREAM
import threading

class ChatServer():
    def __init__(self, host, port, bufsiz):
        self.HOST = host
        self.PORT = port
        self.BUFSIZ = bufsiz
        self.ADDR = (host, port)
        self.chatServSock = socket.socket(AF_INET, SOCK_STREAM)
        self.chatServSock.bind(self.ADDR)

    def recv_msg(self, client):
        msg = client.recv(self.BUFSIZ)
        msg = msg.decode()
        if msg == 'quit()':
            print("Client left the chat.\n")
            exit()
        print("Client:", msg)
        msg = ""
        while msg == "":
            msg = input("-|-> ")

    def send_msg(self, client):
        msg = input(': ')
        if msg == 'quit()':
            client.send(msg.encode())
            exit()

        client.send(msg.encode())

    def run(self):
        self.chatServSock.listen(1) # num can be passed to __init__
        while True:
            print("Waiting for connection...")
            self.chatCliSock, self.cliAddr = self.chatServSock.accept()
            self.chatCliSock.send(b'Connection established. Now we can chat!')
            print("Connected to:", self.cliAddr)
            t1 = threading.Thread(target = self.recv_msg, args = [self.chatCliSock])
            t2 = threading.Thread(target = self.send_msg, args = [self.chatCliSock])
            t1.start()
            t2.start()
        self.chatServSock.close() #not really used


if __name__ == "__main__":
    chatServer = ChatServer('localhost', 33000, 1024)
    chatServer.run()


