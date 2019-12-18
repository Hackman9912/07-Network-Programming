import socket
from socket import AF_INET, SOCK_STREAM
import threading

class ChatClnt():
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.ADDR = (host, port)
        self.chatCliSock = socket.socket(AF_INET, SOCK_STREAM)

    def recv_msg(self, client):
        msg = client.recv(2048)
        msg = msg.decode()
        if msg == 'quit()':
            print("Client left the chat.\n")
            exit()
        print("Client:", msg)
        msg = ""
        while msg == "":
            msg = input("-|-> ")

    def send_msg(self, client, msg):
        if msg == 'quit()':
            client.send(msg.encode())
            exit()
        client.send(msg.encode())

    def run(self):
        self.chatCliSock.connect(self.ADDR)
        while True:
            message = input('Enter your message: ')
            t1 = threading.Thread(target = self.recv_msg, args = [self.chatCliSock])
            t2 = threading.Thread(target = self.send_msg, args = [self.chatCliSock, message])
            t2.start()
            t1.start()
        self.chatCliSock.close()


if __name__ == "__main__":
    chatClnt = ChatClnt('localhost', 33000)
    chatClnt.run()